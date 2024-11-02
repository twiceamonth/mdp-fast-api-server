from typing import List

from fastapi import APIRouter

from models import Employee, EmployeeResponse

router = APIRouter(tags=["Сотрудники"])

@router.get("/employees")
def get_employees_list() -> List[EmployeeResponse]:
    return []

@router.get("/employees/{employee_id}")
def get_employee_by_id(employee_id: str) -> EmployeeResponse:
    return {}

@router.post("/employee")
def create_employee(employee: Employee):
    return {}

@router.delete("/employee/{employee_id}")
def delete_employee(employee_id: str):
    return {}

@router.patch("/employee/{employee_id}")
def update_employee(employee_id: str, new_employee: Employee):
    return {}