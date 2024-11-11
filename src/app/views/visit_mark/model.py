from datetime import time

from pydantic import BaseModel


class VisitMarkResponse(BaseModel):
    mark_id: str
    fixation_time: time
    photo_path: str
    visit_id: str