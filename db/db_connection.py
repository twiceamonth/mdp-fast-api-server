from asyncio import current_task

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker

from config import settings

engine = create_engine(settings.db_url, echo_pool=True)
session = Session(engine)
