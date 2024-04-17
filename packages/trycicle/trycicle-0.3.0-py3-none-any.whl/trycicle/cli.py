import logging
import os
import sys
import typing

import click
import platformdirs
from click.shell_completion import CompletionItem

from .git_clone import create_clean_copy, remove_copy
from .models import Job
from .parser import parse_config
from .run import DebugEnabled, run_job


def complete_variables(
    ctx: click.Context, param: click.Parameter, incomplete: str
) -> list[CompletionItem]:
    if "=" in incomplete:
        return []

    variable_names: set[str] = set()
    if ctx.params["file"]:
        try:
            config = parse_config(ctx.params["file"])
        except Exception:
            pass
        else:
            variable_names = config.all_variable_names()

    variables = [
        CompletionItem(k, help="Variable")
        for k in sorted(variable_names)
        if k.startswith(incomplete)
    ]

    environment = [
        CompletionItem(k, help="Environment")
        for k in sorted(os.environ)
        if k.startswith(incomplete)
    ]
    return variables + environment


def complete_job(
    ctx: click.Context, param: click.Parameter, incomplete: str
) -> list[CompletionItem]:
    if not ctx.params["file"]:
        return []

    try:
        config = parse_config(ctx.params["file"])
    except Exception:
        return []

    return [
        CompletionItem(name, help="Job")
        for name in sorted(config.jobs)
        if name.startswith(incomplete)
        and (incomplete.startswith(".") or not name.startswith("."))
    ]


@click.command(name="trycicle")
@click.option(
    "--verbose",
    "-v",
    count=True,
    help="Verbose output",
)
@click.option(
    "--service-logs/--no-service-logs",
    default=False,
    help="Display logs from services",
)
@click.option(
    "--workdir",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    metavar="DIR",
    help="Working directory",
)
@click.option(
    "--clean/--in-place",
    default=False,
    help="Run in a clean copy of the repository",
)
@click.option(
    "--env",
    "-e",
    metavar="KEY[=VALUE]",
    multiple=True,
    help="Environment variables to pass to the job",
    shell_complete=complete_variables,
)
@click.option(
    "--file",
    "-f",
    type=click.File("r"),
    metavar="YAML",
    help="Path to the .gitlab-ci.yml file",
    default=".gitlab-ci.yml",
)
@click.option(
    "--debug",
    type=click.Choice(("true", "false", "immediate"), case_sensitive=False),
    is_flag=False,
    flag_value="true",
    default="false",
    help="Enable interactive debugging",
)
@click.option(
    "--cache-directory",
    type=click.Path(file_okay=False, dir_okay=True),
    metavar="DIR",
    help="Directory to store cache files",
    default=platformdirs.user_cache_dir("trycicle"),
)
@click.argument(
    "job_name",
    metavar="JOB",
    required=False,
    shell_complete=complete_job,
)
def main(
    verbose: int,
    service_logs: bool,
    workdir: str | None,
    clean: bool,
    env: list[str],
    file: typing.TextIO,
    job_name: str | None,
    debug: DebugEnabled,
    cache_directory: str,
) -> None:
    configure_logging(verbose)

    config = parse_config(file)
    if job_name not in config.jobs:
        if job_name is not None:
            click.echo(f"Job {job_name!r} not found in {file!r}", err=True)
        click.echo("Available jobs:", err=True)
        for name in config.jobs:
            if not name.startswith("."):
                click.echo(f"  - {name}", err=True)
        sys.exit(0 if job_name is None else 1)

    job = config.get_job(job_name)
    set_variables(job, env)

    source_dir = workdir or os.path.dirname(file.name)
    original_dir = source_dir
    if clean:
        source_dir = create_clean_copy(original_dir)

    result = run_job(
        job, source_dir, original_dir, service_logs, debug, cache_directory
    )

    if clean:
        remove_copy(source_dir)

    sys.exit(result)


def configure_logging(verbose: int) -> None:
    logging.basicConfig(level=logging.INFO)
    if verbose >= 2:
        logging.getLogger().setLevel(logging.DEBUG)
    elif verbose:
        logging.getLogger(__package__).setLevel(logging.DEBUG)


def set_variables(job: Job, variables: list[str]) -> None:
    for variable in variables:
        if "=" in variable:
            key, value = variable.split("=", 1)
        else:
            key, value = variable, os.environ[variable]
        job.variables[key] = value
