from fastapi import FastAPI
import uvicorn
from starlette.staticfiles import StaticFiles

from src.app.views.event.event_views import router as event_router
from src.app.views.biometrics.biometrics_views import router as biometrics_router
from src.app.views.department.department_views import router as department_router
from src.app.views.employee.employee_views import router as employee_router
from src.app.views.invitation.invitation_views import router as invitation_router
from src.app.views.position.position_views import router as position_router
from src.app.views.visit_mark.visit_mark_views import router as visit_mark_router
from src.app.views.visit.visit_views import router as visit_router

app = FastAPI()

app.mount("/biometrics", StaticFiles(directory="src/app/static_files/biometrics"), name="biometrics")
app.mount("/photos", StaticFiles(directory="src/app/static_files/photos"), name="photos")
app.mount("/videos", StaticFiles(directory="src/app/static_files/videos"), name="videos")

app.include_router(event_router)
app.include_router(employee_router)
app.include_router(biometrics_router)
app.include_router(department_router)
app.include_router(invitation_router)
app.include_router(position_router)
app.include_router(visit_mark_router)
app.include_router(visit_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
