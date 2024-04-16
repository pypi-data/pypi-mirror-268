import os
from typing import Optional, Self, Type

import typer

from gitoptim.utils.cli import error_console


class EnvironmentVariables:
    _INSTANCE: Self = None
    _project_id: Optional[str] = None
    _job_id: Optional[str] = None
    _private_token: Optional[str] = None
    _gitlab_api_url: Optional[str] = None
    _gitlab_server_url: Optional[str] = None
    _workflows_trigger_url: Optional[str] = None
    _workflows_trigger_secret: Optional[str] = None

    def __new__(cls):
        if cls._INSTANCE is None:
            cls._INSTANCE = super().__new__(cls)
        return cls._INSTANCE

    def _load_variable(self, name: str, cast_type: Type = str):
        if hasattr(self, name) and getattr(self, name) is not None:
            return getattr(self, name)

        value = os.environ.get(name)
        if value is None:
            error_console.print(f"Environment variable {name} not found")
            raise typer.Exit(code=1)
        return cast_type(value)

    @property
    def project_id(self) -> str:
        self._project_id = self._load_variable("CI_PROJECT_ID")
        return self._project_id

    @property
    def job_id(self) -> str:
        self._job_id = self._load_variable("CI_JOB_ID")
        return self._job_id

    @property
    def private_token(self) -> str:
        self._private_token = self._load_variable("GITOPTIM_PRIVATE_TOKEN")
        return self._private_token

    @property
    def gitlab_api_url(self) -> str:
        self._gitlab_api_url = self._load_variable("CI_API_V4_URL")
        return self._gitlab_api_url

    @property
    def gitlab_server_url(self) -> str:
        self._gitlab_server_url = self._load_variable("CI_SERVER_URL")
        return self._gitlab_server_url

    @property
    def workflows_trigger_url(self) -> str:
        self._workflows_trigger_url = self._load_variable("GITOPTIM_TRIGGER_URL")
        return self._workflows_trigger_url

    @property
    def workflows_trigger_secret(self) -> str:
        self._workflows_trigger_secret = self._load_variable("GITOPTIM_TRIGGER_SECRET")
        return self._workflows_trigger_secret
