import httpx

from gitoptim.schemas.workflows import AnalyseLogsSchema
from gitoptim.utils.environment import EnvironmentVariables


class WorkflowService:
    _trigger_url: str
    _trigger_secret: str

    def __init__(self):
        self._trigger_url = EnvironmentVariables().workflows_trigger_url
        self._trigger_secret = EnvironmentVariables().workflows_trigger_secret

    def _get_headers(self):
        return {
            "X-GITOPTIM-KEY": self._trigger_secret
        }

    def trigger_log_analysis(self, payload: AnalyseLogsSchema):
        return httpx.post(self._trigger_url, headers=self._get_headers(), json=payload).raise_for_status()


workflow_service = WorkflowService()
