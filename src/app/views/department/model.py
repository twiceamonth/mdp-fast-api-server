from pydantic import BaseModel


class DepartmentResponse(BaseModel):
    department_id: str
    name: str

class Department(BaseModel):
    name: str