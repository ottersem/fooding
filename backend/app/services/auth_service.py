# 회원가입 및 로그인 로직을 담당하는 서비스 모듈임

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_
from core.models import (
  User,
  UserProfile,
  UserInterest,
  UserTimeSlot,
)
from app.schemas.auth_schema import (
  SignUpRequest,
  SignUpResponse,
  LogInRequest,
  LogInResponse,
)


def create_user_and_profile(db: Session, data: SignUpRequest) -> SignUpResponse:
  # username 또는 email이 이미 존재하는지 확인
  existing = (
    db.query(User)
    .filter(or_(User.email == data.email, User.username == data.username))
    .first()
  )
  if existing:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="username or email already exists",
    )

  # 요구사항에 따라 비밀번호를 그대로 저장 (실서비스에서는 절대 이렇게 하면 안 됨)
  user = User(
    username=data.username,
    email=data.email,
    password=data.password,
    is_active=True,
  )
  db.add(user)
  db.commit()
  db.refresh(user)

  # 프로필 생성
  profile = UserProfile(
    user_id=user.id,
    major=data.major,
    grade=data.grade,
    intro_text=data.intro_text,
    profile_image_url=None,  # 최초에는 빈 값으로 두고, 프론트에서 초성 아바타 등을 사용하도록 함
  )
  db.add(profile)

  # 관심사 연결을 저장
  for interest_id in data.interest_ids:
    db.add(
      UserInterest(
        user_id=user.id,
        interest_id=interest_id,
      )
    )

  # 시간대 연결을 저장
  for ts_id in data.time_slot_ids:
    db.add(
      UserTimeSlot(
        user_id=user.id,
        time_slot_id=ts_id,
      )
    )

  db.commit()

  return SignUpResponse(
    user_id=user.id,
    username=user.username,
    email=user.email,
  )


def log_in_user(db: Session, data: LogInRequest) -> LogInResponse:
  # 이메일과 비밀번호를 그대로 비교하여 로그인 검증
  user = (
    db.query(User)
    .filter(User.email == data.email, User.password == data.password)
    .first()
  )
  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="invalid email or password",
    )

  if not user.is_active:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="user is inactive",
    )

  return LogInResponse(
    user_id=user.id,
    username=user.username,
    email=user.email,
  )
