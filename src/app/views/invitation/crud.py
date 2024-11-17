from fastapi import HTTPException, status
from sqlalchemy import select, Result
from sqlalchemy.orm import Session

from src.app.db.base import convert_to_db
from src.app.db.models.invitation import InvitationDTO
from src.app.views.invitation.model import InvitationResponse


def get_invitations_for_event(session: Session, event_id: str) -> list[InvitationResponse]:
    q = select(InvitationDTO).where(InvitationDTO.event_id == event_id)
    result: Result = session.execute(q)
    invitations = result.scalars().all()
    return [InvitationResponse.model_validate(inv) for inv in invitations]

def create_new_invitation(session: Session, new_invitation: InvitationResponse) -> InvitationResponse:
    sao = convert_to_db(new_invitation, InvitationDTO)
    session.add(sao)
    session.commit()
    session.refresh(sao)
    return sao

def delete(session: Session, invitation: InvitationResponse):
    inv = session.get(InvitationDTO, [invitation.employee_id, invitation.event_id])
    if inv is not None:
        session.delete(inv)
        session.commit()
        return {"message": "Success"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Приглашения не найдено!",
    )