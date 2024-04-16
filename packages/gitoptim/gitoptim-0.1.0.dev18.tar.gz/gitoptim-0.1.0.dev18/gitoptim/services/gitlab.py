import re

import httpx

from gitoptim.utils.environment import EnvironmentVariables


class GitlabAPI:
    _api_url: str
    _private_token: str
    _job_id: str
    _project_id: str

    def __init__(self):
        self._api_url = EnvironmentVariables().gitlab_api_url
        self._private_token = EnvironmentVariables().private_token
        self._job_id = EnvironmentVariables().job_id
        self._project_id = EnvironmentVariables().project_id

    def _get_headers(self):
        return {
            "PRIVATE-TOKEN": self._private_token
        }

    def get(self, path: str, **kwargs):
        return httpx.get(f"{self._api_url}/{path}", headers=self._get_headers(), **kwargs).raise_for_status()

    def get_job_logs(self):
        return self._escape_ansi(
            self.get(f"projects/{self._project_id}/jobs/{self._job_id}/trace").content.decode("utf-8", "ignore"))

    def _escape_ansi(self, text: str):
        ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
        return ansi_escape.sub('', text)
