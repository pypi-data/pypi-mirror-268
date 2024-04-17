import pathlib
from unittest import mock

import pytest

from trycicle.variables import Variables, get_commit_variables, get_project_variables


def test_commit_variables(git_repo: pathlib.Path) -> None:
    variables = get_commit_variables(str(git_repo))

    assert variables["CI_COMMIT_AUTHOR"] == "Test <test@example.org>"
    assert variables["CI_COMMIT_BRANCH"] == "main"
    assert variables["CI_COMMIT_REF_NAME"] == "main"
    assert len(variables["CI_COMMIT_SHA"]) == 40
    assert len(variables["CI_COMMIT_SHORT_SHA"]) == 8

    assert variables["CI_COMMIT_TITLE"] == "Add b.txt"
    assert (
        variables["CI_COMMIT_DESCRIPTION"]
        == "Here is a longer description of why this was necessary."
    )
    assert (
        variables["CI_COMMIT_MESSAGE"]
        == "Add b.txt\n\nHere is a longer description of why this was necessary."
    )


@pytest.mark.parametrize(
    "origin",
    [
        "git@gitlab.com:phooijenga/trycicle.git",
        "https://gitlab.com/phooijenga/trycicle.git",
    ],
)
def test_project_variables(origin: str) -> None:
    with mock.patch("trycicle.variables.get_command_output") as get_command_output:
        get_command_output.return_value = origin
        variables = get_project_variables(".")

    assert variables["CI_REPOSITORY_URL"] == origin
    assert variables["CI_PROJECT_NAME"] == "trycicle"
    assert variables["CI_PROJECT_NAMESPACE"] == "phooijenga"
    assert variables["CI_PROJECT_URL"] == "https://gitlab.com/phooijenga/trycicle"


def test_replace_variables() -> None:
    variables = Variables({"FOO": "bar", "BAR": "baz", "QUX": "$FOO ${BAR}"})
    replaced = variables.as_dict()
    assert replaced["FOO"] == "bar"
    assert replaced["QUX"] == "bar baz"


def test_replace_variable_warns_undefined_once(
    caplog: pytest.LogCaptureFixture,
) -> None:
    with caplog.at_level("WARNING"):
        replaced = Variables({"FOO": "$BAR", "QUX": "$BAR"}).as_dict()

    assert replaced["FOO"] == "$BAR"
    assert "Undefined variable 'BAR'" in caplog.text
    assert caplog.text.count("Undefined variable") == 1


def test_add_variables() -> None:
    a = Variables({"a": "1"})
    b = Variables({"b": "2"})
    combined = a + b
    assert combined.as_dict() == {"a": "1", "b": "2"}


def test_add_variables_dict() -> None:
    a = Variables({"a": "1"})
    b = {"b": "2"}
    combined = a + b
    assert combined.as_dict() == {"a": "1", "b": "2"}


def test_add_variables_unsupported() -> None:
    a = Variables({"a": "1"})
    with pytest.raises(TypeError):
        _ = a + 1
