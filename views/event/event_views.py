from typing import List

from fastapi import APIRouter, UploadFile, File

from model import EventResponse, Event

router = APIRouter(tags=["Мероприятия"])

@router.get("/events")
def get_events_list() -> List[EventResponse]:
    return []

@router.get("/events/{event_id}")
def get_event_by_id(event_id: str) -> Event:
    return {}

@router.get("/download-event-video")
def download_event_video():
    return {}

@router.post("/event")
def create_event(event: Event):
    return {}

@router.post("/upload-event-video")
def upload_event_video(video: UploadFile = File()):
    return {}

@router.delete("/event/{event_id}")
def delete_event(event_id: str):
    return {}

@router.patch("/event/{event_id}")
def update_event(event_id: str, new_event: Event):
    return {}