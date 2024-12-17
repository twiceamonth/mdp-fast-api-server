import uuid

from fastapi import UploadFile, File, HTTPException, status
from sqlalchemy import select, Result
from sqlalchemy.orm import Session

from src.app.db.base import convert_to_db
from src.app.views.visit_mark.model import VisitMarkCreate
from src.app.db.models.visitmark import VisitMarkDTO
from src.app.db.base import check_uuid
from src.app.views.visit_mark.model import VisitMarkResponse


def get_visit_marks_for_visit(session: Session, visit_id: str) -> list[VisitMarkResponse]:
    check_uuid(visit_id)
    q = select(VisitMarkDTO).where(VisitMarkDTO.visit_id == visit_id)
    result: Result = session.execute(q)
    visit_marks = result.scalars().all()
    return [VisitMarkResponse.model_validate(vm) for vm in visit_marks]

def create_visit_new_mark(session: Session, visit_id: str, file: UploadFile = File()) -> VisitMarkResponse:
    check_uuid(visit_id)
    ext = file.filename.split(".")[-1]
    mark_new_id = uuid.uuid4()
    path = f"src/app/static_files/photos/{mark_new_id}.{ext}"
    response_path = f"photos-static/{mark_new_id}.{ext}"

    contents = file.file.read()
    with open(path, "wb") as f:
        f.write(contents)
    file.file.close()

    create_mark_visit = VisitMarkCreate(
        mark_id = mark_new_id,
        photo_path = response_path,
        visit_id = visit_id
    )

    sao = convert_to_db(create_mark_visit, VisitMarkDTO)
    session.add(sao)
    session.commit()
    session.refresh(sao)
    return sao

def delete(session: Session, mark_id: str):
    check_uuid(mark_id)
    mark = session.get(VisitMarkDTO, mark_id)
    if mark is not None:
        session.delete(mark)
        session.commit()
        return { "message" : "Success" }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Отметки с id {mark_id} не найдено!",
    )