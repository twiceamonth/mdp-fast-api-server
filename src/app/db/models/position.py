from sqlalchemy import Column, text, Text, UUID
from sqlalchemy.orm import relationship

from src.app.db.base import Base


class PositionDTO(Base):
    __tablename__ = "Position"
    __table_args__ = {"schema": "mdp"}

    position_id = Column(
        UUID,
        primary_key=True,
        server_default=text("nextval('position_id_seq'::regclass)"),
    )
    name = Column(Text)

    employees = relationship("EmployeeDTO", back_populates="position")
