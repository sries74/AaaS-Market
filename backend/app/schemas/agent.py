import uuid

from pydantic import BaseModel


class AgentResponse(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    description: str
    category: str
    credit_cost: int
    is_active: bool

    model_config = {"from_attributes": True}


class AgentRunRequest(BaseModel):
    agent_id: uuid.UUID
    input_data: dict


class AgentRunResponse(BaseModel):
    id: uuid.UUID
    agent_id: uuid.UUID
    user_id: uuid.UUID
    status: str
    input_data: str
    output_data: str | None
    error_message: str | None
    created_at: str
    completed_at: str | None

    model_config = {"from_attributes": True}
