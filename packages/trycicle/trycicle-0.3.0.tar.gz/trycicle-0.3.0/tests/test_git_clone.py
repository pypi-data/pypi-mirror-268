import pathlib

import pytest

from trycicle.git_clone import create_clean_copy, remove_copy, rmtree_warn_errors


def test_create_clean_copy(git_repo: pathlib.Path) -> None:
    copy_path = pathlib.Path(create_clean_copy(str(git_repo)))
    assert copy_path.is_dir()

    copy_file = copy_path / "a.txt"
    assert copy_file.read_text() == "Hello, world!\n"


def test_create_clean_copy_from_dirty_repo(git_repo: pathlib.Path) -> None:
    repo_file = git_repo / "a.txt"
    repo_file.write_text("Some changes that are not committed\n")

    copy_path = pathlib.Path(create_clean_copy(str(git_repo)))
    assert copy_path.is_dir()

    copy_file = copy_path / "a.txt"
    assert copy_file.read_text() == "Hello, world!\n"


def test_create_copy_from_subdir(git_repo: pathlib.Path) -> None:
    copy_path = pathlib.Path(create_clean_copy(str(git_repo / "subdir")))
    assert copy_path.is_dir()

    assert copy_path.name == "subdir"

    copy_file = copy_path / "b.txt"
    assert copy_file.read_text() == "Second file\n"


def test_remove_copy(git_repo: pathlib.Path) -> None:
    remove_copy(str(git_repo))
    assert not git_repo.exists()


def test_remove_copy_from_subdirectory(git_repo: pathlib.Path) -> None:
    remove_copy(str(git_repo / "subdir"))
    assert not git_repo.exists()


def test_keep_dirty_copy(
    git_repo: pathlib.Path, caplog: pytest.LogCaptureFixture
) -> None:
    repo_file = git_repo / "a.txt"
    repo_file.write_text("Some changes that are not committed\n")

    with caplog.at_level("WARNING"):
        remove_copy(str(git_repo))
    assert git_repo.exists()

    assert len(caplog.messages) == 1
    assert str(git_repo) in caplog.messages[0]


def test_remove_warn_errors(
    tmp_path: pathlib.Path, caplog: pytest.LogCaptureFixture
) -> None:
    with caplog.at_level("WARNING"):
        rmtree_warn_errors(str(tmp_path / "does-not-exist"))

    assert len(caplog.messages) == 1
    assert "Unable to remove 1 files" in caplog.messages[0]
