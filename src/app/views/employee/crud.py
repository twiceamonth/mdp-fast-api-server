import os
import uuid

from fastapi import HTTPException, UploadFile, File
from sqlalchemy import select, Result
from sqlalchemy.orm import Session, joinedload
from starlette import status

from src.app.views.employee.model import EmployeeCreate, EmployeePatch
from src.app.db.base import convert_to_db
from src.app.db.base import check_uuid
from src.app.db.models.employee import EmployeeDTO
from src.app.views.employee.model import EmployeeResponse, Employee


def get_employees(session: Session) -> list[EmployeeResponse]:
    q = (select(EmployeeDTO)
         .options(
        joinedload(EmployeeDTO.department),
                joinedload(EmployeeDTO.position))
         .order_by(EmployeeDTO.first_name))
    result: Result = session.execute(q)
    employees = result.scalars().all()
    return [EmployeeResponse.model_validate(emp) for emp in employees]

def get_employee(session: Session, employee_id: str) -> EmployeeResponse:
    check_uuid(employee_id)
    employee = session.get(EmployeeDTO, employee_id)
    if employee is not None:
        return employee
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Сотрудник с id {employee_id} не найден!",
    )

def create_new_employee(session: Session, new_employee: Employee, photo: UploadFile = File()) -> EmployeeResponse:
    ext = photo.filename.split(".")[-1]
    employee_new_id = uuid.uuid4()
    path = f"static_files/photos/{employee_new_id}.{ext}"
    response_path = f"photos-static/{employee_new_id}.{ext}"

    contents = photo.file.read()
    with open(path, "wb") as f:
        f.write(contents)
    photo.file.close()

    create_empl_sao = EmployeeCreate(
        employee_id = employee_new_id,
        first_name = new_employee.first_name,
        second_name = new_employee.second_name,
        patronymic = new_employee.patronymic,
        position_id = new_employee.position,
        department_id = new_employee.department,
        employee_photo = response_path
    )
    sao = convert_to_db(create_empl_sao, EmployeeDTO)
    session.add(sao)
    session.commit()
    session.refresh(sao)
    return sao

def delete(session: Session, employee_id: str):
    check_uuid(employee_id)
    employee = session.get(EmployeeDTO, employee_id)
    if employee is not None:
        session.delete(employee)
        session.commit()
        return { "message" : "Success" }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Сотрудник с id {employee_id} не найден!",
    )

def update_employee_patch(session: Session, employee_id: str, new_employee: EmployeePatch, photo: UploadFile = File()) -> EmployeeResponse:
    check_uuid(employee_id)
    old_employee = session.get(EmployeeDTO, employee_id)
    new_employee.model_dump(exclude_unset=True)

    if old_employee is not None:
        if photo is not None:
            ext = photo.filename.split(".")[-1]
            path = f"static_files/photos/{employee_id}.{ext}"
            response_path = f"photos-static/{employee_id}.{ext}"
            contents = photo.file.read()

            for file in os.listdir("static_files/photos"):
                filename = file.split(".")
                if (filename[0] == employee_id):
                    os.remove(f"static_files/photos/{filename[0]}.{filename[1]}")
            with open(path, "wb") as f:
                f.write(contents)
            photo.file.close()

            for name, value in new_employee.model_dump(exclude_unset=True).items():
                setattr(old_employee, name, value)
            setattr(old_employee, "employee_photo", response_path)
            session.commit()
            return old_employee
        else:
            for name, value in new_employee.model_dump(exclude_unset=True).items():
                setattr(old_employee, name, value)
            session.commit()
            return old_employee
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Сотрудник с id {employee_id} не найден!",
    )