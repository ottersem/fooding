# FastAPI 애플리케이션의 진입점

from fastapi import FastAPI
from app.api import api_router
from core.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

# 앱 시작 시 테이블이 없으면 생성
def init_models():

  Base.metadata.create_all(bind=engine)


init_models()

app = FastAPI(
  title="Fooding Backend (SQLAlchemy)",
)

# 모든 API는 /api 아래에 위치하게 함
app.include_router(api_router, prefix="/api")

#CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
  # 단순 헬스 체크용 엔드포인트임
  return {"status": "ok"}
