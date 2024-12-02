from fastapi import HTTPException, status
from sqlalchemy import select, distinct, func, extract, join
from sqlalchemy.dialects.postgresql import INTERVAL, TIME
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import count

from src.app.views.visit_mark.model import VisitMarkResponse
from src.app.views.employee.model import EmployeeResponse
from src.app.db.models.employee import EmployeeDTO
from src.app.db.base import check_uuid
from src.app.db.models.visit import VisitDTO
from src.app.db.models.visitmark import VisitMarkDTO
from src.app.views.reports.model import EventReportResponse, EventProgrammeResponse, EventAbsentResponse, \
    EventDashboardResponse
from src.app.db.models.event import EventDTO


def get_report_for_event_by_id(session: Session, event_id: str):
    check_uuid(event_id)
    event_dto = session.get(EventDTO, event_id)
    if event_dto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Мероприятие с id {event_id} не найдено!",
        )
    query = (select(count(distinct(VisitDTO.employee_id)))
                        .select_from(VisitDTO)
                         .where(VisitDTO.event_id == event_id)
                         .join(VisitMarkDTO, VisitMarkDTO.visit_id == VisitDTO.visit_id)
                         .where(VisitDTO.event_id == event_id))
    visitors_count = session.execute(query).scalar()

    response = EventReportResponse(
        event_name = event_dto.event_name,
        start_time = event_dto.start_time,
        end_time = event_dto.end_time,
        visitor_count = visitors_count
    )

    return response


def get_report_for_event_programme_by_id(session: Session, event_id: str):
    check_uuid(event_id)

    event_dto = session.get(EventDTO, event_id)
    if event_dto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Мероприятие с id {event_id} не найдено!",
        )
    el_query = select(EmployeeDTO).join(VisitDTO).where(VisitDTO.event_id == event_id)
    el_query_response = session.execute(el_query).scalars().all()
    employee_list = [EmployeeResponse.model_validate(emp) for emp in el_query_response]

    response = EventProgrammeResponse(
        event_name = event_dto.event_name,
        start_time = event_dto.start_time,
        end_time = event_dto.end_time,
        description = event_dto.description,
        participants = employee_list
    )

    return response

def get_absent_participants_list_by_id(session: Session, event_id: str):
    check_uuid(event_id)
    event_dto = session.get(EventDTO, event_id)
    if event_dto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Мероприятие с id {event_id} не найдено!",
        )

    attended_employees_query = (
        select(VisitMarkDTO.visit_id)
        .join(VisitDTO)
        .where(VisitDTO.event_id == event_id)
    )

    no_show_query = (
        select(VisitDTO.employee_id)
        .where(VisitDTO.event_id == event_id)
        .except_(attended_employees_query)  # Исключаем тех, кто пришел
    )

    no_show_employees_ids = session.execute(no_show_query).scalars().all()

    nse_q = select(EmployeeDTO).where(EmployeeDTO.employee_id.in_(no_show_employees_ids))
    no_show_employees = session.execute(nse_q).scalars().all()

    return [EmployeeResponse.model_validate(emp) for emp in no_show_employees]

def get_unknown_participants_list_by_id(session: Session, event_id: str):
    check_uuid(event_id)
    event_dto = session.get(EventDTO, event_id)
    if event_dto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Мероприятие с id {event_id} не найдено!",
        )
    result_query = (
        session.query(VisitMarkDTO)
        .join(VisitDTO, VisitMarkDTO.visit_id == VisitDTO.visit_id)
        .filter(VisitDTO.event_id == event_id)
        .filter(VisitDTO.employee_id == None)  # Фильтруем по employee_id равным null
        .order_by(VisitMarkDTO.fixation_time)  # Сортируем по времени
    )
    result = session.execute(result_query).scalars().all()
    return [VisitMarkResponse.model_validate(visit_mark) for visit_mark in result]


def get_dashboard_for_event_visits_by_id(session: Session, event_id: str):
    check_uuid(event_id)
    event_dto = session.get(EventDTO, event_id)
    if event_dto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Мероприятие с id {event_id} не найдено!",
        )

    # Получаем время начала и конца мероприятия
    event_start = event_dto.start_time  # Время начала в формате TIME
    event_end = event_dto.end_time      # Время конца в формате TIME

    # Определяем временные интервалы по 5 минут
    interval_start = func.date_trunc(
        'minute',
        func.date_trunc('hour', VisitMarkDTO.fixation_time) +
        (func.floor(extract('minute', VisitMarkDTO.fixation_time) / 5) * 5 * func.cast('1 minute', INTERVAL))
    )

    # Запрос для получения количества уникальных посетителей за каждые 5 минут
    result_query = (
        session.query(
            func.to_char(interval_start, 'HH24:MI').label("time"),  # Форматируем время
            func.count(func.distinct(VisitDTO.employee_id)).label("visitor_count"),
        )
        .join(VisitDTO, VisitMarkDTO.visit_id == VisitDTO.visit_id)
        .filter(VisitMarkDTO.fixation_time >= event_start)  # Фильтруем по времени начала мероприятия
        .filter(VisitMarkDTO.fixation_time < event_end)     # Фильтруем по времени конца мероприятия
        .group_by(interval_start)
        .order_by(interval_start)  # Убедитесь, что сортировка по интервалу
    )

    result = session.execute(result_query).all()

    # Преобразуем результат в удобный формат
    return [EventDashboardResponse.model_validate(r) for r in result]