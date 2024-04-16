from pydantic import BaseModel


class AnalyseLogsSchema(BaseModel):
    logs: str
    event_type: str = "gitoptim-analyse-logs"
