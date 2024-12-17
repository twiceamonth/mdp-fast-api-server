from uuid import UUID

from pydantic import BaseModel, ConfigDict


class InvitationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    event_id: UUID
    employee_id: UUID