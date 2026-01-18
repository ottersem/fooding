from typing import Optional, List
from pydantic import BaseModel
from datetime import date


class MeetingCreateRequest(BaseModel):
  interest_id: int
  category: str #1/18추가
  title: str
  description: str
  meeting_date: date
  time_slot_id: int
  place: str
  max_participants: int


class MeetingUpdateRequest(BaseModel):
  interest_id: Optional[int] = None
  category: Optional[str] = None #1/18추가
  title: Optional[str] = None
  description: Optional[str] = None
  meeting_date: Optional[date] = None
  time_slot_id: Optional[int] = None
  place: Optional[str] = None
  max_participants: Optional[int] = None


class MeetingSummary(BaseModel):
  id: int
  title: str
  category: str #1/18추가
  interest_name: str
  interest_code: str
  meeting_date: date
  time_slot_label: str
  current_participants: int
  max_participants: int
  status: str


class MeetingDetail(BaseModel):
  id: int
  title: str
  category: str #1/18추가
  description: str
  interest_name: str
  interest_code: str
  meeting_date: date
  time_slot_label: str
  place: str
  max_participants: int
  status: str
  creator_id: int
  creator_name: str
  current_participants: int
  my_member_status: Optional[str] = None
  open_chat_link: Optional[str] = None


class MeetingConfirmRequest(BaseModel):
  open_chat_link: str
