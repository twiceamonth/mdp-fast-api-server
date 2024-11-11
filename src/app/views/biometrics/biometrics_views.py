from typing import List

from fastapi import APIRouter, UploadFile, File

from src.app.views.biometrics.model import BiometricsResponse

router = APIRouter(tags=["Биометрия"])

@router.get("/biometrics")
def get_biometrics_list_for_employee(employee_id: str) -> List[BiometricsResponse]:
    return []

@router.post("/biometrics")
def upload_biometrics(employee_id: str, files: List[UploadFile] = File()):
    return {}

@router.delete("/biometrics/{biometrics_id}")
def delete_biometrics_item(biometrics_id: str):
    return {}
