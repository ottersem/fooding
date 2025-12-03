# 프로필 조회/수정 및 후기 요약 로직을 담당함

from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import func
from core.models import (
  User,
  UserProfile,
  UserInterest,
  UserTimeSlot,
  Interest,
  TimeSlot,
  GroupMember,
  Review,
)
from app.schemas.profile_schema import (
  ProfileInfo,
  InterestInfo,
  TimeSlotInfo,
  ProfileUpdateRequest,
  ReviewSummaryResponse,
)


def get_profile(db: Session, user_id: int) -> ProfileInfo:
  # 유저와 프로필, 관심사, 시간대를 모두 조회
  user = db.query(User).filter(User.id == user_id).first()
  profile = db.query(UserProfile).filter(UserProfile.user_id == user_id).first()

  user_interests = (
    db.query(UserInterest)
    .join(Interest, UserInterest.interest_id == Interest.id)
    .filter(UserInterest.user_id == user_id)
    .all()
  )
  user_time_slots = (
    db.query(UserTimeSlot)
    .join(TimeSlot, UserTimeSlot.time_slot_id == TimeSlot.id)
    .filter(UserTimeSlot.user_id == user_id)
    .all()
  )

  interests: List[InterestInfo] = [
    InterestInfo(
      id=ui.interest.id,
      name=ui.interest.name,
      code=ui.interest.code,
    )
    for ui in user_interests
  ]

  time_slots: List[TimeSlotInfo] = [
    TimeSlotInfo(
      id=ut.time_slot.id,
      label=ut.time_slot.label,
      code=ut.time_slot.code,
    )
    for ut in user_time_slots
  ]

  return ProfileInfo(
    user_id=user.id,
    username=user.username,
    email=user.email,
    major=profile.major if profile else None,
    grade=profile.grade if profile else None,
    intro_text=profile.intro_text if profile else None,
    profile_image_url=profile.profile_image_url if profile else None,
    interests=interests,
    time_slots=time_slots,
  )


def update_profile(
  db: Session,
  user_id: int,
  data: ProfileUpdateRequest,
) -> ProfileInfo:
  # 유저 기본 정보를 수정
  user = db.query(User).filter(User.id == user_id).first()
  if data.username is not None:
    user.username = data.username
  if data.email is not None:
    user.email = data.email

  # 프로필 정보를 수정하거나 새로 생성
  profile = db.query(UserProfile).filter(UserProfile.user_id == user_id).first()
  if not profile:
    profile = UserProfile(user_id=user_id)
    db.add(profile)

  if data.major is not None:
    profile.major = data.major
  if data.grade is not None:
    profile.grade = data.grade
  if data.intro_text is not None:
    profile.intro_text = data.intro_text
  if data.profile_image_url is not None:
    profile.profile_image_url = data.profile_image_url

  # 관심사와 시간대가 들어온 경우, 기존 것을 지우고 다시 저장
  if data.interest_ids is not None:
    db.query(UserInterest).filter(UserInterest.user_id == user_id).delete()
    for interest_id in data.interest_ids:
      db.add(UserInterest(user_id=user_id, interest_id=interest_id))

  if data.time_slot_ids is not None:
    db.query(UserTimeSlot).filter(UserTimeSlot.user_id == user_id).delete()
    for ts_id in data.time_slot_ids:
      db.add(UserTimeSlot(user_id=user_id, time_slot_id=ts_id))

  db.commit()
  db.refresh(user)
  db.refresh(profile)

  # 최신 상태를 다시 조회해서 반환
  return get_profile(db, user_id)

#"실제로 참여 완료한 모임 수"로 리뷰 작성 가능 조건 추가
from app.services.meeting_service import MEMBER_STATUS_ACCEPTED

def get_review_summary(db: Session, user_id: int) -> ReviewSummaryResponse:
  # 이 유저가 그룹 멤버로 참여한 횟수를 센다음 참여 횟수로 사용
  member_count = db.query(func.count(GroupMember.id)).filter(
    GroupMember.user_id == user_id,
    GroupMember.status == MEMBER_STATUS_ACCEPTED,
  ).scalar() or 0

  # 이 유저가 쓴 리뷰 수를 조회
  total_reviews_written = (
    db.query(func.count(Review.id))
    .filter(Review.reviewer_id == user_id)
    .scalar()
    or 0
  )

  # 이 유저가 받은 리뷰의 평균 점수를 계산
  avg_score = (
    db.query(func.avg(Review.score))
    .filter(Review.review_ed_id == user_id)
    .scalar()
  )
  if avg_score is None:
    avg_score = 0.0

  return ReviewSummaryResponse(
    total_participated=member_count,
    total_reviews_written=total_reviews_written,
    average_score=float(avg_score),
  )
