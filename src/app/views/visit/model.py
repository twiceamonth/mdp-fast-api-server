from uuid import UUID

from pydantic import BaseModel, ConfigDict


class VisitResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    visit_id: UUID
    employee_id: UUID
    event_id: UUID

class Visit(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    employee_id: UUID
    event_id: UUID