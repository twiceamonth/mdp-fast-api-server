from typing import Type
from uuid import UUID

from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    pass


# __abstract__ = True

#    @declared_attr.directive
#   def __tablename__(cls) -> str:
#      return f"{cls.__name__.lower()}"


def check_uuid(uuid: str):
    try:
        event_id = UUID(uuid)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Не коректный формат event_id. Должна быть корректная форма UUID.",
        )


def convert_to_db(pydantic_model: BaseModel, sqlalchemy_model_class: Type[Base]):
    # Получаем словарь данных из Pydantic модели
    data = pydantic_model.model_dump()

    # Проходим по всем полям SQLAlchemy модели и заполняем их значениями из Pydantic модели
    sqlalchemy_model = sqlalchemy_model_class()
    for key, value in data.items():
        if hasattr(sqlalchemy_model, key):
            setattr(sqlalchemy_model, key, value)

    # Возвращаем заполненный объект SQLAlchemy модели
    return sqlalchemy_model
