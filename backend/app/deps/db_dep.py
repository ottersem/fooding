# SQLAlchemy 세션을 FastAPI 의존성으로 제공하는 모듈임

from typing import Generator
from sqlalchemy.orm import Session
from core.database import SessionLocal


def get_db() -> Generator[Session, None, None]:
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
