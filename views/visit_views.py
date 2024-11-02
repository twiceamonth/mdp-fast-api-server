from typing import List

from fastapi import APIRouter

from models import VisitResponse, Visit

router = APIRouter(tags=["Посещения мероприятий"])

@router.get("/visits")
def get_visits_list_for_employee(employee_id: str) -> List[VisitResponse]:
    return []

@router.post("/visit")
def create_visit(visit: Visit):
    return {}

@router.delete("/visits/{visit_id}")
def delete_visit(visit_id: str):
    return []