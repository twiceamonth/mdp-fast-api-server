from typing import List

from fastapi import APIRouter, Depends

from src.app.views.auth.crud import oauth2_scheme
from src.app.views.position.crud import create_new_position, get_positions, delete_position_by_id, update_position_patch
from src.app.views.position.model import PositionResponse, Position
from src.app.db.db_connection import session as db

router = APIRouter(tags=["Должности"])


@router.get("/positions", response_model=List[PositionResponse], dependencies=[Depends(oauth2_scheme)])
def get_positions_list() -> List[PositionResponse]:
    return get_positions(db)


@router.post("/position", response_model=PositionResponse, dependencies=[Depends(oauth2_scheme)])
def create_position(position: Position):
    return create_new_position(db, position)


@router.delete("/position/{position_id}", dependencies=[Depends(oauth2_scheme)])
def delete_position(position_id: str):
    return delete_position_by_id(db, position_id)


@router.patch("/position/{position_id}", response_model=PositionResponse, dependencies=[Depends(oauth2_scheme)])
def update_position(position_id: str, new_position: Position):
    return update_position_patch(db, position_id, new_position)
