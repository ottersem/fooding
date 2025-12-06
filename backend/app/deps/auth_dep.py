# 아주 단순한 인증 의존성을 제공하는 모듈
# 프론트에서 X-User-Id 헤더로 user_id를 넘겨준다고 가정함

from fastapi import Header, HTTPException, status, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.deps.db_dep import get_db
from core.models import User


class CurrentUser(BaseModel):
  id: int
  username: str
  email: str


def get_current_user(
  x_user_id: int = Header(..., alias="X-User-Id"),
  db: Session = Depends(get_db),
) -> CurrentUser:
  # 헤더에 담긴 user_id로 users 테이블을 조회
  user: User | None = db.query(User).filter(User.id == x_user_id).first()
  if not user or not user.is_active:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="invalid user id",
    )

  return CurrentUser(
    id=user.id,
    username=user.username,
    email=user.email,
  )
