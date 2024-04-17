import logging
import re
import typing
from urllib.parse import urlparse

from .models import Job
from .subprocess import get_command_output

logger = logging.getLogger(__name__)

# https://docs.gitlab.com/ee/ci/variables/predefined_variables.html
constants = {
    "CI": "true",
    "CI_SERVER": "yes",
    "GITLAB_CI": "true",
    "CI_BUILDS_DIR": "/builds",
    "CI_CONCURRENT_ID": "0",
    "CI_DEFAULT_BRANCH": "main",
    "CI_NODE_INDEX": "0",
    "CI_NODE_TOTAL": "1",
    "CI_PROJECT_DIR": "/src",
}


def slugify(s: str) -> str:
    """Return a slug of the given string.

    Slugs are lowercase, no longer than 63 characters, with everything
    except 0-9 and a-z replaced with -. No leading / trailing -.
    """
    return re.sub(r"[^a-z0-9]+", "-", s.lower())[:63].strip("-")


def get_commit_variables(source_dir: str) -> dict[str, str]:
    """Return variables related to the current commit."""
    placeholders = {
        "%an <%ae>": "CI_COMMIT_AUTHOR",
        "%P": "CI_COMMIT_BEFORE_SHA",
        "%b": "CI_COMMIT_DESCRIPTION",
        "%B": "CI_COMMIT_MESSAGE",
        "%H": "CI_COMMIT_SHA",
        "%ci": "CI_COMMIT_TIMESTAMP",
        "%s": "CI_COMMIT_TITLE",
    }

    separator = "\n--\n"
    pretty_format = separator.replace("\n", "%n").join(placeholders.keys())
    git_log = get_command_output(
        ["git", "log", f"--pretty=format:{pretty_format}", "-1"],
        cwd=source_dir or None,
    )

    variables = {
        variable: value.rstrip()
        for variable, value in zip(placeholders.values(), git_log.split(separator))
    }

    # Git has '%h' for abbreviated commit hash, but it uses 7 characters
    # by default; GitLab always uses 8.
    variables["CI_COMMIT_SHORT_SHA"] = variables["CI_COMMIT_SHA"][:8]

    ref_name = get_command_output(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=source_dir or None,
    )

    variables["CI_COMMIT_REF_NAME"] = ref_name
    variables["CI_COMMIT_REF_SLUG"] = slugify(ref_name)

    # TODO: This is only correct when HEAD is a branch.
    variables["CI_COMMIT_BRANCH"] = ref_name

    return variables


def get_job_variables(job: Job) -> dict[str, str]:
    """Return variables related to the given job."""
    return {
        "CI_JOB_ID": "42",
        "CI_JOB_NAME": job.name,
        "CI_JOB_NAME_SLUG": slugify(job.name),
        "CI_JOB_IMAGE": job.image.name,
    }


def get_project_variables(source_dir: str) -> dict[str, str]:
    """Return variables related to the current project."""

    git_remote_url = get_command_output(
        ["git", "remote", "get-url", "origin"],
        cwd=source_dir or None,
    )

    if "://" not in git_remote_url and ":" in git_remote_url:
        # Rewrite scp-style remote, so it can be parsed as a URL
        url = urlparse("ssh://" + git_remote_url.replace(":", "/", 1))
    else:
        url = urlparse(git_remote_url)

    project_path = url.path.strip("/").removesuffix(".git")
    namespace, _, project = project_path.rpartition("/")
    root_namespace, _, _ = namespace.partition("/")

    return {
        "CI_PROJECT_NAME": project,
        "CI_PROJECT_NAMESPACE": namespace,
        "CI_PROJECT_PATH": project_path,
        "CI_PROJECT_PATH_SLUG": slugify(project_path),
        "CI_PROJECT_ROOT_NAMESPACE": root_namespace,
        "CI_PROJECT_URL": f"https://{url.hostname}/{project_path}",
        "CI_REGISTRY": f"registry.{url.hostname}",
        "CI_REGISTRY_IMAGE": f"registry.{url.hostname}/{project_path}",
        "CI_REPOSITORY_URL": git_remote_url,
    }


variable = re.compile(r"\$(?:\{([^}]+)}|([a-zA-Z0-9_]+))")


class Variables:
    def __init__(self, variables: dict[str, str]):
        self.variables = variables
        self.undefined: set[str] = set()

    def __add__(self, other: typing.Any) -> "Variables":
        if other is None:
            other = {}
        elif isinstance(other, Variables):
            other = other.variables
        elif not isinstance(other, dict):
            return NotImplemented
        return Variables({**self.variables, **other})

    def lookup(self, match: re.Match[str]) -> str:
        key = match.group(1) or match.group(2)
        if key in self.variables:
            return self.variables[key]
        if key not in self.undefined:
            self.undefined.add(key)
            logger.warning(f"Undefined variable {key!r}")
        return match.group(0)

    def replace(self, s: str) -> str:
        return variable.sub(self.lookup, s)

    def replace_list(self, items: list[str] | None) -> list[str] | None:
        return None if items is None else [self.replace(item) for item in items]

    def as_dict(self) -> dict[str, str]:
        return {k: self.replace(v) for k, v in self.variables.items()}


def get_all_variables(job: Job, source_dir: str) -> Variables:
    """Return a dictionary of all predefined variables for the given job."""

    values = {
        **constants,
        **get_job_variables(job),
        **get_commit_variables(source_dir),
        **get_project_variables(source_dir),
        **job.variables,
    }
    return Variables(values)
