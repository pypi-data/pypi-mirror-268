import logging
import shlex
import subprocess
import typing

logger = logging.getLogger(__name__)


def run_command(
    args: list[str], **kwargs: typing.Any
) -> subprocess.CompletedProcess[str]:
    logger.debug(f"Running {args[0]}: " + " ".join(shlex.quote(arg) for arg in args))
    return subprocess.run(args, **kwargs)


def get_command_output(args: list[str], **kwargs: typing.Any) -> str:
    p = run_command(args, check=True, capture_output=True, text=True, **kwargs)
    return p.stdout.removesuffix("\n")
