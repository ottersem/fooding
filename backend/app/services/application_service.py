
# 모임 신청/취소 및 신청자 관리 로직을 담당함

from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import (
  Group,
  GroupMember,
  UserProfile,
  UserInterest,
  Interest,
)
from app.schemas.application_schema import ApplicationsResponse, ApplicationInfo
from app.services.meeting_service import (
  MEMBER_STATUS_APPLIED,
  MEMBER_STATUS_ACCEPTED,
  MEMBER_STATUS_REJECTED,
  MEMBER_STATUS_CANCELED,
  ROLE_MEMBER,
)


def apply_to_meeting(db: Session, meeting_id: int, user_id: int) -> None:
  # 이미 신청 또는 참여한 기록이 있는지 확인
  existing = (
    db.query(GroupMember)
    .filter(GroupMember.group_id == meeting_id, GroupMember.user_id == user_id)
    .first()
  )

  if existing and existing.status != MEMBER_STATUS_CANCELED:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="already applied or joined",
    )

  if existing and existing.status == MEMBER_STATUS_CANCELED:
    # 취소 상태라면 다시 APPLIED로 바꿈
    existing.status = MEMBER_STATUS_APPLIED
    db.commit()
  else:
    # 새 신청 레코드를 생성함
    member = GroupMember(
      group_id=meeting_id,
      user_id=user_id,
      role=ROLE_MEMBER,
      status=MEMBER_STATUS_APPLIED,
    )
    db.add(member)
    db.commit()


def cancel_application(db: Session, meeting_id: int, user_id: int) -> None:
  # 신청 취소 로직
  member = (
    db.query(GroupMember)
    .filter(GroupMember.group_id == meeting_id, GroupMember.user_id == user_id)
    .first()
  )
  if not member:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="application not found",
    )

  member.status = MEMBER_STATUS_CANCELED
  db.commit()


def get_applications(
  db: Session, meeting_id: int, host_id: int
) -> ApplicationsResponse:
  # 신청자 목록을 조회함 (host만 가능함)
  group = db.query(Group).filter(Group.id == meeting_id).first()
  if not group:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="meeting not found",
    )
  if group.creator_id != host_id:
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="only creator can see applications",
    )

  members = (
    db.query(GroupMember)
    .filter(GroupMember.group_id == meeting_id)
    .all()
  )

  application_infos: List[ApplicationInfo] = []

  for m in members:
    user = m.user
    profile = (
      db.query(UserProfile)
      .filter(UserProfile.user_id == m.user_id)
      .first()
    )
    user_interests = (
      db.query(UserInterest)
      .join(Interest, UserInterest.interest_id == Interest.id)
      .filter(UserInterest.user_id == m.user_id)
      .all()
    )
    interest_codes = [ui.interest.code for ui in user_interests]

    application_infos.append(
      ApplicationInfo(
        application_id=m.id,
        user_id=m.user_id,
        username=user.username,
        major=profile.major if profile else None,
        grade=profile.grade if profile else None,
        interest_codes=interest_codes,
        status=m.status,
      )
    )

  return ApplicationsResponse(
    group_id=meeting_id,
    title=group.title,
    total_count=len(application_infos),
    applications=application_infos,
  )


def accept_application(db: Session, application_id: int, host_id: int) -> None:
  # 신청 수락 로직
  member = (
    db.query(GroupMember)
    .filter(GroupMember.id == application_id)
    .first()
  )
  if not member:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="application not found",
    )
  if member.group.creator_id != host_id:
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="only creator can accept",
    )

  member.status = MEMBER_STATUS_ACCEPTED
  db.commit()


def reject_application(db: Session, application_id: int, host_id: int) -> None:
  # 신청 거절 로직
  member = (
    db.query(GroupMember)
    .filter(GroupMember.id == application_id)
    .first()
  )
  if not member:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="application not found",
    )
  if member.group.creator_id != host_id:
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="only creator can reject",
    )

  member.status = MEMBER_STATUS_REJECTED
  db.commit()
