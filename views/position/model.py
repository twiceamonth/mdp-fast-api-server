from pydantic import BaseModel


class PositionResponse(BaseModel):
    position_id: str
    name: str

class Position(BaseModel):
    name: str