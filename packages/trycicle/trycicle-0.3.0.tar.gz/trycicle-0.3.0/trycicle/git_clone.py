import logging
import os
import shutil
import tempfile
import typing

from .subprocess import get_command_output, run_command

logger = logging.getLogger(__name__)


def create_clean_copy(source_dir: str) -> str:
    toplevel = get_command_output(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=source_dir or None,
    )

    clone_dir = tempfile.mkdtemp()
    os.chmod(clone_dir, 0o755)

    run_command(["git", "clone", "--local", toplevel, clone_dir], check=True)
    run_command(
        ["git", "remote", "set-url", "origin", "/repo"], cwd=clone_dir, check=True
    )

    # TODO: What if source_dir is not a subdirectory of toplevel? Is this possible?
    return os.path.join(clone_dir, os.path.relpath(source_dir or os.getcwd(), toplevel))


def remove_copy(clone_dir: str) -> None:
    status = get_command_output(
        ["git", "status", "--porcelain"],
        cwd=clone_dir,
    )
    if status:
        logger.warning(f"Some files in {clone_dir!r} have been changed")
        return

    toplevel = get_command_output(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=clone_dir,
    )
    rmtree_warn_errors(toplevel)


def rmtree_warn_errors(path: str) -> None:
    errors = 0

    def onerror(*args: typing.Any) -> None:
        nonlocal errors
        errors += 1

    shutil.rmtree(path, onerror=onerror)
    if errors:
        logger.warning(f"Unable to remove {errors} files from {path!r}")
