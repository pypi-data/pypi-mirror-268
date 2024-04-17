import copy
import shlex
import typing
from collections import deque

import yaml

from .models import Cache, Config, Dict, Job, JobImage, Reference, Service

NOT_JOBS = {"workflow", "stages"}

T = typing.TypeVar("T")


def get_list(v: T | list[T] | None) -> list[T]:
    if v is None:
        return []
    if isinstance(v, list):
        return v
    return [v]


def get_list_or_none(v: T | list[T] | None) -> list[T] | None:
    if isinstance(v, list):
        return v
    return [v] if v is not None else None


def parse_command(raw: str | list[str] | None) -> list[str] | None:
    if raw is None:
        return None
    return shlex.split(raw) if isinstance(raw, str) else raw


def parse_service(raw: typing.Any) -> Service:
    if isinstance(raw, str):
        raw = {"name": raw}
    if isinstance(raw, dict):
        alias, _, _ = raw["name"].replace("/", "-").partition(":")
        return Service(
            name=raw["name"],
            alias=raw.get("alias") or alias,
            variables=raw.get("variables"),
            entrypoint=parse_command(raw.get("entrypoint")),
            command=parse_command(raw.get("command")),
        )
    raise ValueError(f"Unable to parse service, expected str or dict, got {raw!r}")


def parse_image(raw: typing.Any) -> JobImage:
    if isinstance(raw, str):
        return JobImage(name=raw)
    if isinstance(raw, dict):
        if "entrypoint" in raw:
            raw["entrypoint"] = get_list_or_none(raw["entrypoint"])
        return JobImage(**raw)
    raise ValueError(f"Unable to parse image, expected str or dict, got {raw!r}")


def parse_cache(raw: Dict) -> Cache:
    raw_key = raw.get("key") or "default"
    if isinstance(raw_key, str):
        key = raw_key
        key_files = None
        key_prefix = None
    else:
        key = None
        key_files = raw_key.get("files")
        assert isinstance(key_files, list)
        assert 1 <= len(key_files) <= 2
        key_prefix = raw_key.get("prefix")

    return Cache(
        key=key,
        key_files=key_files,
        key_prefix=key_prefix,
        paths=raw.get("paths"),
        untracked=raw.get("untracked", False),
        when=raw.get("when", "on_success"),
        policy=raw.get("policy", "pull-push"),
    )


def parse_job(name: str, raw: Dict) -> Job:
    image = parse_image(raw["image"])
    before_script: list[str] = get_list(raw.get("before_script"))
    script: list[str] = get_list(raw.get("script"))
    after_script: list[str] = get_list(raw.get("after_script"))
    variables = {k: str(v) for k, v in raw.get("variables", {}).items()}
    raw_services: list[typing.Any] = get_list(raw.get("services"))
    services = [parse_service(s) for s in raw_services]
    raw_cache: list[Dict] = get_list(raw.get("cache"))
    cache = [parse_cache(c) for c in raw_cache]
    return Job(
        name=name,
        image=image,
        before_script=before_script,
        script=script,
        after_script=after_script,
        variables=variables,
        services=services,
        cache=cache,
    )


def extend(a: Dict, b: Dict) -> Dict:
    """Extend `a` with values from `b`. Values in `a` will not be overwritten."""
    merged = copy.deepcopy(a)
    for key, value in b.items():
        if key not in a:
            merged[key] = value
        elif isinstance(a[key], dict) and isinstance(value, dict):
            merged[key] = extend(a[key], value)
    return merged


def all_parents(config: Dict, name: str) -> typing.Iterable[str]:
    """Get all parents of a job, including the job itself."""
    parents = deque([name])
    while parents:
        parent = parents.popleft()
        yield parent
        parents.extendleft(get_list(config[parent].get("extends")))


def merge_extends_and_defaults(
    name: str, config: Dict, default: Dict, globals: Dict, variables: dict[str, str]
) -> Dict:
    job: Dict = {"variables": {}}

    # Merge job with all extends
    for parent in all_parents(config, name):
        job = extend(job, config[parent])

    # Merge job with defaults, respecting `inherit:default`
    inherit = job.get("inherit", {})
    inherit_default = inherit.get("default", True)
    if isinstance(inherit_default, list):
        for key in inherit_default:
            if key in default and key not in job:
                job[key] = default[key]
    elif inherit_default:
        job = extend(job, default)

    # Merge job with variables, respecting `inherit:variables`
    inherit_variables = inherit.get("variables", True)
    if isinstance(inherit_variables, list):
        for key in inherit_variables:
            if key in variables and key not in job["variables"]:
                job["variables"][key] = variables[key]
    elif inherit_variables:
        job["variables"] = extend(job["variables"], variables)

    # Merge job with globals
    return extend(job, globals)


def resolve_references(root: Dict, value: typing.Any) -> typing.Any:
    if isinstance(value, Reference):
        resolved = root
        for key in value.path:
            resolved = resolved[key]
        return resolve_references(root, resolved)

    if isinstance(value, dict):
        return {k: resolve_references(root, v) for k, v in value.items()}

    if isinstance(value, list):
        new_value = []
        for item in value:
            # Flatten references that resolve to another list, but not nested lists
            resolved = resolve_references(root, item)
            if isinstance(item, Reference) and isinstance(resolved, list):
                new_value.extend(resolved)
            else:
                new_value.append(resolved)

        return new_value

    return value


class Loader(yaml.SafeLoader):
    def construct_reference(self, node: yaml.SequenceNode) -> Reference:
        return Reference(self.construct_sequence(node))


Loader.add_constructor("!reference", Loader.construct_reference)


def load_config(fp: typing.TextIO) -> Dict:
    raw = yaml.load(fp, Loader)
    assert isinstance(raw, dict)
    raw = resolve_references(raw, raw)
    assert isinstance(raw, dict)
    return raw


def parse_config(fp: typing.TextIO) -> Config:
    raw = load_config(fp)

    # Globally set defaults (deprecated, but widely used)
    globals = {
        key: raw.pop(key)
        for key in ("image", "services", "cache", "before_script", "after_script")
        if key in raw
    }

    default = raw.pop("default", {})

    # Global variables support some extra options, but we only need the values
    variables = {
        key: str(value.get("value", "")) if isinstance(value, dict) else str(value)
        for key, value in raw.pop("variables", {}).items()
    }

    return Config(
        globals=globals,
        default=default,
        variables=variables,
        jobs={
            key: value
            for key, value in raw.items()
            if isinstance(value, dict) and key not in NOT_JOBS
        },
    )
