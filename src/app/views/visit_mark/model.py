from datetime import time
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class VisitMarkResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    mark_id: UUID
    fixation_time: time
    photo_path: str
    visit_id: UUID

class VisitMarkCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    mark_id: UUID
    photo_path: str
    visit_id: UUID