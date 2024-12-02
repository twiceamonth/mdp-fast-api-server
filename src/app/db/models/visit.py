from sqlalchemy import Column, UUID, text, ForeignKey

from src.app.db.base import Base


class VisitDTO(Base):
    __tablename__ = "Visit"
    __table_args__ = {"schema": "mdp"}

    visit_id = Column(
        UUID,
        primary_key=True,
        server_default=text("nextval('visit_id_seq'::regclass)"),
    )
    employee_id = Column(ForeignKey("mdp.Employee.employee_id"), nullable=True)
    event_id = Column(ForeignKey("mdp.Event.event_id"), nullable=False)
