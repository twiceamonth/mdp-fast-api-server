from uuid import UUID

from pydantic import BaseModel, ConfigDict

from src.app.views.department.model import DepartmentResponse
from src.app.views.position.model import PositionResponse


class EmployeeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    employee_id: UUID
    first_name: str
    second_name: str
    patronymic: str | None = None
    position: PositionResponse
    department: DepartmentResponse
    employee_photo: str

class Employee(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    first_name: str
    second_name: str
    patronymic: str | None = None
    position: UUID
    department: UUID

class EmployeePatch(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    first_name: str | None = None
    second_name: str | None = None
    patronymic: str | None = None
    position_id: UUID | None = None
    department_id: UUID | None = None

class EmployeeCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    employee_id: UUID
    first_name: str
    second_name: str
    patronymic: str | None = None
    position_id: UUID
    department_id: UUID
    employee_photo: str