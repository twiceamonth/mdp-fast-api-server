from typing import List

from fastapi import APIRouter

from views.position.model import PositionResponse, Position

router = APIRouter(tags=["Должности"])

@router.get("/positions")
def get_positions_list() -> List[PositionResponse]:
    return []

@router.post("/position")
def create_position(position: Position):
    return {}

@router.delete("/position/{position_id}")
def delete_position(position_id: str):
    return []

@router.patch("/position/{position_id}")
def update_position(position_id: str, new_position: Position):
    return {}