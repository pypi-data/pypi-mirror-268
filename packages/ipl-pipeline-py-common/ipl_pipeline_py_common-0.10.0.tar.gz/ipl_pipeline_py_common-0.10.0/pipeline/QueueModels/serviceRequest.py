from pydantic import BaseModel, Field


class ServiceRequest(BaseModel):
    request_node_id: str = Field("unknown")
    request_node_version: str = Field("unknown")
