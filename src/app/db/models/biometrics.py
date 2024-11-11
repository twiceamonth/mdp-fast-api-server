from sqlalchemy import Column, UUID, text, Date, Text, ForeignKey
from sqlalchemy.orm import relationship

from src.app.db.base import Base


class BiometricsDTO(Base):
    __tablename__ = "Biometrics"
    __table_args__ = {"schema": "mdp"}

    photo_id = Column(
        UUID,
        primary_key=True,
        server_default=text("nextval('photo_id_seq'::regclass)"),
    )
    upload_date = Column(Date)
    photo_path = Column(Text)
    employee_id = Column(ForeignKey("Employee.employee_id"), nullable=False)

    employee = relationship(
        "Employee",
    )


# primaryjoin="Employee.employee_id == Biometrics.employee_id"
