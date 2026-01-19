from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps.db_dep import get_db
from app.deps.auth_dep import get_current_user, CurrentUser
from app.schemas.review_schema import (
  ReviewCreateRequest,
  ReviewItemResponse,
  MyWrittenReviewsResponse,
)
from app.services.review_service import (
  create_or_update_reviews,
  get_my_written_reviews,
  get_review_detail, #1/18
)

router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.post("/meetings/{meeting_id}", response_model=List[ReviewItemResponse])
def create_or_update_reviews_endpoint(
  meeting_id: int,
  body: ReviewCreateRequest,
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  # 모임 참가자들에 대한 후기를 작성하거나 수정
  return create_or_update_reviews(db, meeting_id, current_user.id, body)


@router.get("/my_written", response_model=MyWrittenReviewsResponse)
def get_my_written_reviews_endpoint(
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  # 내가 작성한 후기 목록을 조회
  return get_my_written_reviews(db, current_user.id)

#1/18 추가 : 엔드포인트 추가
@router.get("/{review_id}", response_model=ReviewItemResponse)
def get_review_detail_endpoint(
  review_id: int,
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  
  #후기 수정 화면에서 내가 작성한 특정 후기 1개 조회
  return get_review_detail(db, review_id, current_user.id)
