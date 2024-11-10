from sqlalchemy import Column, UUID, text, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base


class VisitDTO(Base):
    __tablename__ = "Visit"
    __table_args__ = {"schema": "mdp"}

    visit_id = Column(
        UUID,
        primary_key=True,
        server_default=text("nextval('visit_id_seq'::regclass)"),
    )
    employee_id = Column(ForeignKey("Employee.employee_id"), nullable=False)
    event_id = Column(ForeignKey("Event.event_id"), nullable=False)

    employee = relationship("Employee")
    event = relationship("Event")
