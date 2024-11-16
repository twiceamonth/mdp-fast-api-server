from typing import List

from fastapi import APIRouter, UploadFile, File
from src.app.db.db_connection import session as db

from src.app.views.biometrics.crud import get_biometrics_by_employee_id, upload_biometrics_by_employee_id, \
    delete_biometrics_by_id
from src.app.views.biometrics.model import BiometricsResponse

router = APIRouter(tags=["Биометрия"])

@router.get("/biometrics", response_model=List[BiometricsResponse])
def get_biometrics_list_for_employee(employee_id: str) -> List[BiometricsResponse]:
    return get_biometrics_by_employee_id(db, employee_id)

@router.post("/biometrics", response_model=List[BiometricsResponse])
def upload_biometrics(employee_id: str, files: List[UploadFile] = File()):
    return upload_biometrics_by_employee_id(db, employee_id, files)

@router.delete("/biometrics/{biometrics_id}")
def delete_biometrics_item(biometrics_id: str):
    return delete_biometrics_by_id(db, biometrics_id)
