# 모임(그룹) 관련 비즈니스 로직을 담당함

from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session, joinedload
from core.models import (
  Group,
  GroupMember,
)
from app.schemas.meeting_schema import (
  MeetingCreateRequest,
  MeetingUpdateRequest,
  MeetingSummary,
  MeetingDetail,
  MeetingConfirmRequest,
)
from app.utils.pagination import get_offset

# 모임 상태 상수 정의
STATUS_RECRUITING = "RECRUITING"
STATUS_ONGOING = "ONGOING"
STATUS_FINISHED = "FINISHED"

# 그룹 멤버 상태 상수 정의
MEMBER_STATUS_APPLIED = "APPLIED"
MEMBER_STATUS_ACCEPTED = "ACCEPTED"
MEMBER_STATUS_REJECTED = "REJECTED"
MEMBER_STATUS_CANCELED = "CANCELED"

ROLE_HOST = "HOST"
ROLE_MEMBER = "MEMBER"


def create_meeting(
  db: Session,
  creator_id: int,
  data: MeetingCreateRequest,
) -> MeetingDetail:
  # groups 테이블에 새 모임을 생성함
  group = Group(
    creator_id=creator_id,
    interest_id=data.interest_id,
    title=data.title,
    description=data.description,
    meeting_date=data.meeting_date,
    time_slot_id=data.time_slot_id,
    place=data.place,
    max_participants=data.max_participants,
    status=STATUS_RECRUITING,
  )
  db.add(group)
  db.commit()
  db.refresh(group)

  # 생성자를 HOST로 group_members에 등록
  host_member = GroupMember(
    group_id=group.id,
    user_id=creator_id,
    role=ROLE_HOST,
    status=MEMBER_STATUS_ACCEPTED,
  )
  db.add(host_member)
  db.commit()

  return get_meeting_detail(db, group.id, creator_id)


def get_meeting_detail(
  db: Session,
  meeting_id: int,
  current_user_id: Optional[int],
) -> MeetingDetail:
  # 모임 상세 정보를 조회
  group: Group | None = (
    db.query(Group)
    .options(
      joinedload(Group.interest),
      joinedload(Group.time_slot),
      joinedload(Group.creator),
      joinedload(Group.members),
    )
    .filter(Group.id == meeting_id)
    .first()
  )
  if not group:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="meeting not found",
    )

  current_members = [
    m for m in group.members if m.status == MEMBER_STATUS_ACCEPTED
  ]
  current_participants = len(current_members) 

  my_member_status: Optional[str] = None
  if current_user_id is not None:
    for m in group.members:
      if m.user_id == current_user_id:
        my_member_status = m.status
        break

  return MeetingDetail(
    id=group.id,
    title=group.title,
    description=group.description,
    interest_name=group.interest.name,
    interest_code=group.interest.code,
    meeting_date=group.meeting_date,
    time_slot_label=group.time_slot.label,
    place=group.place,
    max_participants=group.max_participants,
    status=group.status,
    creator_id=group.creator_id,
    creator_name=group.creator.username,
    current_participants=current_participants,
    my_member_status=my_member_status,
    open_chat_link=group.open_chat_link,
  )


def get_main_meeting_list(
  db: Session,
  current_user_id: int,
  tab: str,
  page: Optional[int],
  size: Optional[int],
  interest_id: Optional[int],
  time_slot_id: Optional[int],
  sort_by: str,
) -> List[MeetingSummary]:
  # 메인 탭별 모임 목록을 조회
  offset = get_offset(page, size)
  limit = size or 10

  query = (
    db.query(Group)
    .options(
      joinedload(Group.interest),
      joinedload(Group.time_slot),
      joinedload(Group.members),
    )
  )

  # 1) 탭(status) 필터
  if tab == "recruiting":
    query = query.filter(Group.status == STATUS_RECRUITING)
  elif tab == "ongoing":
    query = query.filter(Group.status == STATUS_ONGOING)
  elif tab == "finished":
    query = query.filter(Group.status == STATUS_FINISHED)
  elif tab == "applied":
    my_members = (
      db.query(GroupMember)
      .filter(GroupMember.user_id == current_user_id)
      .all()
    )
    group_ids = list({m.group_id for m in my_members})
    if not group_ids:
      return []
    query = query.filter(Group.id.in_(group_ids))
  else:
    # 기본값: 모집중
    query = query.filter(Group.status == STATUS_RECRUITING)

  # 2) 관심사 필터
  if interest_id is not None:
    query = query.filter(Group.interest_id == interest_id)

  # 3) 시간대 필터
  if time_slot_id is not None:
    query = query.filter(Group.time_slot_id == time_slot_id)

  # 4) 정렬 옵션
  if sort_by == "date":
    # 모임 날짜 빠른 순
    query = query.order_by(Group.meeting_date.asc(), Group.id.desc())
    groups = query.offset(offset).limit(limit).all()
  elif sort_by == "latest":
    # 최신 생성 순
    query = query.order_by(Group.id.desc())
    groups = query.offset(offset).limit(limit).all()
  elif sort_by == "members":
    # 참여 인원 많은 순 (Python에서 정렬 - joinedload로 미리 멤버 로드됨)
    groups = query.offset(offset).limit(limit).all()
    groups.sort(
      key=lambda g: len(
        [m for m in g.members if m.status == MEMBER_STATUS_ACCEPTED]
      ),
      reverse=True,
    )
  else:
    # 알 수 없는 sort 옵션이면 기본: latest
    query = query.order_by(Group.id.desc())
    groups = query.offset(offset).limit(limit).all()

  summaries: List[MeetingSummary] = []
  for g in groups:
    accepted_members = [
      m for m in g.members if m.status == MEMBER_STATUS_ACCEPTED
    ]
    summaries.append(
      MeetingSummary(
        id=g.id,
        title=g.title,
        interest_name=g.interest.name,
        interest_code=g.interest.code,
        meeting_date=g.meeting_date,
        time_slot_label=g.time_slot.label,
        current_member_count=len(accepted_members),
        max_participants=g.max_participants,
        status=g.status,
      )
    )

  return summaries



def update_meeting(
  db: Session,
  meeting_id: int,
  current_user_id: int,
  data: MeetingUpdateRequest,
) -> MeetingDetail:
  # 모임 수정 로직
  group: Group | None = db.query(Group).filter(Group.id == meeting_id).first()
  if not group:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="meeting not found",
    )
  if group.creator_id != current_user_id:
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="only creator can update meeting",
    )

  update_data = data.dict(exclude_none=True)
  for key, value in update_data.items():
    setattr(group, key, value)

  db.commit()
  db.refresh(group)

  return get_meeting_detail(db, meeting_id, current_user_id)


def delete_meeting(
  db: Session,
  meeting_id: int,
  current_user_id: int,
) -> None:
  # 모임 삭제 로직
  group: Group | None = db.query(Group).filter(Group.id == meeting_id).first()
  if not group:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="meeting not found",
    )
  if group.creator_id != current_user_id:
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="only creator can delete meeting",
    )

  # 관련 멤버와 리뷰 먼저 삭제한 뒤 그룹을 삭제
  db.query(GroupMember).filter(GroupMember.group_id == meeting_id).delete()
  from core.models import Review  # 순환참조 방지용 임포로로로로롤트
  db.query(Review).filter(Review.group_id == meeting_id).delete()
  db.delete(group)
  db.commit()


def finish_meeting(
  db: Session,
  meeting_id: int,
  current_user_id: int,
) -> MeetingDetail:
  # 모임을 종료 상태로 변경
  group: Group | None = db.query(Group).filter(Group.id == meeting_id).first()
  if not group:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="meeting not found",
    )
  if group.creator_id != current_user_id:
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="only creator can finish meeting",
    )

  group.status = STATUS_FINISHED
  db.commit()
  db.refresh(group)

  return get_meeting_detail(db, meeting_id, current_user_id)


def confirm_meeting(
  db: Session,
  meeting_id: int,
  current_user_id: int,
  data: MeetingConfirmRequest,
) -> MeetingDetail:
  # 모임을 진행 상태로 변경하고 오픈채팅 링크를 저장
  group: Group | None = db.query(Group).filter(Group.id == meeting_id).first()
  if not group:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="meeting not found",
    )
  if group.creator_id != current_user_id:
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="only creator can confirm meeting",
    )

  group.status = STATUS_ONGOING
  group.open_chat_link = data.open_chat_link
  db.commit()
  db.refresh(group)

  return get_meeting_detail(db, meeting_id, current_user_id)


def get_my_meetings(
  db: Session,
  current_user_id: int,
  tab: str,
  page: Optional[int],
  size: Optional[int],
  interest_id: Optional[int],
  time_slot_id: Optional[int],
  sort_by: str,
) -> List[MeetingSummary]:
  # 내 모임 탭에서 사용할 목록을 조회
  offset = get_offset(page, size)
  limit = size or 10

  my_members = (
    db.query(GroupMember)
    .filter(GroupMember.user_id == current_user_id)
    .all()
  )
  group_ids = list({m.group_id for m in my_members})
  if not group_ids:
    return []

  query = (
    db.query(Group)
    .options(
      joinedload(Group.interest),
      joinedload(Group.time_slot),
      joinedload(Group.members),
    )
    .filter(Group.id.in_(group_ids))
  )

  # 1) 탭(status) 필터
  if tab == "recruiting":
    query = query.filter(Group.status == STATUS_RECRUITING)
  elif tab == "ongoing":
    query = query.filter(Group.status == STATUS_ONGOING)
  elif tab == "finished":
    query = query.filter(Group.status == STATUS_FINISHED)
  # tab == "applied" / "all" 은 status 필터 없음

  # 2) 관심사 필터
  if interest_id is not None:
    query = query.filter(Group.interest_id == interest_id)

  # 3) 시간대 필터
  if time_slot_id is not None:
    query = query.filter(Group.time_slot_id == time_slot_id)

  # 4) 정렬 옵션
  if sort_by == "date":
    query = query.order_by(Group.meeting_date.asc(), Group.id.desc())
    groups = query.offset(offset).limit(limit).all()
  elif sort_by == "latest":
    query = query.order_by(Group.id.desc())
    groups = query.offset(offset).limit(limit).all()
  elif sort_by == "members":
    groups = query.offset(offset).limit(limit).all()
    groups.sort(
      key=lambda g: len(
        [m for m in g.members if m.status == MEMBER_STATUS_ACCEPTED]
      ),
      reverse=True,
    )
  else:
    query = query.order_by(Group.id.desc())
    groups = query.offset(offset).limit(limit).all()

  summaries: List[MeetingSummary] = []
  for g in groups:
    accepted_members = [
      m for m in g.members if m.status == MEMBER_STATUS_ACCEPTED
    ]
    summaries.append(
      MeetingSummary(
        id=g.id,
        title=g.title,
        interest_name=g.interest.name,
        interest_code=g.interest.code,
        meeting_date=g.meeting_date,
        time_slot_label=g.time_slot.label,
        current_member_count=len(accepted_members),
        max_participants=g.max_participants,
        status=g.status,
      )
    )

  return summaries

