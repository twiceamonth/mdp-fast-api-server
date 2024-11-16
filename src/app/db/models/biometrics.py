from sqlalchemy import Column, UUID, text, Date, Text, ForeignKey
from sqlalchemy.orm import relationship

from src.app.db.models.employee import EmployeeDTO
from src.app.db.base import Base


class BiometricsDTO(Base):
    __tablename__ = "Biometrics"
    __table_args__ = {"schema": "mdp"}

    photo_id = Column(
        UUID,
        primary_key=True,
        server_default=text("nextval('photo_id_seq'::regclass)"),
    )
    upload_date = Column(Date, server_default=text("nextval('upload_date_seq'::regclass)"))
    photo_path = Column(Text)
    employee_id = Column(ForeignKey(EmployeeDTO.employee_id), nullable=False)

    employee = relationship(EmployeeDTO)


# primaryjoin="Employee.employee_id == Biometrics.employee_id"
