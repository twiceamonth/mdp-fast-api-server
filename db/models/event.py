from sqlalchemy import String, Date, Time, Text, Column, UUID, text

from db.base import Base


class EventDTO(Base):
    __tablename__ = "Event"
    __table_args__ = {"schema": "mdp"}

    event_id = Column(
        UUID,
        primary_key=True,
        server_default=text("nextval('event_id_seq'::regclass)"),
    )
    event_name = Column(String(500))
    event_date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    description = Column(Text)
    event_video = Column(Text)
