from typing import List

from fastapi import APIRouter, UploadFile, File

from views.visit_mark.model import VisitMarkResponse

router = APIRouter(tags=["Временные отметки о посещении"])

@router.get("/visit-marks")
def get_visit_marks_list_for_visit(visit_id: str) -> List[VisitMarkResponse]:
    return []

@router.post("/visit-marks")
def create_visit_mark(visit_id: str, file: UploadFile = File()):
    return {}

@router.delete("/visitmarks/{mark_id}")
def delete_visit_marks(mark_id: str):
    return []