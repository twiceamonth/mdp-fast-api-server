from datetime import date
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class BiometricsResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    photo_id: UUID
    upload_date: date
    photo_path: str
    employee_id: UUID


class Biometrics(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    photo_id: UUID | None = None
    photo_path: str | None = None
    employee_id: UUID | None = None