import logging
import os
import pathlib
import shutil

from .models import Cache
from .subprocess import get_command_output
from .variables import Variables

logger = logging.getLogger(__name__)


def get_last_commit(name: str, source_dir: str) -> str:
    return get_command_output(
        ["git", "log", "--pretty=format:%H", "-1", "--", name],
        cwd=source_dir or None,
    )


def get_cache_path(cache: Cache, variables: Variables, source_dir: str) -> str:
    key_fragments = ["cache", os.path.basename(source_dir)]
    if cache.key_prefix is not None:
        key_fragments.append(cache.key_prefix)
    if cache.key is not None:
        key_fragments.append(cache.key)
    if cache.key_files is not None:
        key_fragments += [get_last_commit(name, source_dir) for name in cache.key_files]

    cache_key = variables.replace("-".join(key_fragments))
    assert "/" not in cache_key
    logger.info(f"Using cache {cache_key!r}")
    return cache_key


def copy_matching(
    paths: list[str],
    variables: Variables,
    source: str,
    destination: str,
) -> None:
    source_path = pathlib.Path(source)
    destination_path = pathlib.Path(destination)
    for pattern in paths:
        for match in source_path.glob(variables.replace(pattern)):
            target = destination_path / match.relative_to(source_path)
            logger.debug(f"Copying {match} to {target}")
            os.makedirs(target.parent, exist_ok=True)
            if match.is_dir():
                shutil.copytree(match, target, dirs_exist_ok=True)
            elif match.is_file():
                shutil.copy(match, target)


def pull_cache(
    cache: Cache, variables: Variables, cache_path: str, source_dir: str
) -> None:
    if cache.policy in {"pull", "pull-push"} and cache.paths:
        # TODO: Cache should not overwrite existing files
        copy_matching(cache.paths, variables, cache_path, source_dir)


def push_cache(
    cache: Cache, variables: Variables, cache_path: str, source_dir: str
) -> None:
    if cache.policy in {"push", "pull-push"} and cache.paths:
        copy_matching(cache.paths, variables, source_dir, cache_path)
