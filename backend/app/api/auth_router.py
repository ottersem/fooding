from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps.db_dep import get_db
from app.schemas.auth_schema import (
    SignUpRequest,
    SignUpResponse,
    LogInRequest,
    LogInResponse,
)
from app.services.auth_service import (
    create_user_and_profile,
    log_in_user,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=SignUpResponse)
def sign_up(
    body: SignUpRequest,
    db: Session = Depends(get_db),
):
    # 회원가입 및 온보딩을 처리함
    return create_user_and_profile(db, body)


@router.post("/login", response_model=LogInResponse)
def log_in(
    body: LogInRequest,
    db: Session = Depends(get_db),
):
    # 로그인 요청을 처리함
    return log_in_user(db, body)
