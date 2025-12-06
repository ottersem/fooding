from typing import List, Optional
from pydantic import BaseModel


class ApplicationInfo(BaseModel):
  application_id: int
  user_id: int
  username: str
  major: Optional[str] = None
  grade: Optional[str] = None
  interest_codes: List[str]
  status: str


class ApplicationsResponse(BaseModel):
  group_id: int
  title: str
  total_count: int
  applications: List[ApplicationInfo]
