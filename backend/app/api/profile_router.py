from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps.db_dep import get_db
from app.deps.auth_dep import get_current_user, CurrentUser
from app.schemas.profile_schema import (
  ProfileInfo,
  ProfileUpdateRequest,
  ReviewSummaryResponse,
)
from app.services.profile_service import (
  get_profile,
  update_profile,
  get_review_summary,
)

router = APIRouter(prefix="/profiles", tags=["profiles"])


@router.get("/me", response_model=ProfileInfo)
def get_me_profile(
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  # 현재 로그인한 사용자의 프로필을 반환
  return get_profile(db, current_user.id)


@router.put("/me", response_model=ProfileInfo)
def update_me_profile(
  body: ProfileUpdateRequest,
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  # 현재 로그인한 사용자의 프로필 정보를 수정
  return update_profile(db, current_user.id, body)


@router.get("/me/review_summary", response_model=ReviewSummaryResponse)
def get_me_review_summary(
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  # 현재 로그인한 사용자의 후기 요약 정보를 반환
  return get_review_summary(db, current_user.id)
