from typing import List

from fastapi import APIRouter

from src.app.views.invitation.model import InvitationResponse

router = APIRouter(tags=["Приглашения"])

@router.get("/invitations")
def get_invitations_list_for_event(event_id: str) -> List[InvitationResponse]:
    return []

@router.post("/invitation")
def create_invitation(invitation: InvitationResponse):
    return {}

@router.delete("/invitations/delete")
def delete_invitation(invitation: InvitationResponse):
    return []