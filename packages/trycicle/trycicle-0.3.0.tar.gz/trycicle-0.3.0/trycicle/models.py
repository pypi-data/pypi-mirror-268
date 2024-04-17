import dataclasses
import typing

Dict: typing.TypeAlias = dict[str, typing.Any]


@dataclasses.dataclass
class Reference:
    path: list[str]


@dataclasses.dataclass
class Service:
    name: str
    alias: str
    variables: dict[str, str] | None = None
    entrypoint: list[str] | None = None
    command: list[str] | None = None

    @property
    def is_docker_dind(self) -> bool:
        return self.name.startswith("docker:") and "dind" in self.name


@dataclasses.dataclass
class JobImage:
    name: str
    entrypoint: list[str] | None = None


@dataclasses.dataclass
class Cache:
    key: str | None = None
    key_files: list[str] | None = None
    key_prefix: str | None = None
    paths: list[str] | None = None  # Array of globs relative to CI_PROJECT_DIR
    untracked: bool = False
    when: typing.Literal["on_success", "on_failure", "always"] = "on_success"
    policy: typing.Literal["pull", "push", "pull-push"] = "pull-push"


@dataclasses.dataclass
class Job:
    name: str
    image: JobImage
    before_script: list[str] = dataclasses.field(default_factory=list)
    script: list[str] = dataclasses.field(default_factory=list)
    after_script: list[str] = dataclasses.field(default_factory=list)
    variables: dict[str, str] = dataclasses.field(default_factory=dict)
    services: list[Service] = dataclasses.field(default_factory=list)
    cache: list[Cache] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class Config:
    globals: Dict
    default: Dict
    variables: dict[str, str]
    jobs: Dict

    def get_job(self, name: str) -> Job:
        from .parser import merge_extends_and_defaults, parse_job

        job = merge_extends_and_defaults(
            name, self.jobs, self.default, self.globals, self.variables
        )
        return parse_job(name, job)

    def all_variable_names(self) -> set[str]:
        return set(self.variables.keys()) | {
            name for job in self.jobs.values() for name in job.get("variables", {})
        }
