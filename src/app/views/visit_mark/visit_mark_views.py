from typing import List

from fastapi import APIRouter, UploadFile, File, Depends

from src.app.views.auth.crud import oauth2_scheme
from src.app.views.visit_mark.crud import get_visit_marks_for_visit
from src.app.views.visit_mark.crud import create_visit_new_mark
from src.app.views.visit_mark.crud import delete
from src.app.db.db_connection import session as db
from src.app.views.visit_mark.model import VisitMarkResponse

router = APIRouter(tags=["Временные отметки о посещении"])

@router.get("/visit-marks", response_model=list[VisitMarkResponse], dependencies=[Depends(oauth2_scheme)])
def get_visit_marks_list_for_visit(visit_id: str) -> List[VisitMarkResponse]:
    return get_visit_marks_for_visit(db, visit_id)

@router.post("/visit-marks", response_model=VisitMarkResponse, dependencies=[Depends(oauth2_scheme)])
def create_visit_mark(visit_id: str, file: UploadFile = File()):
    return create_visit_new_mark(db, visit_id, file)

@router.delete("/visitmarks/{mark_id}", dependencies=[Depends(oauth2_scheme)])
def delete_visit_marks(mark_id: str):
    return delete(db, mark_id)