from fastapi import HTTPException
from sqlalchemy import select, Result
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND

from src.app.db.base import check_uuid
from src.app.db.base import convert_to_db
from src.app.db.models.position import PositionDTO
from src.app.views.position.model import Position, PositionResponse


def get_positions(session: Session) -> list[PositionResponse]:
    q = select(PositionDTO).order_by(PositionDTO.name)
    result: Result = session.execute(q)
    positions = result.scalars().all()
    return [PositionResponse.model_validate(position) for position in positions]

def create_new_position(session: Session,new_position: Position):
    sao = convert_to_db(new_position, PositionDTO)
    session.add(sao)
    session.commit()
    session.refresh(sao)
    return sao

def delete_position_by_id(session: Session, position_id: str):
    check_uuid(position_id)
    position = session.get(PositionDTO, position_id)
    if position is not None:
        session.delete(position)
        session.commit()
        return { "message" : "Success" }
    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"Должности с id {position_id} не найдено!",
    )

def update_position_patch(session: Session, position_id: str, new_position: Position) -> PositionResponse:
    check_uuid(position_id)
    new_position.model_dump(exclude_unset=True)
    old_position = session.get(PositionDTO, position_id)
    if old_position is not None:
        for name, value in new_position.model_dump(exclude_unset=True).items():
            setattr(old_position, name, value)
        session.commit()
        return old_position
    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"Должности с id {position_id} не найдено!",
    )