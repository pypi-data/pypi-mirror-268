import io

import pytest

from trycicle.models import Reference
from trycicle.parser import (
    all_parents,
    extend,
    load_config,
    parse_config,
    parse_image,
    parse_job,
    parse_service,
    resolve_references,
)


def test_parse_config() -> None:
    with open("tests/example.yml") as fp:
        config = parse_config(fp)
    assert len(config.jobs) == 5
    assert "operator tests" in config.jobs
    assert "variables" not in config.jobs
    assert config.variables["AWS_ACCOUNT_ID"] == "123456"


def test_parse_job() -> None:
    with open("tests/example.yml") as fp:
        config = parse_config(fp)

    job = config.get_job("operator integration tests")
    assert job.image.name == "python:3.11"
    assert "pipenv install --deploy --dev" in job.before_script
    assert "pipenv run ci-coverage -k integration" in job.script
    assert job.variables["MODULE"] == "operator"
    assert job.services[0].name == "docker:20-dind"


def test_parser_missing_defaults() -> None:
    config = parse_config(io.StringIO("{}"))
    assert config.variables == {}
    assert config.jobs == {}


def test_parser_defaults() -> None:
    config_file = io.StringIO(
        """\
variables:
  FOO: bar
before_script:
  - echo "Hello, world!"
services:
  - postgres:latest
cache:
  key: test
job:
  image: test
  script: echo
"""
    )
    config = parse_config(config_file)
    job = config.get_job("job")
    assert job.variables == {"FOO": "bar"}
    assert job.before_script == ['echo "Hello, world!"']
    assert job.services is not None
    assert job.services[0].name == "postgres:latest"
    assert job.cache is not None
    assert job.cache[0].key == "test"
    assert job.script == ["echo"]


def test_parse_service_from_string() -> None:
    service = parse_service("docker:20-dind")
    assert service.name == "docker:20-dind"
    assert service.alias == "docker"


def test_parse_service_alias() -> None:
    service = parse_service("tutum/wordpress:latest")
    assert service.alias == "tutum-wordpress"


def test_parse_service_dict() -> None:
    service = parse_service({"name": "docker:20-dind", "alias": "test"})
    assert service.name == "docker:20-dind"
    assert service.alias == "test"


def test_parse_service_with_command() -> None:
    service = parse_service({"name": "docker:20-dind", "command": "ls -la"})
    assert service.name == "docker:20-dind"
    assert service.alias == "docker"
    assert service.command == ["ls", "-la"]


def test_parse_service_with_command_list() -> None:
    service = parse_service({"name": "docker:20-dind", "command": ["ls", "-la"]})
    assert service.name == "docker:20-dind"
    assert service.command == ["ls", "-la"]


def test_parse_service_invalid() -> None:
    with pytest.raises(ValueError, match="Unable to parse service"):
        parse_service([])


def test_parse_image_from_string() -> None:
    image = parse_image("busybox:latest")
    assert image.name == "busybox:latest"
    assert image.entrypoint is None


def test_parse_image_from_dict() -> None:
    image = parse_image({"name": "busybox:latest"})
    assert image.name == "busybox:latest"
    assert image.entrypoint is None


def test_parse_image_with_entrypoint() -> None:
    image = parse_image({"name": "busybox:latest", "entrypoint": "sh"})
    assert image.name == "busybox:latest"
    assert image.entrypoint == ["sh"]


def test_parse_image_with_entrypoint_arguments() -> None:
    image = parse_image({"name": "busybox:latest", "entrypoint": ["/bin/sh", "-c"]})
    assert image.name == "busybox:latest"
    assert image.entrypoint == ["/bin/sh", "-c"]


def test_parse_image_invalid() -> None:
    with pytest.raises(ValueError, match="Unable to parse image"):
        parse_image([])


def test_get_all_parents() -> None:
    with open("tests/example.yml") as fp:
        example = load_config(fp)

    parent_names = [
        "operator integration tests",
        ".tests",
        ".only module",
        ".install dev dependencies",
    ]
    assert list(all_parents(example, "operator integration tests")) == parent_names


def test_extend() -> None:
    job = {
        "script": "echo 1",
        "after_script": "echo 2",
        "variables": {"FOO": "bar"},
    }
    extends = {
        "before_script": "echo 0",
        "variables": {"BAZ": "qux"},
        "after_script": "ignored",
    }
    merged = extend(job, extends)
    assert merged["script"] == "echo 1"
    assert merged["before_script"] == "echo 0"
    assert merged["after_script"] == "echo 2"
    assert merged["variables"] == {"FOO": "bar", "BAZ": "qux"}


def test_resolve_references_nested_lists() -> None:
    raw = {
        "first": "one",
        "last": "four",
        "list": [Reference(["first"]), "two", "three"],
        "flatten": [Reference(["list"]), Reference(["last"])],
        "nested": [[Reference(["list"])], [Reference(["last"])]],
    }
    resolved = resolve_references(raw, raw)
    assert resolved["list"] == ["one", "two", "three"]
    assert resolved["flatten"] == ["one", "two", "three", "four"]
    assert resolved["nested"] == [["one", "two", "three"], ["four"]]


def test_parse_references_variables() -> None:
    with open("tests/references.yml") as fp:
        config = parse_config(fp)

    vars_one = config.get_job("test-vars-1")
    assert vars_one.variables == {
        "URL": "http://my-url.internal",
        "IMPORTANT_VAR": "the details",
    }

    vars_two = config.get_job("test-vars-2")
    assert vars_two.variables == {"MY_VAR": "the details"}


def test_parse_references_scripts() -> None:
    with open("tests/references.yml") as fp:
        config = parse_config(fp)

    nested = config.get_job("nested-references")
    assert nested.script == ['echo "ONE!"', 'echo "TWO!"', 'echo "THREE!"']


def test_parse_single_cache() -> None:
    raw = {"image": "test", "cache": {"key": "$CI_COMMIT_REF_SLUG", "paths": [".npm/"]}}
    job = parse_job("test", raw)
    assert job.cache is not None and len(job.cache) == 1
    assert job.cache[0].key == "$CI_COMMIT_REF_SLUG"


def test_parse_single_cache_without_key() -> None:
    raw = {"image": "test", "cache": {"paths": [".npm/"]}}
    job = parse_job("test", raw)
    assert job.cache is not None and len(job.cache) == 1
    assert job.cache[0].key == "default"


def test_parse_single_cache_with_key_file() -> None:
    raw = {
        "image": "test",
        "cache": {"key": {"files": ["package-lock.json"]}, "paths": [".npm/"]},
    }
    job = parse_job("test", raw)
    assert job.cache is not None and len(job.cache) == 1
    assert job.cache[0].key_files == ["package-lock.json"]


def test_parse_multiple_caches() -> None:
    raw = {
        "image": "test",
        "cache": [
            {"key": {"files": ["Gemfile.lock"]}, "paths": ["vendor/ruby"]},
            {"key": {"files": ["yarn.lock"]}, "paths": [".yarn-cache/"]},
        ],
    }
    job = parse_job("test", raw)
    assert job.cache is not None and len(job.cache) == 2
    assert job.cache[0].key_files == ["Gemfile.lock"]
    assert job.cache[1].key_files == ["yarn.lock"]


def test_parse_cache_extends() -> None:
    with open("tests/extends.yml") as fp:
        config = parse_config(fp)

    one = config.get_job("one")
    assert one.cache is not None and len(one.cache) == 1
    assert one.cache[0].paths == ["*.txt"]
    assert one.cache[0].policy == "pull-push"

    two = config.get_job("two")
    assert two.cache is not None and len(two.cache) == 1
    assert two.cache[0].paths == ["*.txt"]
    assert two.cache[0].policy == "pull"


def test_parse_inherit_default() -> None:
    with open("tests/extends.yml") as fp:
        config = parse_config(fp)

    one = config.get_job("one")
    assert one.before_script == ["echo before"]
    assert one.after_script == ["echo after"]

    three = config.get_job("three")
    assert not three.before_script
    assert not three.after_script

    four = config.get_job("four")
    assert not four.before_script
    assert four.after_script


def test_parse_inherit_variables() -> None:
    with open("tests/extends.yml") as fp:
        config = parse_config(fp)

    one = config.get_job("one")
    assert one.variables == {"a": "1", "b": "2", "c": ""}

    five = config.get_job("five")
    assert five.variables == {}

    six = config.get_job("six")
    assert six.variables == {"a": "1", "c": "3"}
