from fastapi import APIRouter, Body
from pydantic import BaseModel

router = APIRouter(tags=["Мероприятия"])

@router.get("/events")
def get_events_list():
    return []

@router.get("/events/{event_id}")
def get_event_by_id(event_id: str):
    return []

@router.post("/event")
def create_event(event: BaseModel = Body()):
    return {}

@router.delete("/event/{event_id}")
def delete_event(event_id: str):
    return []

@router.put("/event/{event_id}")
def update_event(event_id: str, new_event: BaseModel = Body()):
    return {}