from sqlalchemy import Column, ForeignKey, text, UUID, String, Text
from sqlalchemy.orm import relationship

from src.app.db.base import Base


class EmployeeDTO(Base):
    __tablename__ = "Employee"
    __table_args__ = {"schema": "mdp"}

    employee_id = Column(
        UUID,
        primary_key=True,
        server_default=text("nextval('employee_id_seq'::regclass)"),
    )
    first_name = Column(String(100))
    second_name = Column(String(100))
    patronymic = Column(String(100), nullable=True)
    employee_photo = Column(Text)
    department_id = Column(UUID, ForeignKey("mdp.Department.department_id"), nullable=False)
    position_id = Column(UUID, ForeignKey("mdp.Position.position_id"), nullable=False)

    position = relationship("PositionDTO", back_populates="employees")
    department = relationship("DepartmentDTO", back_populates="employees")