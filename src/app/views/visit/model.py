from pydantic import BaseModel


class VisitResponse(BaseModel):
    visit_id: str
    employee_id: str
    event_id: str

class Visit(BaseModel):
    employee_id: str
    event_id: str