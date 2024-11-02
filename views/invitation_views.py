from fastapi import APIRouter, Body
from pydantic import BaseModel

router = APIRouter(tags=["Приглашения"])

@router.get("/invitations")
def get_invitations_list_for_event(event_id: str):
    return []

@router.post("/invitation")
def create_invitation(invitation: BaseModel = Body()):
    return {}

@router.delete("/invitations/{employee_id}/{event_id}")
def delete_invitation(employee_id: str,event_id: str):
    return []