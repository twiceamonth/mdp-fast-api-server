from typing import List

from fastapi import UploadFile, File
from pydantic import BaseModel
from datetime import date, time

class Event(BaseModel):
    event_name: str
    event_date: date
    start_time: time
    end_time: time
    description: str

class EventResponse(BaseModel):
    event_id: str
    event_name: str
    event_date: date
    start_time: time
    end_time: time
    description: str

class PositionResponse(BaseModel):
    position_id: str
    name: str

class Position(BaseModel):
    name: str

class DepartmentResponse(BaseModel):
    department_id: str
    name: str

class Department(BaseModel):
    name: str

class EmployeeResponse(BaseModel):
    employee_id: str
    first_name: str
    second_name: str
    patronymic: str | None = None
    position: PositionResponse
    department: DepartmentResponse

class Employee(BaseModel):
    first_name: str
    second_name: str
    patronymic: str | None = None
    position: str
    department: str

class BiometricsResponse(BaseModel):
    biometrics_id: str
    upload_date: date
    photo_path: str
    employee_id: str

class InvitationResponse(BaseModel):
    event_id: str
    employee_id: str

class VisitResponse(BaseModel):
    visit_id: str
    employee_id: str
    event_id: str

class Visit(BaseModel):
    employee_id: str
    event_id: str

class VisitMarkResponse(BaseModel):
    mark_id: str
    fixation_time: time
    photo_path: str
    visit_id: str