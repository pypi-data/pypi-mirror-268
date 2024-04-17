import logging
import os
import shutil
import sys
import tempfile
import threading
import typing
from datetime import datetime

from docker import DockerClient
from docker.errors import ImageNotFound
from docker.models.containers import Container

from .cache import get_cache_path, pull_cache, push_cache
from .models import Job, Service
from .subprocess import run_command
from .variables import Variables, get_all_variables

logger = logging.getLogger(__name__)

job_script_shebang = "#!/bin/sh\n"

job_script_header = """\
git config --global --add safe.directory /src 2>/dev/null || true
set -x
"""

job_script_debugger = """\
# Start a shell if the script fails
function debugger() {
    set +x
    if [ -n "$1" ]; then
       echo "Job failed, starting debug shell." >&2
       echo "Last command: $BASH_COMMAND" >&2
    fi
    echo "The job script is available at $0" >&2
    echo "The job will continue after you exit this shell. To abort, type 'exit 1'" >&2
    ${SHELL:-sh} || exit 1
    set -x
}
trap 'debugger trap' ERR
"""

DebugEnabled = typing.Literal["true", "false", "immediate"]


def write_job_script(
    filename: str,
    before_script: list[str],
    script: list[str],
    debugger: DebugEnabled = "false",
) -> None:
    with open(filename, "w") as fp:
        print(job_script_shebang.strip(), file=fp)
        if debugger != "false":
            print(job_script_debugger.strip(), file=fp)
        print(job_script_header.strip(), file=fp)
        if debugger == "immediate":
            print("debugger", file=fp)
        if before_script:
            print("", file=fp)
            print("# Before", file=fp)
            print("\n".join(before_script), file=fp)
        if script:
            print("", file=fp)
            print("# Script", file=fp)
            print("\n".join(script), file=fp)
    os.chmod(filename, 0o755)


dind_volumes = {"dind-certs": {"bind": "/certs/client", "mode": "rw"}}


def run_job(
    job: Job,
    source_dir: str,
    original_dir: str,
    service_logs: bool = False,
    debugger: DebugEnabled = "false",
    cache_directory: str = "",
) -> int:
    job_start = datetime.utcnow()
    docker = DockerClient.from_env()

    source_dir = os.path.abspath(source_dir)
    original_dir = os.path.abspath(original_dir)
    build_dir = tempfile.mkdtemp()
    os.chmod(build_dir, 0o755)
    logger.debug(f"Using temporary build directory {build_dir}")

    job_sh = os.path.join(build_dir, "job.sh")
    write_job_script(job_sh, job.before_script, job.script, debugger)

    variables = get_all_variables(job, original_dir)

    labels = {
        "trycicle": "true",
        "trycicle.workdir": original_dir,
        "trycicle.job": job.name,
    }

    service_containers = [
        run_service(docker, service, variables, labels, service_logs)
        for service in job.services
    ]
    links = {
        container.id: service.alias
        for service, container in zip(job.services, service_containers)
    }

    volumes = {
        source_dir: {"bind": "/src", "mode": "rw"},
        build_dir: {"bind": "/build", "mode": "ro"},
    }

    if original_dir != source_dir:
        volumes[original_dir] = {"bind": "/repo", "mode": "ro"}

    if any(service.is_docker_dind for service in job.services):
        volumes.update(dind_volumes)

    cache_paths = [
        os.path.join(cache_directory, get_cache_path(cache, variables, original_dir))
        for cache in job.cache
    ]
    for cache_path, cache in zip(cache_paths, job.cache):
        pull_cache(cache, variables, cache_path, source_dir)

    job_image = variables.replace(job.image.name)
    logger.info(f"Starting job ({job_image})")

    interactive = debugger != "false"
    container = create_container(
        docker,
        image=job_image,
        detach=True,
        tty=True,
        stdin_open=interactive,
        command=["/build/job.sh"],
        entrypoint=variables.replace_list(job.image.entrypoint),
        environment=variables.as_dict(),
        volumes=volumes,
        links=links,
        working_dir="/src",
        labels=labels,
    )

    if service_containers:
        stop_event_thread = start_event_thread(docker, links, job_start)

    if interactive:
        interactive_session(container)
    else:
        container.start()
        write_logs(container, b"job | " if service_logs else b"")

    status_code = int(container.wait()["StatusCode"])
    logger.debug(f"Job finished with exit code {status_code}")

    if service_containers:
        logger.debug(f"Stopping {len(service_containers)} service containers")
        stop_event_thread()
        for container in service_containers:
            container.stop()

    for cache_path, cache in zip(cache_paths, job.cache):
        if (
            cache.when == "always"
            or (cache.when == "on_success" and status_code == 0)
            or (cache.when == "on_failure" and status_code != 0)
        ):
            push_cache(cache, variables, cache_path, source_dir)

    shutil.rmtree(build_dir)
    # TODO: Remove containers? (on success only?)
    return status_code


def write_logs(container: Container, prefix: bytes = b"") -> None:
    """Write logs from a container to stdout, optionally prefixing every line.

    Because this function is called from multiple threads, it internally buffers the
    logs until a newline is found, to avoid mixing output from different containers.
    """
    buffer = b""
    for chunk in container.logs(stream=True, follow=True):
        buffer += chunk
        if not buffer:
            continue

        # Split the accumulated buffer into lines. If the last line is complete, output
        # everything. Otherwise, keep the last line in the buffer, and output the rest.
        lines = buffer.splitlines(keepends=True)
        if lines[-1].endswith(b"\n"):
            buffer = b""
        else:
            buffer = lines.pop()

        for line in lines:
            sys.stdout.buffer.write(prefix + line)
            sys.stdout.flush()

    # Output the last line, if any.
    if buffer:
        sys.stdout.buffer.write(prefix + buffer + b"\n")


def start_log_thread(container: Container, prefix: bytes = b"") -> None:
    thread = threading.Thread(
        target=write_logs,
        args=(container, prefix),
        daemon=True,
    )
    thread.start()


def create_container(docker: DockerClient, **kwargs: typing.Any) -> Container:
    try:
        return docker.containers.create(**kwargs)
    except ImageNotFound:
        docker.images.pull(kwargs["image"])
        return docker.containers.create(**kwargs)


def run_service(
    docker: DockerClient,
    service: Service,
    variables: Variables,
    labels: dict[str, str],
    logs: bool,
) -> Container:
    service_variables = variables + service.variables
    service_image = service_variables.replace(service.name)

    volumes = {}
    if service.is_docker_dind:
        volumes.update(dind_volumes)

    logger.info(f"Starting service {service.alias} ({service_image})")
    container = create_container(
        docker,
        image=service_image,
        detach=True,
        command=service_variables.replace_list(service.command),
        entrypoint=service_variables.replace_list(service.entrypoint),
        environment=service_variables.as_dict(),
        privileged=service.is_docker_dind,
        volumes=volumes,
        labels={"trycicle.service": service.alias, **labels},
    )
    container.start()

    if logs:
        start_log_thread(container, f"{service.alias} | ".encode())

    return container


def start_event_thread(
    docker: DockerClient, containers: dict[str, str], since: datetime
) -> typing.Callable[[], None]:
    # We're only interested in events for the services
    filters = {
        "type": ["container"],
        "container": list(containers.keys()),
    }
    event_stream = docker.events(filters=filters, since=since, decode=True)

    thread = threading.Thread(
        target=consume_events,
        args=(event_stream, containers),
        daemon=True,
    )
    thread.start()

    return event_stream.close  # type: ignore[no-any-return]


class DockerEventActor(typing.TypedDict):
    ID: str
    Attributes: dict[str, str]


class DockerEvent(typing.TypedDict):
    Type: str
    Action: str
    Actor: DockerEventActor
    scope: str
    time: int
    timeNano: int


def consume_events(
    stream: typing.Iterable[DockerEvent], containers: dict[str, str]
) -> None:
    unhealthy: set[str] = set()

    for event in stream:
        alias = containers.get(event["Actor"]["ID"])
        if alias is None:
            continue

        match event["Action"]:
            case "die":
                status = event["Actor"]["Attributes"]["exitCode"]
                verb = "finished" if status == "0" else "died"
                logger.warning(f"Service {alias} {verb} with exit code {status}")
            case "oom":
                logger.warning(f"Service {alias} ran out of memory")
            case "health_status: healthy":
                if alias in unhealthy:
                    logger.info(f"Service {alias} is healthy")
                    unhealthy.remove(alias)
            case "health_status: unhealthy":
                if alias not in unhealthy:
                    logger.warning(f"Service {alias} is unhealthy")
                    unhealthy.add(alias)


def interactive_session(container: Container) -> None:
    # Unfortunately, docker-py doesn't seem to support interactively attaching
    # to a running container, so we have to shell out.
    run_command(["docker", "start", "--attach", "--interactive", container.id])
