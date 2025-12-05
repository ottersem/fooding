from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.deps.db_dep import get_db
from app.deps.auth_dep import get_current_user, CurrentUser
from app.schemas.meeting_schema import (
  MeetingCreateRequest,
  MeetingUpdateRequest,
  MeetingSummary,
  MeetingDetail,
  MeetingConfirmRequest,
)
from app.services.meeting_service import (
  create_meeting,
  get_meeting_detail,
  get_main_meeting_list,
  update_meeting,
  delete_meeting,
  finish_meeting,
  confirm_meeting,
  get_my_meetings,
)

router = APIRouter(prefix="/meetings", tags=["meetings"])


@router.get("/main_list", response_model=List[MeetingSummary])
def get_main_list(
  tab: str = Query("recruiting"),
  page: Optional[int] = Query(1),
  size: Optional[int] = Query(10),

  # 🔽 새로 추가되는 필터/정렬 옵션
  interest_id: Optional[int] = Query(None, description="관심사 ID로 필터링"),
  time_slot_id: Optional[int] = Query(None, description="시간대 ID로 필터링"),
  sort_by: str = Query(
    "latest",
    description="정렬 기준: latest(기본), date, members",
  ),

  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  """
  메인 화면에서 사용할 모임 목록을 반환.
  - tab: recruiting / ongoing / finished / applied
  - interest_id: 해당 관심사로 필터링
  - time_slot_id: 해당 시간대로 필터링
  - sort_by:
      - latest  : 최신 생성순 (id desc)
      - date    : 모임 날짜 빠른 순 (meeting_date asc)
      - members : 현재 참여 인원 많은 순
  """
  return get_main_meeting_list(
    db=db,
    current_user_id=current_user.id,
    tab=tab,
    page=page,
    size=size,
    interest_id=interest_id,
    time_slot_id=time_slot_id,
    sort_by=sort_by,
  )



@router.post("", response_model=MeetingDetail)
def create_meeting_endpoint(
  body: MeetingCreateRequest,
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  # 새 모임을 생성
  return create_meeting(db, current_user.id, body)


@router.get("/{meeting_id}", response_model=MeetingDetail)
def get_meeting_detail_endpoint(
  meeting_id: int,
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  # 특정 모임의 상세 정보를 반환
  return get_meeting_detail(db, meeting_id, current_user.id)


@router.put("/{meeting_id}", response_model=MeetingDetail)
def update_meeting_endpoint(
  meeting_id: int,
  body: MeetingUpdateRequest,
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  # 모임 정보를 수정
  return update_meeting(db, meeting_id, current_user.id, body)


@router.delete("/{meeting_id}")
def delete_meeting_endpoint(
  meeting_id: int,
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  # 모임을 삭제
  delete_meeting(db, meeting_id, current_user.id)
  return {"detail": "deleted"}


@router.post("/{meeting_id}/finish", response_model=MeetingDetail)
def finish_meeting_endpoint(
  meeting_id: int,
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  # 모임을 종료 상태로 변경
  return finish_meeting(db, meeting_id, current_user.id)


@router.post("/{meeting_id}/confirm", response_model=MeetingDetail)
def confirm_meeting_endpoint(
  meeting_id: int,
  body: MeetingConfirmRequest,
  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  # 모임을 진행 상태로 변경하고 오픈채팅 링크를 저장
  return confirm_meeting(db, meeting_id, current_user.id, body)


@router.get("/my_list", response_model=List[MeetingSummary])
def get_my_meetings_endpoint(
  tab: str = Query("all"),
  page: Optional[int] = Query(1),
  size: Optional[int] = Query(10),

  interest_id: Optional[int] = Query(None, description="관심사 ID로 필터링"),
  time_slot_id: Optional[int] = Query(None, description="시간대 ID로 필터링"),
  sort_by: str = Query(
    "latest",
    description="정렬 기준: latest(기본), date, members",
  ),

  current_user: CurrentUser = Depends(get_current_user),
  db: Session = Depends(get_db),
):
  """
  내 모임 탭에서 사용할 목록을 반환.
  - tab: all / recruiting / ongoing / finished / applied
  - interest_id: 해당 관심사로 필터링
  - time_slot_id: 해당 시간대로 필터링
  - sort_by:
      - latest  : 최신 생성순
      - date    : 모임 날짜 빠른 순
      - members : 현재 참여 인원 많은 순
  """
  return get_my_meetings(
    db=db,
    current_user_id=current_user.id,
    tab=tab,
    page=page,
    size=size,
    interest_id=interest_id,
    time_slot_id=time_slot_id,
    sort_by=sort_by,
  )

