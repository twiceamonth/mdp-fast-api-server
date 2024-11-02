from fastapi import APIRouter, Body, UploadFile, File
from pydantic import BaseModel

router = APIRouter(tags=["Временные отметки о посещении"])

@router.get("/visit-marks")
def get_visit_marks_list_for_visit(visit_id: str):
    return []

@router.post("/visit-mark")
def create_visit_mark(visitmark: BaseModel = Body(), file: UploadFile = File()):
    return {}

@router.delete("/visitmarks/{mark_id}")
def delete_visit_marks(mark_id: str):
    return []