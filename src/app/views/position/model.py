from uuid import UUID

from pydantic import BaseModel, ConfigDict


class PositionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    position_id: UUID
    name: str

class Position(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str