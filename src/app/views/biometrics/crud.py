import os
import uuid
from random import Random
from typing import List
from uuid import UUID

from fastapi import UploadFile, File, HTTPException
from sqlalchemy import select, Result
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND

from app.db.base import check_uuid, convert_to_db
from app.db.models.biometrics import BiometricsDTO
from app.views.biometrics.model import BiometricsResponse, Biometrics


def get_biometrics_by_employee_id(session: Session, employee_id: str) -> list[BiometricsResponse]:
    q = select(BiometricsDTO).where(BiometricsDTO.employee_id == employee_id).order_by(BiometricsDTO.upload_date)
    result: Result = session.execute(q)
    biometrics = result.scalars().all()
    return [BiometricsResponse.model_validate(b) for b in biometrics]

def upload_biometrics_by_employee_id(session: Session, employee_id: str, files: List[UploadFile] = File()) -> List[BiometricsResponse]:
    check_uuid(employee_id)
    for file in files:
        ext = file.filename.split(".")[-1]
        file_new_uuid = uuid.uuid4()
        path = f"static_files/biometrics/{file_new_uuid}.{ext}"
        response_path = f"biometrics-static/{file_new_uuid}.{ext}"
        contents = file.file.read()
        with open(path, "wb") as f:
            f.write(contents)
        file.close()
        sao = convert_to_db(Biometrics(photo_id=file_new_uuid, photo_path=response_path, employee_id=employee_id), BiometricsDTO)
        session.add(sao)
        session.commit()
        session.refresh(sao)
    return get_biometrics_by_employee_id(session, employee_id)


def delete_biometrics_by_id(session: Session, photo_id: str):
    check_uuid(photo_id)
    for file in os.listdir("static_files/biometrics"):
        file_name = file.split(".")
        if(file_name[0] == photo_id):
            os.remove(f"static_files/biometrics/{file_name[0]}.{file_name[1]}")
            bio = session.get(BiometricsDTO, photo_id)
            session.delete(bio)
            session.commit()
            return { "message" : "Success" }
    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"Файл биометрии с id {photo_id} не найден!",
    )