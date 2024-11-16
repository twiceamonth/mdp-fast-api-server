from typing import List

from fastapi import APIRouter
from src.app.db.db_connection import session as db

from src.app.views.department.crud import get_departments, create_new_department, delete_department_by_id, \
    update_department_patch
from src.app.views.department.model import DepartmentResponse, Department

router = APIRouter(tags=["Отделы"])


@router.get("/departments", response_model=List[DepartmentResponse])
def get_departments_list() -> List[DepartmentResponse]:
    return get_departments(db)


@router.post("/department", response_model=DepartmentResponse)
def create_department(department: Department):
    return create_new_department(db, department)


@router.delete("/department/{department_id}")
def delete_department(department_id: str):
    return delete_department_by_id(db, department_id)


@router.patch("/department/{department_id}", response_model=DepartmentResponse)
def update_department(department_id: str, new_department: Department):
    return update_department_patch(db, department_id, new_department)
