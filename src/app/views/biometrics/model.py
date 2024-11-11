from datetime import date

from pydantic import BaseModel


class BiometricsResponse(BaseModel):
    biometrics_id: str
    upload_date: date
    photo_path: str
    employee_id: str