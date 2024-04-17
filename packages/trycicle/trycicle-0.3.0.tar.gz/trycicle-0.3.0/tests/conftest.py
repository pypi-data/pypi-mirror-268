import pathlib
import re
import subprocess
import typing
from unittest import mock

import pytest


@pytest.fixture
def git_repo(tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch) -> pathlib.Path:
    monkeypatch.setenv("GIT_AUTHOR_NAME", "Test")
    monkeypatch.setenv("GIT_COMMITTER_NAME", "Test")
    monkeypatch.setenv("GIT_AUTHOR_EMAIL", "test@example.org")
    monkeypatch.setenv("GIT_COMMITTER_EMAIL", "test@example.org")

    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init", "--initial-branch=main"], cwd=str(repo), check=True)
    subprocess.run(
        ["git", "commit", "--allow-empty", "-m", "Initial commit"],
        cwd=str(repo),
        check=True,
    )

    file = repo / "a.txt"
    file.write_text("Hello, world!\n")

    subprocess.run(["git", "add", "a.txt"], cwd=str(repo), check=True)
    subprocess.run(["git", "commit", "-m", "Add a.txt"], cwd=str(repo), check=True)

    subdir = repo / "subdir"
    subdir.mkdir()
    file_in_subdirectory = subdir / "b.txt"
    file_in_subdirectory.write_text("Second file\n")

    subprocess.run(["git", "add", "subdir/b.txt"], cwd=str(repo), check=True)
    subprocess.run(
        [
            "git",
            "commit",
            "-m",
            "Add b.txt\n\nHere is a longer description of why this was necessary.\n",
        ],
        cwd=str(repo),
        check=True,
    )

    return repo


@pytest.fixture(name="mkdtemp", autouse=True)
def mock_mkdtemp(
    request: pytest.FixtureRequest,
    tmp_path_factory: pytest.TempPathFactory,
) -> typing.Iterable[None]:
    basename = re.sub(r"\W+", "_", request.node.name).strip("_")

    def mkdtemp() -> str:
        return str(tmp_path_factory.mktemp(basename, numbered=True))

    with mock.patch("tempfile.mkdtemp", new=mkdtemp):
        yield


@pytest.fixture(name="get_commit_variables")
def mock_get_commit_variables() -> typing.Iterable[mock.MagicMock]:
    with mock.patch("trycicle.variables.get_commit_variables") as get_commit_variables:
        get_commit_variables.return_value = {"CI_COMMIT_SHA": "test"}
        yield get_commit_variables


@pytest.fixture(name="get_project_variables")
def mock_get_project_variables() -> typing.Iterable[mock.MagicMock]:
    with mock.patch("trycicle.variables.get_project_variables") as get_variables:
        get_variables.return_value = {}
        yield get_variables
