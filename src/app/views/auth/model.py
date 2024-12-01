from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    login: str
    password_hash: str

class UserInDb(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    login: str
    password_hash: str

class UserResponse(BaseModel):
    login: str  # This should match the type of your login field
    password_hash: str
    # Add other fields if necessary

    class Config:
        orm_mode = True  # This allows Pydantic to read data from SQLAlchemy models

