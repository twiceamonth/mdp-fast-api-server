from fastapi import FastAPI
import uvicorn

from views.event_views import router as event_router
from views.biometrics_views import router as biometrics_router
from views.department_views import router as department_router
from views.employee_views import router as employee_router
from views.invitation_views import router as invitation_router
from views.position_views import router as position_router
from views.visit_mark_views import router as visit_mark_router
from views.visit_views import router as visit_router

app = FastAPI()
app.include_router(event_router)
app.include_router(employee_router)
app.include_router(biometrics_router)
app.include_router(department_router)
app.include_router(invitation_router)
app.include_router(position_router)
app.include_router(visit_mark_router)
app.include_router(visit_router)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)