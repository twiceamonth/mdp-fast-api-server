from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from src.app.db.base import Base


class InvitationDTO(Base):
    __tablename__ = "Invitation"
    __table_args__ = {"schema": "mdp"}

    employee_id = Column(ForeignKey("Employee.employee_id"), nullable=False)
    event_id = Column(ForeignKey("Event.event_id"), nullable=False)

    employee = relationship("Employee")
    event = relationship("Event")
