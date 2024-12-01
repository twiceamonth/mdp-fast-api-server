from sqlalchemy import Column, UUID, text, Text

from src.app.db.base import Base


class UserDTO(Base):
    __tablename__ = "User"
    __table_args__ = {"schema": "mdp"}

    login = Column(Text, primary_key=True)
    password_hash = Column(Text)