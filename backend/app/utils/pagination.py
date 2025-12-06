# 페이지네이션 offset 계산 유틸임

from typing import Optional


def get_offset(page: Optional[int], size: Optional[int]) -> int:
  # page와 size를 이용해 offset을 계산함
  if page is None or page < 1:
    page = 1
  if size is None or size < 1:
    size = 10
  return (page - 1) * size
