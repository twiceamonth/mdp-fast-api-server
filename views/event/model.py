from datetime import date, time

from pydantic import BaseModel


class Event(BaseModel):
    event_name: str
    event_date: date
    start_time: time
    end_time: time
    description: str
    event_video: str | None = None

class EventResponse(BaseModel):
    event_id: str
    event_name: str
    event_date: date
    start_time: time
    end_time: time
    description: str
    event_video: str | None = None