from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DepartmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    department_id: UUID
    name: str

class Department(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str