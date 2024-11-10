from typing import List

from fastapi import APIRouter

from model import DepartmentResponse, Department

router = APIRouter(tags=["Отделы"])


@router.get("/departments")
def get_departments_list() -> List[DepartmentResponse]:
    return []


@router.post("/department")
def create_department(department: Department):
    return {}


@router.delete("/department/{department_id}")
def delete_department(department_id: str):
    return []


@router.patch("/department/{department_id}")
def update_department(department_id: str, new_department: Department):
    return {}
