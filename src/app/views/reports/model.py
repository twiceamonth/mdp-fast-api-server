from datetime import time

from pydantic import BaseModel, ConfigDict

from src.app.views.employee.model import EmployeeResponse


class EventReportResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    event_name: str
    start_time: time
    end_time: time
    visitor_count: int

class EventProgrammeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    event_name: str
    start_time: time
    end_time: time
    description: str
    participants: list[EmployeeResponse]

class EventAbsentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    absent_list: list[EmployeeResponse]

class EventDashboardResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    time: str
    visitor_count: int