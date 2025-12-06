from typing import List
from pydantic import BaseModel


class SingleReviewItem(BaseModel):
  target_user_id: int
  score_0_100: int
  comment: str


class ReviewCreateRequest(BaseModel):
  items: List[SingleReviewItem]


class ReviewItemResponse(BaseModel):
  id: int
  group_id: int
  reviewer_id: int
  review_ed_id: int
  score: int
  comment: str


class MyWrittenReviewsResponse(BaseModel):
  reviews: List[ReviewItemResponse]
