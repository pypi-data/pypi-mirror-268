import itertools
import os
import pathlib
import typing
from unittest import mock

import pytest
from docker.errors import ImageNotFound

from trycicle.models import Cache, Job, JobImage, Service
from trycicle.run import (
    DockerEvent,
    consume_events,
    create_container,
    job_script_debugger,
    job_script_header,
    job_script_shebang,
    run_job,
    write_job_script,
    write_logs,
)

pytestmark = pytest.mark.usefixtures("get_commit_variables", "get_project_variables")


def test_write_job_script(tmp_path: pathlib.Path) -> None:
    job_script = tmp_path / "job.sh"
    write_job_script(str(job_script), ["echo before"], ["echo script"])
    script_text = """
# Before
echo before

# Script
echo script
"""

    expected_script = job_script_shebang + job_script_header + script_text
    assert job_script.read_text() == expected_script


def test_write_job_script_no_before(tmp_path: pathlib.Path) -> None:
    job_script = tmp_path / "job.sh"
    write_job_script(str(job_script), [], ["echo script"])
    script_text = """
# Script
echo script
"""

    expected_script = job_script_shebang + job_script_header + script_text
    assert job_script.read_text() == expected_script


def test_write_job_script_debugger(tmp_path: pathlib.Path) -> None:
    job_script = tmp_path / "job.sh"
    write_job_script(str(job_script), [], [], debugger="true")
    expected_script = job_script_shebang + job_script_debugger + job_script_header
    assert job_script.read_text() == expected_script


def test_write_job_script_debugger_immediate(tmp_path: pathlib.Path) -> None:
    job_script = tmp_path / "job.sh"
    write_job_script(str(job_script), ["echo before"], [], debugger="immediate")
    script = job_script.read_text().splitlines()
    assert script.index("debugger") < script.index("echo before")


@pytest.fixture(name="docker_client")
def mock_docker_client() -> typing.Iterable[mock.MagicMock]:
    with mock.patch("docker.client.DockerClient.from_env") as from_env:
        client = from_env.return_value
        container = client.containers.create.return_value
        type(container).id = mock.PropertyMock(
            side_effect=(f"id-{i}" for i in itertools.count(1))
        )
        container.logs.return_value = [b"logs"]
        container.wait.return_value = {"StatusCode": 0}
        yield client


def test_run(docker_client: mock.MagicMock) -> None:
    job = Job(
        name="test",
        image=JobImage(name="busybox:latest"),
    )
    run_job(job, "", "")

    assert docker_client.containers.create.call_count == 1
    run_args = docker_client.containers.create.call_args
    assert run_args.kwargs["image"] == "busybox:latest"
    assert run_args.kwargs["command"] == ["/build/job.sh"]


def test_run_service(docker_client: mock.MagicMock) -> None:
    job = Job(
        name="test",
        image=JobImage(name="busybox:latest"),
        services=[Service("mysql:latest", "mysql")],
    )
    run_job(job, "", "")

    assert docker_client.containers.create.call_count == 2
    service_args = docker_client.containers.create.call_args_list[0]
    assert service_args.kwargs["image"] == "mysql:latest"

    job_args = docker_client.containers.create.call_args_list[1]
    assert job_args.kwargs["image"] == "busybox:latest"
    links = job_args.kwargs["links"]
    assert links == {"id-1": "mysql"}

    assert docker_client.containers.create.return_value.stop.call_count == 1


def test_run_labels(docker_client: mock.MagicMock) -> None:
    job = Job(
        name="test",
        image=JobImage(name="busybox:latest"),
        services=[Service("mysql:latest", "mysql")],
    )
    run_job(job, "", "")

    assert docker_client.containers.create.call_count == 2
    service_args = docker_client.containers.create.call_args_list[0]
    service_labels = service_args.kwargs["labels"]
    assert service_labels == {
        "trycicle": "true",
        "trycicle.job": "test",
        "trycicle.workdir": os.getcwd(),
        "trycicle.service": "mysql",
    }

    job_args = docker_client.containers.create.call_args_list[1]
    job_labels = job_args.kwargs["labels"]
    assert job_labels == {
        "trycicle": "true",
        "trycicle.job": "test",
        "trycicle.workdir": os.getcwd(),
    }


def test_run_service_command(docker_client: mock.MagicMock) -> None:
    job = Job(
        name="test",
        image=JobImage("busybox:latest"),
        services=[
            Service(
                "mysql:latest",
                "mysql",
                entrypoint=["exec"],
                command=["ls"],
            )
        ],
    )
    run_job(job, "", "")

    assert docker_client.containers.create.call_count == 2
    service_args = docker_client.containers.create.call_args_list[0]
    assert service_args.kwargs["image"] == "mysql:latest"
    assert service_args.kwargs["entrypoint"] == ["exec"]
    assert service_args.kwargs["command"] == ["ls"]

    assert docker_client.containers.create.return_value.stop.call_count == 1


def test_run_service_specific_variables(docker_client: mock.MagicMock) -> None:
    job = Job(
        name="test",
        image=JobImage(name="busybox:latest"),
        variables={"FOO": "bar"},
        services=[
            Service(
                "postgres:latest",
                "postgres",
                variables={"POSTGRES_PASSWORD": "test"},
            )
        ],
    )
    with mock.patch("shutil.rmtree"):
        run_job(job, "", "")

    assert docker_client.containers.create.call_count == 2
    service_args = docker_client.containers.create.call_args_list[0]
    assert service_args.kwargs["image"] == "postgres:latest"

    service_environment = service_args.kwargs["environment"]
    assert service_environment["FOO"] == "bar"
    assert service_environment["POSTGRES_PASSWORD"] == "test"

    job_args = docker_client.containers.create.call_args_list[1]
    assert job_args.kwargs["image"] == "busybox:latest"

    job_environment = job_args.kwargs["environment"]
    assert job_environment["FOO"] == "bar"
    assert "POSTGRES_PASSWORD" not in job_environment


def test_run_extra_dind_flags(docker_client: mock.MagicMock) -> None:
    job = Job(
        name="test",
        image=JobImage(name="busybox:latest"),
        services=[Service("docker:dind", "docker")],
    )
    run_job(job, "", "")

    assert docker_client.containers.create.call_count == 2
    service_args = docker_client.containers.create.call_args_list[0]
    assert service_args.kwargs["image"] == "docker:dind"
    assert service_args.kwargs["privileged"] is True
    service_volumes = service_args.kwargs["volumes"]
    assert "dind-certs" in service_volumes

    job_args = docker_client.containers.create.call_args_list[1]
    job_volumes = job_args.kwargs["volumes"]
    assert job_volumes["dind-certs"] == service_volumes["dind-certs"]


def test_run_entrypoint(docker_client: mock.MagicMock) -> None:
    job = Job(
        name="test",
        image=JobImage(name="busybox:latest", entrypoint=["/bin/sh", "-c"]),
    )
    run_job(job, "", "")

    assert docker_client.containers.create.call_count == 1
    run_args = docker_client.containers.create.call_args
    assert run_args.kwargs["image"] == "busybox:latest"
    assert run_args.kwargs["entrypoint"] == ["/bin/sh", "-c"]
    assert run_args.kwargs["command"] == ["/build/job.sh"]


def test_run_original_volume(docker_client: mock.MagicMock) -> None:
    job = Job(
        name="test",
        image=JobImage(name="busybox:latest"),
    )
    run_job(job, "source", "original")

    assert docker_client.containers.create.call_count == 1
    run_args = docker_client.containers.create.call_args
    volumes = run_args.kwargs["volumes"]
    assert any(
        volume.endswith("/source") and args == {"bind": "/src", "mode": "rw"}
        for volume, args in volumes.items()
    )
    assert any(
        volume.endswith("/original") and args == {"bind": "/repo", "mode": "ro"}
        for volume, args in volumes.items()
    )


def test_run_with_logs(
    docker_client: mock.MagicMock, capsys: pytest.CaptureFixture[str]
) -> None:
    job = Job(
        name="test",
        image=JobImage(name="busybox:latest"),
        services=[
            Service(
                "postgres:latest",
                "postgres",
            ),
        ],
    )
    run_job(job, "", "", service_logs=True)

    out, _ = capsys.readouterr()
    assert "job | logs\n" in out
    assert "postgres | logs\n" in out


def test_run_with_debugger(docker_client: mock.MagicMock) -> None:
    with mock.patch("trycicle.run.run_command") as run_command:
        job = Job(
            name="test",
            image=JobImage(name="busybox:latest"),
        )
        run_job(job, "", "", debugger="true")

    assert run_command.call_count == 1
    command = run_command.call_args.args[0]
    assert command[:2] == ["docker", "start"]
    assert command[-1] == "id-1"


def test_run_with_cache(docker_client: mock.MagicMock) -> None:
    job = Job(
        name="test",
        image=JobImage(name="busybox:latest"),
        cache=[Cache(policy="pull-push", paths=["test"])],
    )
    with (
        mock.patch("trycicle.run.pull_cache") as pull_cache,
        mock.patch("trycicle.run.push_cache") as push_cache,
    ):
        run_job(job, "", "")

    pull_cache.assert_called_once()
    push_cache.assert_called_once()


def test_run_with_cache_push_when(docker_client: mock.MagicMock) -> None:
    always = Cache()
    on_success = Cache(when="on_success")
    on_failure = Cache(when="on_failure")

    job = Job(
        name="test",
        image=JobImage(name="busybox:latest"),
        cache=[always, on_success, on_failure],
    )
    with (
        mock.patch("trycicle.run.pull_cache") as pull_cache,
        mock.patch("trycicle.run.push_cache") as push_cache,
    ):
        run_job(job, "", "")

    assert pull_cache.call_count == 3
    assert push_cache.call_count == 2
    assert push_cache.call_args_list[0].args[0] is always
    assert push_cache.call_args_list[1].args[0] is on_success


@pytest.mark.parametrize(
    "events,expected",
    [
        pytest.param(
            [
                {
                    "Type": "container",
                    "Action": "die",
                    "Actor": {"ID": "test", "Attributes": {"exitCode": "1"}},
                }
            ],
            ["Service test died with exit code 1"],
            id="die",
        ),
        pytest.param(
            [
                {
                    "Type": "container",
                    "Action": "die",
                    "Actor": {"ID": "test", "Attributes": {"exitCode": "0"}},
                }
            ],
            ["Service test finished with exit code 0"],
            id="finish",
        ),
        pytest.param(
            [
                {
                    "Type": "container",
                    "Action": "oom",
                    "Actor": {"ID": "test", "Attributes": {}},
                }
            ],
            ["Service test ran out of memory"],
            id="oom",
        ),
        pytest.param(
            [
                {
                    "Type": "container",
                    "Action": "health_status: unhealthy",
                    "Actor": {"ID": "test", "Attributes": {}},
                }
            ],
            ["Service test is unhealthy"],
            id="unhealthy",
        ),
        pytest.param(
            [
                {
                    "Type": "container",
                    "Action": "health_status: healthy",
                    "Actor": {"ID": "test", "Attributes": {}},
                }
            ],
            [],
            id="healthy",
        ),
        pytest.param(
            [
                {
                    "Type": "container",
                    "Action": "health_status: unhealthy",
                    "Actor": {"ID": "test", "Attributes": {}},
                },
                {
                    "Type": "container",
                    "Action": "health_status: healthy",
                    "Actor": {"ID": "test", "Attributes": {}},
                },
            ],
            ["Service test is unhealthy", "Service test is healthy"],
            id="recovery",
        ),
        pytest.param(
            [
                {
                    "Type": "container",
                    "Action": "health_status: unhealthy",
                    "Actor": {"ID": "test", "Attributes": {}},
                },
                {
                    "Type": "container",
                    "Action": "health_status: unhealthy",
                    "Actor": {"ID": "test", "Attributes": {}},
                },
            ],
            ["Service test is unhealthy"],
            id="unhealthy",
        ),
        pytest.param(
            [
                {
                    "Type": "container",
                    "Action": "die",
                    "Actor": {"ID": "unknown", "Attributes": {"exitCode": "1"}},
                }
            ],
            [],
            id="unknown-container",
        ),
        pytest.param(
            [
                {
                    "Type": "container",
                    "Action": "start",
                    "Actor": {"ID": "test", "Attributes": {}},
                }
            ],
            [],
            id="unknown-action",
        ),
    ],
)
def test_consume_events(
    events: list[DockerEvent], expected: list[str], caplog: pytest.LogCaptureFixture
) -> None:
    consume_events(events, {"test": "test"})
    assert caplog.messages == expected


def test_write_logs(capsys: pytest.CaptureFixture[str]) -> None:
    container = mock.MagicMock()
    container.logs.return_value = [b"line 1\n", b"line 2\n"]
    write_logs(container, b"test | ")
    out, _ = capsys.readouterr()
    assert out == "test | line 1\ntest | line 2\n"


def test_write_logs_no_final_newline(capsys: pytest.CaptureFixture[str]) -> None:
    container = mock.MagicMock()
    container.logs.return_value = [b"line 1\n", b"line 2"]
    write_logs(container, b"test | ")
    out, _ = capsys.readouterr()
    assert out == "test | line 1\ntest | line 2\n"


def test_write_logs_unbuffered(capsys: pytest.CaptureFixture[str]) -> None:
    container = mock.MagicMock()
    container.logs.return_value = map(bytes, zip(b"line 1\nline 2\n"))
    write_logs(container, b"test | ")
    out, _ = capsys.readouterr()
    assert out == "test | line 1\ntest | line 2\n"


def test_write_logs_empty_chunk(capsys: pytest.CaptureFixture[str]) -> None:
    container = mock.MagicMock()
    container.logs.return_value = [b"", b"logs", b"\n"]
    write_logs(container, b"test | ")
    out, _ = capsys.readouterr()
    assert out == "test | logs\n"


def test_create_container_retries_image_not_found(
    docker_client: mock.MagicMock,
) -> None:
    docker_client.containers.create.side_effect = ImageNotFound("test")

    with pytest.raises(ImageNotFound):
        create_container(docker_client, image="image")

    docker_client.images.pull.assert_called_once_with("image")
    assert docker_client.containers.create.call_count == 2
