from click import UUID
from sqlalchemy import Column, text, Text
from sqlalchemy.orm import Mapped

from db.base import Base


class DepartmentDTO(Base):
    __tablename__ = "Department"
    __table_args__ = {"schema": "mdp"}

    department_id = Column(
        UUID,
        primary_key=True,
        server_default=text("nextval('department_id_seq'::regclass)"),
    )
    name = Column(Text)
