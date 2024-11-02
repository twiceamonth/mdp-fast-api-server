from typing import List

from fastapi import APIRouter, Body, UploadFile, File
from pydantic import BaseModel

router = APIRouter(tags=["Биометрия"])

@router.get("/biometrics")
def get_biometrics_list_for_employee(employee_id: str):
    return []

@router.post("/biometrics")
def upload_biometrics(biometrics: BaseModel = Body(), files: List[UploadFile] = File()):
    return {}

@router.delete("/biometrics/{biometrics_id}")
def delete_biometrics_item(biometrics_id: str):
    return []