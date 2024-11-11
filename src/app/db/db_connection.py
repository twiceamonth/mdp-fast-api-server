from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.app.config import settings

engine = create_engine(settings.db_url, echo_pool=True)
session = Session(engine)
