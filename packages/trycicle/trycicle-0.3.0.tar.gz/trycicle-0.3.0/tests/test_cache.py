import os
import pathlib
import typing
from unittest import mock

import pytest

from trycicle.cache import copy_matching, get_cache_path, pull_cache, push_cache
from trycicle.models import Cache
from trycicle.variables import Variables


def test_cache_path_simple_key() -> None:
    cache = Cache(key="test")
    variables = Variables({})
    assert get_cache_path(cache, variables, "project") == "cache-project-test"


def test_cache_path_key_variable() -> None:
    cache = Cache(key="cache-$CI_COMMIT_REF_SLUG")
    variables = Variables({"CI_COMMIT_REF_SLUG": "main"})
    assert get_cache_path(cache, variables, "project") == "cache-project-cache-main"


def test_cache_path_key_file() -> None:
    cache = Cache(key_files=["a.txt"])
    variables = Variables({})

    with mock.patch("trycicle.cache.get_command_output") as git_log:
        git_log.return_value = "sha"
        assert get_cache_path(cache, variables, "project") == "cache-project-sha"

    git_log.assert_called_once_with(
        ["git", "log", "--pretty=format:%H", "-1", "--", "a.txt"],
        cwd="project",
    )


def test_cache_path_key_file_prefix() -> None:
    cache = Cache(key_files=["a.txt"], key_prefix="prefix")
    variables = Variables({})

    with mock.patch("trycicle.cache.get_command_output") as git_log:
        git_log.return_value = "sha"
        assert get_cache_path(cache, variables, "project") == "cache-project-prefix-sha"


def test_cache_path_key_files() -> None:
    cache = Cache(key_files=["a.txt", "b.txt"])
    variables = Variables({})

    with mock.patch("trycicle.cache.get_command_output") as git_log:
        git_log.side_effect = ["sha1", "sha2"]
        assert get_cache_path(cache, variables, "project") == "cache-project-sha1-sha2"

    assert git_log.call_count == 2


def test_recursive_matching() -> None:
    current_file = pathlib.Path(__file__)
    tests_dir = current_file.parent
    source_dir = tests_dir.parent
    variables = Variables({})
    with mock.patch("shutil.copy") as copy:
        copy_matching(["**/*.py"], variables, str(source_dir), "destination")

    assert copy.call_count >= 1
    copy.assert_any_call(
        current_file, pathlib.Path("destination") / tests_dir.name / current_file.name
    )


def test_copy_directory() -> None:
    current_file = pathlib.Path(__file__)
    tests_dir = current_file.parent
    source_dir = tests_dir.parent
    variables = Variables({})
    with mock.patch("shutil.copytree") as copytree:
        copy_matching([tests_dir.name], variables, str(source_dir), "destination")

    copytree.assert_called_once_with(
        tests_dir, pathlib.Path("destination") / tests_dir.name, dirs_exist_ok=True
    )


def test_copy_ignores_special(tmp_path: pathlib.Path) -> None:
    # Create a (dangling) symlink
    link = tmp_path / "link"
    link.symlink_to(tmp_path / "target")

    # Make sure the pattern matches the link
    assert link in list(tmp_path.glob("*"))

    variables = Variables({})
    with mock.patch("shutil.copy") as copy:
        with mock.patch("shutil.copytree") as copytree:
            copy_matching(["*"], variables, str(tmp_path), "destination")

    copy.assert_not_called()
    copytree.assert_not_called()


@pytest.mark.parametrize("policy", ["pull", "push", "pull-push"])
@pytest.mark.parametrize("direction", ["pull", "push"])
def test_push_pull(
    policy: typing.Literal["pull", "push", "pull-push"],
    direction: typing.Literal["pull", "push"],
) -> None:
    cache = Cache(paths=["**"], policy=policy)
    with mock.patch("trycicle.cache.copy_matching") as copy_matching:
        f = pull_cache if direction == "pull" else push_cache
        f(cache, Variables({}), os.path.dirname(__file__), "/tmp/source")
    assert copy_matching.call_count == int(direction in policy)
