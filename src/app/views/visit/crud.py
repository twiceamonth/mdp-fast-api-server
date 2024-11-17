from fastapi import HTTPException
from sqlalchemy import select, Result
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND

from src.app.db.base import check_uuid
from src.app.db.base import convert_to_db
from src.app.views.visit.model import Visit
from src.app.views.visit.model import VisitResponse
from src.app.db.models.visit import VisitDTO


def get_visits_for_employee(session: Session, employee_id: str) -> list[VisitResponse]:
    q = select(VisitDTO).where(VisitDTO.employee_id == employee_id)
    result: Result = session.execute(q)
    visits = result.scalars().all()
    return [VisitResponse.model_validate(visit) for visit in visits]

def create_new_visit(session: Session, new_visit: Visit) -> VisitResponse:
    sao = convert_to_db(new_visit, VisitDTO)
    session.add(sao)
    session.commit()
    session.refresh(sao)
    return sao

def delete(session: Session, visit_id: str):
    check_uuid(visit_id)
    visit = session.get(VisitDTO, visit_id)
    if visit is not None:
        session.delete(visit)
        session.commit()
        return {"message": "Success"}
    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"Посещение с id {visit_id} не найдено!",
    )
