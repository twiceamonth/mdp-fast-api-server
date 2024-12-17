from typing import List

from fastapi import APIRouter, Depends

from src.app.views.auth.crud import oauth2_scheme
from src.app.views.visit.crud import get_visits_for_employee
from src.app.views.visit.crud import create_new_visit
from src.app.views.visit.crud import delete
from src.app.db.db_connection import session as db
from src.app.views.visit.model import VisitResponse, Visit

router = APIRouter(tags=["Посещения мероприятий"])

@router.get("/visits", response_model=list[VisitResponse], dependencies=[Depends(oauth2_scheme)])
def get_visits_list_for_employee(employee_id: str) -> List[VisitResponse]:
    return get_visits_for_employee(db, employee_id)

@router.post("/visit", response_model=VisitResponse, dependencies=[Depends(oauth2_scheme)])
def create_visit(visit: Visit):
    return create_new_visit(db, visit)

@router.delete("/visits/{visit_id}", dependencies=[Depends(oauth2_scheme)])
def delete_visit(visit_id: str):
    return delete(db, visit_id)