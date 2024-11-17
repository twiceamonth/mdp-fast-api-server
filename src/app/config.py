import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = os.getenv("DATABASE_URL")
    #"postgresql://postgres:12345@localhost:5432/postgres"
    #os.getenv("DATABASE_URL")


settings = Settings()
