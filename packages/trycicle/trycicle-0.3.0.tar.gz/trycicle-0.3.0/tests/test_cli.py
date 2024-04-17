import logging
import typing
from unittest import mock

import pytest
from click.shell_completion import ShellComplete
from click.testing import CliRunner, Result

from trycicle.cli import main
from trycicle.models import Config


@pytest.fixture(name="parse_config")
def mock_parse_config() -> typing.Iterable[mock.MagicMock]:
    config = Config(
        globals={"image": "busybox:latest"},
        default={},
        variables={},
        jobs={"deploy": {}},
    )

    with mock.patch("trycicle.cli.parse_config") as parse_config:
        parse_config.return_value = config
        yield parse_config


@pytest.fixture(name="run_job")
def mock_run_job() -> typing.Iterable[mock.MagicMock]:
    with mock.patch("trycicle.cli.run_job") as run_job:
        run_job.return_value = 0
        yield run_job


def run_main(*args: str) -> Result:
    runner = CliRunner(mix_stderr=False)
    return runner.invoke(main, args)


def test_no_job(parse_config: mock.MagicMock) -> None:
    result = run_main()
    assert result.exit_code == 0

    parse_config.assert_called_once()
    assert parse_config.call_args.args[0].name == ".gitlab-ci.yml"

    assert "Available jobs:" in result.stderr
    assert "  - deploy" in result.stderr


def test_job_not_found(parse_config: mock.MagicMock) -> None:
    result = run_main("invalid")
    assert result.exit_code == 1

    parse_config.assert_called_once()
    assert parse_config.call_args.args[0].name == ".gitlab-ci.yml"

    assert "Available jobs:" in result.stderr
    assert "  - deploy" in result.stderr


def test_job_list_does_not_include_templates(parse_config: mock.MagicMock) -> None:
    parse_config.return_value.jobs[".hidden"] = {}

    result = run_main()
    assert result.exit_code == 0

    assert ".hidden" not in result.stderr


def test_run_job(parse_config: mock.MagicMock, run_job: mock.MagicMock) -> None:
    result = run_main("deploy")
    assert result.exit_code == 0
    assert run_job.call_count == 1
    job = run_job.call_args.args[0]
    assert job.image.name == "busybox:latest"


def test_run_propagates_exit_code(
    parse_config: mock.MagicMock, run_job: mock.MagicMock
) -> None:
    run_job.return_value = 5
    result = run_main("deploy")
    assert result.exit_code == 5


def test_create_clean_copy(
    parse_config: mock.MagicMock, run_job: mock.MagicMock
) -> None:
    with mock.patch("trycicle.cli.create_clean_copy") as create_clean_copy:
        create_clean_copy.return_value = "/tmp/copy"
        with mock.patch("trycicle.cli.remove_copy") as remove_copy:
            result = run_main("--clean", "deploy")
    assert result.exit_code == 0

    create_clean_copy.assert_called_once_with("")
    remove_copy.assert_called_once_with("/tmp/copy")


def test_set_job_variable(
    parse_config: mock.MagicMock, run_job: mock.MagicMock
) -> None:
    result = run_main("--env", "FOO=bar", "-e", "BAZ=qux", "deploy")
    assert result.exit_code == 0
    job = run_job.call_args.args[0]
    assert job.variables["FOO"] == "bar"
    assert job.variables["BAZ"] == "qux"


def test_set_job_variable_from_environment(
    parse_config: mock.MagicMock,
    run_job: mock.MagicMock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("FOO", "bar")
    result = run_main("-e", "FOO", "deploy")
    assert result.exit_code == 0
    job = run_job.call_args.args[0]
    assert job.variables["FOO"] == "bar"


@pytest.mark.parametrize(
    "verbose,root_level,package_level",
    [
        pytest.param(0, "INFO", "NOTSET", id="default"),
        pytest.param(1, "INFO", "DEBUG", id="verbose"),
        pytest.param(2, "DEBUG", "DEBUG", id="extra"),
    ],
)
def test_cli_verbose(verbose: int, root_level: str, package_level: str) -> None:
    # Remove existing handlers, otherwise the basicConfig call will do nothing
    root_logger = logging.getLogger()
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
        h.close()

    result = CliRunner().invoke(main, ["--verbose"] * verbose)
    assert result.exit_code == 0, result.stdout

    assert logging.getLevelName(root_logger.level) == root_level
    assert logging.getLevelName(logging.getLogger("trycicle").level) == package_level


@pytest.mark.parametrize(
    "incomplete,file,expected",
    [
        pytest.param("", "missing", ["SHELL", "USER"], id="environment"),
        pytest.param("U", "missing", ["USER"], id="prefix"),
        pytest.param("X", "missing", [], id="no-match"),
        pytest.param("USER=", "missing", [], id="complete"),
        pytest.param("", "tests/basic.yml", ["NAME", "SHELL", "USER"], id="variable"),
        pytest.param(
            "",
            "tests/example.yml",
            [
                "AWS_ACCOUNT_ID",
                "DOCKER_CERT_PATH",
                "DOCKER_HOST",
                "DOCKER_TLS_CERTDIR",
                "DOCKER_TLS_VERIFY",
                "MODULE",
                "TEST_KUBE_CONTEXT",
                "SHELL",
                "USER",
            ],
            id="multiple-jobs",
        ),
        pytest.param(
            "DOCK",
            "tests/example.yml",
            [
                "DOCKER_CERT_PATH",
                "DOCKER_HOST",
                "DOCKER_TLS_CERTDIR",
                "DOCKER_TLS_VERIFY",
            ],
            id="variable-prefix",
        ),
        pytest.param("X", "README.md", [], id="invalid-file"),
    ],
)
def test_complete_variables(incomplete: str, file: str, expected: list[str]) -> None:
    complete = ShellComplete(main, {}, "trycicle", "")
    with mock.patch("os.environ", {"USER": "paul", "SHELL": "/usr/bin/fish"}):
        items = complete.get_completions(["-f", file, "-e"], incomplete)

    assert [item.value for item in items] == expected


@pytest.mark.parametrize(
    "incomplete,file,expected",
    [
        pytest.param("", "missing", [], id="no-file"),
        pytest.param("", "README.md", [], id="invalid-file"),
        pytest.param(
            "",
            "tests/example.yml",
            ["operator integration tests", "operator tests"],
            id="jobs",
        ),
        pytest.param(".t", "tests/example.yml", [".tests"], id="hidden-jobs"),
    ],
)
def test_complete_jobs(incomplete: str, file: str, expected: list[str]) -> None:
    complete = ShellComplete(main, {}, "trycicle", "")
    items = complete.get_completions(["-f", file], incomplete)
    assert [item.value for item in items] == expected
