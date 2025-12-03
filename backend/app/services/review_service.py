# 후기 작성 및 조회 로직을 담당함

from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import Review, GroupMember
from app.schemas.review_schema import (
  ReviewCreateRequest,
  ReviewItemResponse,
  MyWrittenReviewsResponse,
)
#실제 참가자만 리뷰 가능하게 함.
from app.services.meeting_service import MEMBER_STATUS_ACCEPTED

def convert_score_to_rating(score_0_100: int) -> int:
  # 0~100 점수를 1~5 점수로 변환
  if score_0_100 <= 0:
    return 1
  if score_0_100 >= 100:
    return 5
  # 0~100을 5구간으로 나누어서 올림 처리
  return max(1, min(5, (score_0_100 + 19) // 20))


def create_or_update_reviews(
  db: Session,
  meeting_id: int,
  reviewer_id: int,
  data: ReviewCreateRequest,
) -> List[ReviewItemResponse]:
  # 이 유저가 실제로 해당 모임에 참여했는지 확인
  member = (
    db.query(GroupMember)
    .filter(
      GroupMember.group_id == meeting_id,
      GroupMember.user_id == reviewer_id,
      GroupMember.status == MEMBER_STATUS_ACCEPTED,
    )
    .first()
  )
  if not member:
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="only participants can write reviews",
    )

  result: List[ReviewItemResponse] = []

  for item in data.items:
    rating = convert_score_to_rating(item.score_0_100)

    existing = (
      db.query(Review)
      .filter(
        Review.group_id == meeting_id,
        Review.reviewer_id == reviewer_id,
        Review.reviewed_id == item.target_user_id,
      )
      .first()
    )

    if existing:
      existing.score = rating
      existing.comment = item.comment
      db.commit()
      db.refresh(existing)
      r = existing
    else:
      r = Review(
        group_id=meeting_id,
        reviewer_id=reviewer_id,
        reviewed_id=item.target_user_id,
        score=rating,
        comment=item.comment,
      )
      db.add(r)
      db.commit()
      db.refresh(r)

    result.append(
      ReviewItemResponse(
        id=r.id,
        group_id=r.group_id,
        reviewer_id=r.reviewer_id,
        reviewed_id=r.reviewed_id,
        score=r.score,
        comment=r.comment,
      )
    )

  return result


def get_my_written_reviews(
  db: Session,
  user_id: int,
) -> MyWrittenReviewsResponse:
  # 내가 작성한 리뷰 목록을 조회
  reviews = db.query(Review).filter(Review.reviewer_id == user_id).all()
  items = [
    ReviewItemResponse(
      id=r.id,
      group_id=r.group_id,
      reviewer_id=r.reviewer_id,
      reviewed_id=r.reviewed_id,
      score=r.score,
      comment=r.comment,
    )
    for r in reviews
  ]
  return MyWrittenReviewsResponse(reviews=items)
