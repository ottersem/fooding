from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field


class InterestInfo(BaseModel):
  id: int
  name: str
  code: str


class TimeSlotInfo(BaseModel):
  id: int
  label: str
  code: str


class ProfileInfo(BaseModel):
  user_id: int
  username: str
  email: EmailStr
  major: Optional[str] = None
  grade: Optional[str] = None
  intro_text: Optional[str] = None
  profile_image_url: Optional[str] = None
  interests: List[InterestInfo]
  time_slots: List[TimeSlotInfo]


class ProfileUpdateRequest(BaseModel):
  username: Optional[str] = None
  email: Optional[EmailStr] = None
  major: Optional[str] = None
  grade: Optional[str] = None
  intro_text: Optional[str] = Field(None, max_length=100)
  profile_image_url: Optional[str] = None
  interest_ids: Optional[List[int]] = None
  time_slot_ids: Optional[List[int]] = None


class ReviewSummaryResponse(BaseModel):
  total_participated: int
  total_reviews_written: int
  average_score: float
