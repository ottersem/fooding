from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field


class SignUpRequest(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=30)
    major: Optional[str] = None
    grade: Optional[str] = None
    intro_text: Optional[str] = Field(None, max_length=100)
    interest_ids: List[int]
    time_slot_ids: List[int]



class SignUpResponse(BaseModel):
  user_id: int
  username: str
  email: EmailStr


class LogInRequest(BaseModel):
  email: EmailStr
  password: str


class LogInResponse(BaseModel):
  user_id: int
  username: str
  email: EmailStr
