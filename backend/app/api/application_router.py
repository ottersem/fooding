from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps.db_dep import get_db
from app.deps.auth_dep import get_current_user, CurrentUser
from app.schemas.application_schema import ApplicationsResponse
from app.services.application_service import (
  apply_to_meeting,
  cancel_application,
  get_applications,
  accept_application,
  reject_application,
)

router = APIRouter(prefix="/applications", tags=["applications"])


@router.post("/meetings/{meeting_id}/apply")
def apply_to_meeting_endpoint(
  meeting_id: int,
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  # 모임 신청을 처리함
  apply_to_meeting(db, meeting_id, current_user.id)
  return {"detail": "applied"}


@router.post("/meetings/{meeting_id}/cancel")
def cancel_application_endpoint(
  meeting_id: int,
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  # 모임 신청을 취소함
  cancel_application(db, meeting_id, current_user.id)
  return {"detail": "canceled"}


@router.get("/meetings/{meeting_id}", response_model=ApplicationsResponse)
def get_applications_endpoint(
  meeting_id: int,
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  # 주최자가 신청자 목록을 조회함
  return get_applications(db, meeting_id, current_user.id)


@router.post("/{application_id}/accept")
def accept_application_endpoint(
  application_id: int,
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  # 신청자를 수락함
  accept_application(db, application_id, current_user.id)
  return {"detail": "accepted"}


@router.post("/{application_id}/reject")
def reject_application_endpoint(
  application_id: int,
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  # 신청자를 거절함
  reject_application(db, application_id, current_user.id)
  return {"detail": "rejected"}
