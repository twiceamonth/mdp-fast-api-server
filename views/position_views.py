from fastapi import APIRouter, Body
from pydantic import BaseModel

router = APIRouter(tags=["Должности"])

@router.get("/positions")
def get_positions_list():
    return []

@router.post("/position")
def create_position(position: BaseModel = Body()):
    return {}

@router.delete("/position/{position_id}")
def delete_position(position_id: str):
    return []

@router.put("/position/{position_id}")
def update_position(position_id: str, new_position: BaseModel = Body()):
    return {}