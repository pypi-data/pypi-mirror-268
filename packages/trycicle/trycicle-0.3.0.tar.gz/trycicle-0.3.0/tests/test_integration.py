import dataclasses
import fcntl
import logging
import os
import pathlib
import re
import shlex
import subprocess
import sys
import time
import typing
from unittest import mock

import pytest

from trycicle.cache import get_cache_path
from trycicle.cli import main
from trycicle.models import Cache
from trycicle.variables import Variables, slugify


def test_basic_job(capfd: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit, match="0"):
        main(["--verbose", "--file", "tests/basic.yml", "job"])

    out, err = capfd.readouterr()
    assert "Hello, world!" in out


def test_meta(capfd: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit, match="0"):
        main(["--verbose", "--file", "tests/meta.yml", "--workdir", ".", "test"])

    out, err = capfd.readouterr()
    assert "test session starts" in out
    assert "FAILURES" not in out


@dataclasses.dataclass
class Example:
    section: str
    config: str
    commands: list[str]
    expected: list[str]


def extract_markdown_examples(path: str) -> typing.Iterable[Example]:
    with open(path) as fp:
        markdown = fp.read()

    last_section = "none"
    last_config = ""

    for match in re.finditer(
        r"^#+ (?P<section>.*?)$|^```(?P<language>\w+)\n(?P<code>.*?)\n```$",
        markdown,
        flags=re.MULTILINE | re.DOTALL,
    ):
        if section := match.group("section"):
            last_section = section
            continue

        language, code = match.group("language", "code")
        if language == "yaml":
            last_config = code
            continue

        if language == "console":
            lines = code.splitlines()
            commands = [
                line.removeprefix("$ ") for line in lines if line.startswith("$ ")
            ]
            expected = [line for line in lines if not line.startswith("$ ")]
            yield Example(last_section, last_config, commands, expected)


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    if "readme_example" in metafunc.fixturenames:
        examples = extract_markdown_examples("README.md")
        metafunc.parametrize(
            "readme_example",
            [
                pytest.param(example, id=slugify(example.section))
                for example in examples
            ],
        )


def get_readme_cache_path(cache: Cache, variables: Variables, source_dir: str) -> str:
    return get_cache_path(cache, variables, "readme")


def test_readme_example(
    monkeypatch: pytest.MonkeyPatch,
    readme_example: Example,
    tmp_path: pathlib.Path,
    capfd: pytest.CaptureFixture[str],
    get_commit_variables: mock.MagicMock,
    get_project_variables: mock.MagicMock,
) -> None:
    monkeypatch.setenv("USER", "paul")

    config = tmp_path / "gitlab-ci.yml"
    config.write_text(readme_example.config)

    # Send logs to stdout to simplify test
    logging.basicConfig(level=logging.INFO, stream=sys.stdout, force=True)
    logging.getLogger("trycicle").setLevel(logging.NOTSET)

    for command in readme_example.commands:
        args = shlex.split(command)
        if args[0] == "trycicle":
            with (
                pytest.raises(SystemExit, match="0"),
                mock.patch("trycicle.run.get_cache_path", new=get_readme_cache_path),
            ):
                main(["--file", str(config), *args[1:]])
        else:
            subprocess.run(command, check=True, shell=True, cwd=tmp_path)

    output = capfd.readouterr().out.splitlines()
    i, skip = 0, False
    for line in readme_example.expected:
        print(f"{i=} {skip=} {output[i]=} {line=}")
        if line == "...":
            skip = True
            continue

        # Skip forward until we find the expected line
        while skip and i < len(output) and output[i] != line:
            i += 1

        if i >= len(output):
            raise AssertionError(f"{line} not found in output")

        assert output[i] == line
        i += 1
        skip = False


def run_interactive(
    args: list[str], debugger_commands: list[bytes], prompt: bytes = b" # "
) -> tuple[int, bytes]:
    process = subprocess.Popen(
        [sys.executable, "-m", "trycicle", *args],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        cwd=pathlib.Path(__file__).parent.parent,
    )

    assert process.stdin is not None
    assert process.stdout is not None

    # Make stdout non-blocking
    fd = process.stdout.fileno()
    flags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)

    output = b""
    while process.poll() is None:
        chunk = process.stdout.read()
        if chunk is None:
            time.sleep(0.1)
            continue

        output += chunk
        sys.stdout.buffer.write(chunk)

        if output.endswith(prompt):
            if command := debugger_commands.pop(0):
                process.stdin.write(command + b"\n")
                process.stdin.flush()
            else:
                print(
                    "Warning: prompt received but no more commands available.",
                    file=sys.stderr,
                )
                process.stdin.close()

    return process.returncode, output


def test_interactive_debugger() -> None:
    args = ["--file", "tests/basic.yml", "--debug", "immediate", "job"]
    status, output = run_interactive(args, [b"id", b"exit"])

    assert status == 0
    assert b"The job script is available at /build/job.sh" in output
    assert b"The job will continue after you exit this shell" in output
    assert b"uid=0(root) gid=0(root) groups=0(root),10(wheel)" in output
    assert b"Hello, world!" in output


def test_interactive_debugger_abort() -> None:
    args = ["--file", "tests/basic.yml", "--debug", "immediate", "job"]
    status, output = run_interactive(args, [b"exit 1"])

    assert status == 1
    assert b"The job script is available at /build/job.sh" in output
    assert b"The job will continue after you exit this shell" in output
    assert b"Hello, world!" not in output
