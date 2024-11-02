from fastapi import APIRouter, Body
from pydantic import BaseModel

router = APIRouter(tags=["Сотрудники"])

@router.get("/employees")
def get_employees_list():
    return []

@router.get("/employees/{employee_id}")
def get_employee_by_id(employee_id: str):
    return []

@router.post("/employee")
def create_employee(employee: BaseModel = Body()):
    return {}

@router.delete("/employee/{employee_id}")
def delete_employees(employee_id: str):
    return []

@router.put("/employee/{employee_id}")
def update_event(employee_id: str, new_employee: BaseModel = Body()):
    return {}