from pydantic import BaseModel


from src.app.views.department.model import DepartmentResponse
from src.app.views.position.model import PositionResponse


class EmployeeResponse(BaseModel):
    employee_id: str
    first_name: str
    second_name: str
    patronymic: str | None = None
    position: PositionResponse
    department: DepartmentResponse
    employee_photo: str

class Employee(BaseModel):
    first_name: str
    second_name: str
    patronymic: str | None = None
    position: str
    department: str