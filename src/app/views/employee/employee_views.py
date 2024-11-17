import json
from typing import List

from fastapi import APIRouter, UploadFile, File, Form

from src.app.views.employee.crud import update_employee_patch
from src.app.views.employee.model import EmployeePatch
from src.app.views.employee.crud import delete
from src.app.views.employee.crud import create_new_employee
from src.app.views.employee.crud import get_employees
from src.app.views.employee.crud import get_employee
from src.app.db.db_connection import session as db

from src.app.views.employee.model import EmployeeResponse, Employee

router = APIRouter(tags=["Сотрудники"])

@router.get("/employees", response_model=list[EmployeeResponse])
def get_employees_list() -> List[EmployeeResponse]:
    return get_employees(db)

@router.get("/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee_by_id(employee_id: str) -> EmployeeResponse:
    return get_employee(db, employee_id)

@router.post("/employee", response_model=EmployeeResponse)
def create_employee(employee: str = Form(media_type = "application/json"), photo: UploadFile = File()) -> EmployeeResponse:
    employee_data = json.loads(employee)
    employee_model = Employee(**employee_data)
    return create_new_employee(db, employee_model, photo)

@router.delete("/employee/{employee_id}")
def delete_employee(employee_id: str):
    return delete(db, employee_id)

@router.patch("/employee/{employee_id}", response_model=EmployeeResponse)
def update_employee(employee_id: str, new_employee: str = Form(media_type = "application/json"), photo: UploadFile| None = None ) -> EmployeeResponse:
    employee_data = json.loads(new_employee)
    employee_model = EmployeePatch(**employee_data)
    return update_employee_patch(db, employee_id, employee_model, photo)