from pydantic import BaseModel


class InvitationResponse(BaseModel):
    event_id: str
    employee_id: str