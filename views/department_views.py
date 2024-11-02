from fastapi import APIRouter, Body
from pydantic import BaseModel

router = APIRouter(tags=["Отделы"])

@router.get("/departments")
def get_departments_list():
    return []

@router.post("/department")
def create_department(department: BaseModel = Body()):
    return {}

@router.delete("/department/{department_id}")
def delete_department(department_id: str):
    return []

@router.put("/department/{department_id}")
def update_department(department_id: str, new_department: BaseModel = Body()):
    return {}