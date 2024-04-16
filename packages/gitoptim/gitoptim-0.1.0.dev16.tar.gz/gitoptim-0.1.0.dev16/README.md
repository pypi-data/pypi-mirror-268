# Gitoptim SDK

## Introduction

Gitoptim SDK is a CLI tool that enables integration of Gitlab pipelines and Workflows. It is designed to be used in
CI/CD jobs.

## Features

- #### Gitlab CI/CD logs analysis

- #### Memlab integration

## Development

### Prerequisites

- Python 3.11 or later
- [Poetry](https://python-poetry.org/) for dependency management

### Setup

1. Install dependencies using `poetry install --with dev`
2. Install git hooks using `pre-commit install`. This will run linters and formatters before each push to repository.

#### Environment variables

The following environment variables are required in order to run the CLI:

```
CI_PROJECT_ID
CI_JOB_ID
CI_API_V4_URL
GITOPTIM_PRIVATE_TOKEN - Gitlab personal or project access token with `api-read` scope and `Guest` role
```

Variables prefixed with `CI_` are provided by Gitlab CI/CD.
See: [docs](https://docs.gitlab.com/ee/ci/variables/predefined_variables.html)

#### Pycharm

1. Set the Python interpreter to the one created by Poetry. This can be done by going
   to `File -> Settings -> Project-> Python Interpreter` and selecting the interpreter created by Poetry. Path to the
   interpreter can be found by running `poetry env info` in the terminal.
2. Install Pylint plugin for Pycharm.
3. Enable "Reformat code" on save. This can be done by going to `File -> Settings -> Tools ->
   Actions On Save`.

### How to run

1. Run `poetry shell` to activate the virtual environment.
2. Run `python -m gitoptim` to start the CLI.

**Important**: In order to push to repository you need to have poetry shell enabled so that git hooks can run.
