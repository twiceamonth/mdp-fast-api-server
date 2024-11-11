from typing import List

from fastapi import APIRouter, UploadFile, File, HTTPException, status

from src.app.db.db_connection import session as db
from src.app.views.event.crud import *
from src.app.views.event.model import Event, EventResponse, EventPatch

router = APIRouter(tags=["Мероприятия"])


@router.get("/events", response_model=List[EventResponse])
def get_events_list() -> List[EventResponse]:
    return get_event_list(db)


@router.get("/events/{event_id}", response_model=EventResponse)
def get_event_by_id(event_id: str) -> EventResponse:
    check_uuid(event_id)
    event = get_event(db, event_id)
    if event is not None:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Мероприятие с id {event_id} не найдено!",
    )


@router.post("/event", response_model=EventResponse)
def create_event(event: Event):
    return create_event_post(db, event)


@router.delete("/event/{event_id}")
def delete_event(event_id: str):
    check_uuid(event_id)
    delete(db, event_id)
    return {"details": "Success"}


@router.patch("/event/{event_id}", response_model=EventResponse)
def update_event(event_id: str, new_event: EventPatch):
    check_uuid(event_id)
    return update_event_patch(db, event_id, new_event)


@router.post("/upload-event-video/{event_id}")
def upload_event_video(event_id: str, video: UploadFile = File()):
    return upload_video(db, event_id, video)


@router.get("/download-event-video/{event_id}")
def download_event_video(event_id: str):
    return download_video(db, event_id)
