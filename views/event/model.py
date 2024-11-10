from datetime import date, time
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class Event(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    event_name: str
    event_date: date
    start_time: time
    end_time: time
    description: str


class EventPatch(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    event_name: str | None = None
    event_date: date | None = None
    start_time: time | None = None
    end_time: time | None = None
    description: str | None = None
    event_video: str | None = None


class EventResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    event_id: UUID
    event_name: str
    event_date: date
    start_time: time
    end_time: time
    description: str
    event_video: str | None = None
