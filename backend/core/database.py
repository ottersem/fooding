
# SQLAlchemy 엔진과 세션, Base를 정의하는 모듈임

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings

# SQLAlchemy Base 클래스
Base = declarative_base()

# MySQL 엔진을 생성함
engine = create_engine(
  settings.db_url,
  pool_pre_ping=True,  # 죽은 커넥션을 자동으로 감지
  future=True,
)

# 세션 팩토리
SessionLocal = sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=engine,
)
