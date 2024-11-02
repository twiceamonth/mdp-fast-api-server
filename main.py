from typing import List

from fastapi import FastAPI, Body, UploadFile, File
import uvicorn
from pydantic import BaseModel

app = FastAPI()


#           GET METHODS
@app.get("/events")
def get_events():
    return []

@app.get("/employees")
def get_employees():
    return []

@app.get("/departments")
def get_departments():
    return []

@app.get("/positions")
def get_positions():
    return []

@app.get("/biometrics")
def get_biometrics(employee_id: str):
    return []

@app.get("/invitations")
def get_invitations(event_id: str):
    return []

@app.get("/visits")
def get_visits(employee_id: str):
    return []

@app.get("/visitmarks")
def get_visit_marks(visit_id: str):
    return []

#           POST METHODS
@app.post("/event")
def create_event(event: BaseModel = Body()):
    return {}

@app.post("/employee")
def create_employee(employee: BaseModel = Body()):
    return {}

@app.post("/employee")
def create_employee(employee: BaseModel = Body()):
    return {}

@app.post("/department")
def create_department(department: BaseModel = Body()):
    return {}

@app.post("/position")
def create_position(position: BaseModel = Body()):
    return {}

@app.post("/biometrics")
def upload_biometrics(biometrics: BaseModel = Body(), files: List[UploadFile] = File()):
    return {}

@app.post("/invitation")
def create_invitation(invitation: BaseModel = Body()):
    return {}

@app.post("/visit")
def create_visit(visit: BaseModel = Body()):
    return {}

@app.post("/visit-mark")
def create_visit_mark(visitmark: BaseModel = Body(), file: UploadFile = File()):
    return {}

#           DELETE METHODS
@app.delete("/event/{event_id}")
def delete_event(event_id: str):
    return []

@app.delete("/employee/{employee_id}")
def delete_employees(employee_id: str):
    return []

@app.delete("/department/{department_id}")
def delete_departments(department_id: str):
    return []

@app.delete("/position/{position_id}")
def delete_positions(position_id: str):
    return []

@app.delete("/biometrics/{biometrics_id}")
def delete_biometrics_item(biometrics_id: str):
    return []

@app.delete("/invitations/{employee_id}/{event_id}")
def delete_invitation(employee_id: str,event_id: str):
    return []

@app.delete("/visits/{visit_id}")
def delete_visits(visit_id: str):
    return []

@app.delete("/visitmarks/{mark_id}")
def delete_visit_marks(mark_id: str):
    return []

#           PUT METHODS
@app.put("/event/{event_id}")
def update_event(event_id: str, new_event: BaseModel = Body()):
    return {}

@app.put("/employee/{employee_id}")
def update_event(employee_id: str, new_employee: BaseModel = Body()):
    return {}

@app.put("/department/{department_id}")
def update_event(department_id: str, new_department: BaseModel = Body()):
    return {}

@app.put("/position/{position_id}")
def update_event(position_id: str, new_position: BaseModel = Body()):
    return {}

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)