from sqlalchemy import Column, UUID, text, Time, Text, ForeignKey

from src.app.db.base import Base


class VisitMarkDTO(Base):
    __tablename__ = "VisitMark"
    __table_args__ = {"schema": "mdp"}

    mark_id = Column(
        UUID,
        primary_key=True,
        server_default=text("nextval('mark_id_seq'::regclass)"),
    )
    fixation_time = Column(Time, server_default=text("nextval('fixation_time_seq'::regclass)"))
    photo_path = Column(Text)
    visit_id = Column(UUID, ForeignKey("mdp.Visit.visit_id"), nullable=False)
