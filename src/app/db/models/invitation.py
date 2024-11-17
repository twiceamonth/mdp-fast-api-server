from sqlalchemy import Column, ForeignKey, UUID

from src.app.db.base import Base


class InvitationDTO(Base):
    __tablename__ = "Invitation"
    __table_args__ = {"schema": "mdp"}

    employee_id = Column(UUID, ForeignKey("mdp.Employee.employee_id"), nullable=False, primary_key=True)
    event_id = Column(UUID, ForeignKey("mdp.Event.event_id"), nullable=False, primary_key=True)
