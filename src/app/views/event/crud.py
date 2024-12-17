import os

from fastapi import HTTPException, UploadFile, File, status
from sqlalchemy import select, Result
from sqlalchemy.orm import Session
from starlette.responses import FileResponse
from starlette.status import HTTP_404_NOT_FOUND
import requests

from src.app.views.biometrics.crud import get_all_biometrics
from src.app.db.base import convert_to_db, check_uuid
from src.app.db.models.event import EventDTO
from src.app.views.event.model import EventResponse, Event, EventPatch


def get_event_list(session: Session) -> list[EventResponse]:
    q = select(EventDTO).order_by(EventDTO.event_date)
    result: Result = session.execute(q)
    events = result.scalars().all()
    return [EventResponse.model_validate(event) for event in events]


def get_event(session: Session, event_id: str) -> EventResponse | None:
    check_uuid(event_id)
    event = session.get(EventDTO, event_id)
    if event is not None:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Мероприятие с id {event_id} не найдено!",
    )


def update_event_patch(
    session: Session, event_id: str, new_event: EventPatch
) -> EventResponse:
    check_uuid(event_id)
    new_event.model_dump(exclude_unset=True)
    old_event = session.get(EventDTO, event_id)
    if old_event is not None:
        for name, value in new_event.model_dump(exclude_unset=True).items():
            setattr(old_event, name, value)
        session.commit()
        return old_event
    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"Мероприятия с id {event_id} не найдено!",
    )


def delete(session: Session, event_id: str):
    check_uuid(event_id)
    event = get_event(session, event_id)
    if event is not None:
        session.delete(event)
        session.commit()
        return { "message" : "Success" }
    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"Мероприятия с id {event_id} не найдено!",
    )


def create_event_post(session: Session, new_event: Event):
    sao = convert_to_db(new_event, EventDTO)
    session.add(sao)
    session.commit()
    session.refresh(sao)
    return sao


def upload_video(session: Session, event_id: str, video: UploadFile = File()):
    check_uuid(event_id)
    event = get_event(session, event_id)
    if event is not None:
        ext = video.filename.split(".")[-1]
        path = f"src/app/static_files/videos/{event_id}.{ext}"
        response_path = f"videos-static/{event_id}.{ext}"
        contents = video.file.read()
        with open(path, "wb") as f:
            f.write(contents)
        video.file.close()
        update_event_patch(session, event_id, EventPatch(event_video=response_path))
        session.commit()
        send_to_ai_request(session, event_id)
        return event
    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"Мероприятия с id {event_id} не найдено!",
    )


def download_video(session: Session, event_id: str):
    check_uuid(event_id)
    for file in os.listdir("src/app/static_files/videos"):
        file_name, file_extension = file.split(".")
        if file_name == event_id:
            return FileResponse(
                path=f"videos/{file_name}.{file_extension}",
                filename=file_name.split(".")[0],
                media_type=f"video/{file_extension}",
            )
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"Файл для мероприятия с id {event_id} не найден!",
        )
    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"Мероприятия с id {event_id} не найдено!",
    )


def send_to_ai_request(session: Session, event_id: str):
    biometrics = get_all_biometrics(session)
    requests.get("http://mdp-ai-app:8001/startAI",
                 {
                     "event_id" : event_id,
                     "biometrics" : biometrics
                 })