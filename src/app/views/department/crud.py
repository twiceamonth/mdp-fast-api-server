from fastapi import HTTPException
from sqlalchemy import select, Result
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND

from src.app.db.base import check_uuid, convert_to_db
from src.app.db.models.department import DepartmentDTO
from src.app.views.department.model import DepartmentResponse, Department


def get_departments(session: Session) -> list[DepartmentResponse]:
    q = select(DepartmentDTO).order_by(DepartmentDTO.name)
    result: Result = session.execute(q)
    departments = result.scalars().all()
    return [DepartmentResponse.model_validate(department) for department in departments]

def create_new_department(session: Session, new_department: Department) -> DepartmentResponse:
    sao = convert_to_db(new_department, DepartmentDTO)
    session.add(sao)
    session.commit()
    session.refresh(sao)
    return sao

def delete_department_by_id(session: Session, department_id: str):
    check_uuid(department_id)
    department = session.get(DepartmentDTO, department_id)
    if department is not None:
        session.delete(department)
        session.commit()
        return { "message" : "Success" }
    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"Отдел с id {department_id} не найдена!",
    )

def update_department_patch(session: Session, department_id: str, new_department: Department) -> DepartmentResponse:
    check_uuid(department_id)
    new_department.model_dump(exclude_unset=True)
    old_department = session.get(DepartmentDTO, department_id)
    if old_department is not None:
        for name, value in new_department.model_dump(exclude_unset=True).items():
            setattr(old_department, name, value)
        session.commit()
        return old_department
    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"Отдел с id {department_id} не найдена!",
    )