from fastapi import APIRouter, Depends

from src.app.views.visit_mark.model import VisitMarkResponse
from src.app.views.employee.model import EmployeeResponse
from src.app.views.auth.crud import oauth2_scheme
from src.app.views.reports.model import EventReportResponse, EventProgrammeResponse, EventAbsentResponse, \
    EventDashboardResponse
from src.app.views.reports.crud import get_report_for_event_by_id, get_report_for_event_programme_by_id, \
    get_absent_participants_list_by_id, get_unknown_participants_list_by_id, get_dashboard_for_event_visits_by_id
from src.app.db.db_connection import session as db

router = APIRouter(tags=["Отчеты"])

@router.get("/event-report", response_model=EventReportResponse, dependencies=[Depends(oauth2_scheme)])
def get_report_for_event(event_id: str):
    return get_report_for_event_by_id(db, event_id)

@router.get("/event-programme-report", response_model=EventProgrammeResponse, dependencies=[Depends(oauth2_scheme)])
def get_report_for_event_programme(event_id: str):
    return get_report_for_event_programme_by_id(db, event_id)

@router.get("/absent-report", response_model=list[EmployeeResponse], dependencies=[Depends(oauth2_scheme)])
def get_absent_participants_list(event_id: str):
    return get_absent_participants_list_by_id(db, event_id)

@router.get("/unknown-report", response_model=list[VisitMarkResponse], dependencies=[Depends(oauth2_scheme)])
def get_unknown_participants_list(event_id: str):
    return get_unknown_participants_list_by_id(db, event_id)

@router.get("/dashboard-report", response_model=list[EventDashboardResponse], dependencies=[Depends(oauth2_scheme)])
def get_dashboard_for_event_visits(event_id: str):
    return get_dashboard_for_event_visits_by_id(db, event_id)