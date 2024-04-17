# Trycicle

Try CI jobs locally, including services.

## Installation

    pipx install trycicle

### Tab completion

Trycicle supports tab completion for Bash, Zsh and Fish.

<details>
<summary>Bash</summary>

Add this to your `~/.bashrc`:

```shell
eval "$(_TRYCICLE_COMPLETE=bash_source trycicle)"
```
</details>

<details>
<summary>Zsh</summary>

Add this to your `~/.zshrc`:

```shell
eval "$(_TRYCICLE_COMPLETE=zsh_source trycicle)"
```
</details>

<details>
<summary>Fish</summary>

Save the completion script to your completions directory:

```shell
_TRYCICLE_COMPLETE=fish_source trycicle > ~/.config/fish/completions/trycicle.fish
```
</details>

## Usage

Trycicle is a command line tool that allows you to run CI jobs locally.
It expects the name of the CI job to run as the first argument.
It will look for a `.gitlab-ci.yml` file in the current directory, unless the `--file` option is used to specify a different file.
It assumes the directory containing the `.gitlab-ci.yml` is the source directory, this can be overridden with the `--workdir` option.

## Examples

### Basic usage

Given the following `.gitlab-ci.yml` file:

```yaml
image: busybox:latest

variables:
  NAME: world

test:
  script:
    - echo "Hello, $NAME!"
```

You can run the `test` job with `trycicle test`:

```console
$ trycicle test
INFO:trycicle.run:Starting job (busybox:latest)
...
Hello, world!
```

Trycicle will tell you which jobs (and services) it runs.
Script commands are also echoed.
To get more detailed output, use `--verbose`.

### Variables

Trycicle defines many of the commonly used GitLab CI predefined variables.
If it notices your job depends on a variable that is not set, it will print a warning:

```yaml
image: busybox:latest

test:
  script:
    - echo "CI_JOB_NAME=$CI_JOB_NAME"
    - echo "GREETING=$GREETING"
    - echo "MISSING=$MISSING"
  variables:
    GREETING: "Hello, $USER!"
```

```console
$ trycicle test
INFO:trycicle.run:Starting job (busybox:latest)
WARNING:trycicle.variables:Undefined variable 'USER'
...
CI_JOB_NAME=test
...
GREETING=Hello, $USER!
...
MISSING=
```

As you can see, Trycicle can not detect all cases where a variable is missing.
This is most noticeable when undefined variables are used in scripts, where the shell will expand them to an empty string.
(To help with this, you can use `set -u` in your scripts to make the shell fail when an undefined variable is used. Of course, this works on actual GitLab CI as well.)

To pass an extra variable to the job, use the `--env` (or `-e`) option:

```console
$ trycicle test --env USER=Trycicle --env MISSING=found
...
GREETING=Hello, Trycicle!
...
MISSING=found
```

When a variable is defined in your local environment, use `--env` with just the name to pass it to the job:

```console
$ trycicle test --env USER
...
GREETING=Hello, paul!
```

### Services

Trycicle can run services for your job:

```yaml
test:
  image: busybox:latest
  services:
    - nginx:latest
  script:
    - wget -qO- http://nginx/
```

```console
$ trycicle test
INFO:trycicle.run:Starting service nginx (nginx:latest)
INFO:trycicle.run:Starting job (busybox:latest)
...
<h1>Welcome to nginx!</h1>
```

If a service container exits while the job is still running, Trycicle will print a warning:

```yaml
test:
  image: busybox:latest
  services:
    - name: busybox:latest
      command: [sh, -c, "sleep 1; exit 1"]
  script:
    - sleep 2
    - echo "Done"
```

```console
$ trycicle test
INFO:trycicle.run:Starting service busybox (busybox:latest)
INFO:trycicle.run:Starting job (busybox:latest)
...
WARNING:trycicle.run:Service busybox died with exit code 1
...
Done
```

To display the logs of the service containers, use `--service-logs`. Each line of output is prefixed with the name of the service, or `job`:

```yaml
test:
  image: busybox:latest
  services:
    - name: postgres:latest
      command: postgres -c log_line_prefix=
  variables:
    POSTGRES_PASSWORD: postgres
  script:
    - while ! nc -z postgres 5432; do sleep 1; done
    - echo "Done"
```

```console
$ trycicle test --service-logs
INFO:trycicle.run:Starting service postgres (postgres:latest)
INFO:trycicle.run:Starting job (busybox:latest)
...
postgres | running bootstrap script ... ok
...
postgres | LOG:  database system is ready to accept connections
...
job | Done
```

### Docker-in-Docker

Trycicle tries to detect when your job is using Docker-in-Docker and will run with the `--privileged` option.
It will also use a volume to share the Docker certificates between job and service.

```yaml
test:
  image: python:3.11
  services:
    - docker:20-dind
  variables:
    DOCKER_HOST: tcp://docker:2376
    DOCKER_TLS_CERTDIR: /certs
    DOCKER_TLS_VERIFY: 1
    DOCKER_CERT_PATH: "${DOCKER_TLS_CERTDIR}/client"
  script:
    - pip install docker~=7.0.0
    - |
      python -c 'import docker
      client = docker.from_env()
      output = client.containers.run("busybox:latest", ["echo", "Hello", "DinD!"], remove=True)
      print(output.decode())
      '
```

```console
$ trycicle test
INFO:trycicle.run:Starting service docker (docker:20-dind)
INFO:trycicle.run:Starting job (python:3.11)
...
Hello DinD!
```

### Clean copy

By default, Trycicle runs the job directly in your source directory.
This way you can edit files and run the job again without having to commit and push.
This also means that the job has access to files that would not normally be committed, like `node_modules/` or a `.env` file with settings specific to your local environment.

It also means that the job can create or modify files in your source directory.
This is great to inspect the output of the job, but it can also lead to unexpected changes in your source directory.

To avoid this, Trycicle can use Git to create a clean copy of your source directory and run the job there.
Any changes not committed will not be visible to the job.
Your changes *do not* need to be pushed.
Changes to the `.gitlab-ci.yml` *are* used.

```yaml
test:
  image: buildpack-deps:stable-scm
  script:
    - git remote -v
    - cat hello.txt
    - git status
```

```console
$ git init .
$ echo 'Hello, world!' > hello.txt
$ git add hello.txt
$ git commit -m 'Initial commit'
$ echo 'Another file' > untracked.txt
$ echo 'An uncommitted edit' >> hello.txt
$ trycicle test --clean
...
+ git remote -v
origin	/repo (fetch)
origin	/repo (push)
+ cat hello.txt
Hello, world!
+ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

As you can see, only the committed changes are visible to the job.
Trycicle adds your source directory as a remote to the clean copy, this makes it possible to use `git fetch` in the job.
Pushing does not work, your working directory is mounted read-only.

### Caching

Trycicle has rudimentary support for caching. If a job defines a `cache` key, Trycicle will keep matching files between runs.

```yaml
image: busybox:latest

cache:
  key: example
  paths:
    - "*.txt"

one:
  script:
    - echo 'Hello, world!' > hello.txt

two:
  script:
    - cat hello.txt
```

Running the first job will create a cache with the `hello.txt` file:

```console
$ trycicle one
INFO:trycicle.cache:Using cache 'cache-readme-example'
...
```

The second job will be able to read the file from the cache:

```console
$ trycicle two
INFO:trycicle.cache:Using cache 'cache-readme-example'
...
Hello, world!
```

## Debugging

### Logs

Trycicle does not immediately remove the containers it creates, so you can inspect them after the job has finished.
The containers are labeled with the job they were part of, so you can use a command like `docker ps -a --filter label=trycicle.job=test` to list them.
This can also be combined with `docker logs`, for example to get the logs of `postgresql` service in the most recent run:

```shell
docker logs $(docker ps -q --latest --filter label=trycicle.service=postgres)
```

The labels Trycicle uses are:

| Label              | Value                              | Notes                                                                                             |
|--------------------|------------------------------------|---------------------------------------------------------------------------------------------------|
| `trycicle`         | Always `true`                      | Can be used to list all containers created by Trycicle: `docker ps --all --filter label=trycicle` |
| `trycicle.job`     | Name of the job                    |                                                                                                   |
| `trycicle.service` | Name of the service                | Only set for services                                                                             |
| `trycicle.workdir` | Full path to the working directory | Usually the directory containing the `.gitlab-ci.yml`                                             |

### Interactive debugging

Trycicle can run a job in interactive mode, which means you can execute commands in the container after the job has finished.
This is useful to inspect the state of the container, check environment variables, or find out what that missing package is called.

The debug shell will start automatically when the job fails, you can also add a `debugger` command to the script to start it manually.
To enter the debug shell before the job starts, use the `--debug=immediate` option.
