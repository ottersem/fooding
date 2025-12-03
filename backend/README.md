## 디렉토리 구조

```text
backend/
├─ app/                            # FastAPI 앱 로직 전체
│  ├─ main.py                      # FastAPI 엔트리포인트 / 라우터 등록 / 앱 초기화
│  ├─ api/                         # API 엔드포인트(라우터) 모음
│  │  ├─ auth_router.py            # 로그인/회원가입 API
│  │  ├─ profile_router.py         # 프로필 조회/수정 API
│  │  ├─ meeting_router.py         # 모임 생성/조회/수정/삭제 API
│  │  ├─ application_router.py     # 모임 신청/취소/승인/거절 API
│  │  └─ review_router.py          # 후기 작성/조회 API
│  │
│  ├─ schemas/                     # Pydantic 요청/응답 스키마
│  │  ├─ auth_schema.py            # 로그인/회원가입 요청·응답 모델
│  │  ├─ profile_schema.py         # 프로필 조회·수정 모델
│  │  ├─ meeting_schema.py         # 모임 생성·수정·조회 모델
│  │  ├─ application_schema.py     # 신청/승인 등 신청 관련 모델
│  │  └─ review_schema.py          # 후기 요청/응답 모델
│  │
│  ├─ services/                    # 서비스 레이어(비즈니스 로직)
│  │  ├─ auth_service.py           # 로그인/회원가입 처리 로직
│  │  ├─ profile_service.py        # 프로필 조회/수정 비즈니스 로직
│  │  ├─ meeting_service.py        # 모임 처리 로직(생성/조회/수정/삭제)
│  │  ├─ application_service.py    # 신청 처리 로직(신청/승인/거절)
│  │  └─ review_service.py         # 후기 작성/조회 처리 로직
│  │
│  ├─ deps/                        # FastAPI 의존성 모듈
│  │  ├─ db_dep.py                 # DB 세션 제공(get_db)
│  │  └─ auth_dep.py               # 헤더 기반 인증(get_current_user)
│  │
│  └─ utils/                       # 공용 유틸성 함수 모음
│     ├─ pagination.py             # page/size 기반 offset 계산 유틸
│     └─ time_utils.py             # 시간 관련 유틸(현재는 dummy)
│
├─ core/                           # DB, 환경설정, ORM 모델
│  ├─ config.py                    # 환경 변수(.env) 로드 / DB URL 생성
│  ├─ database.py                  # SQLAlchemy engine + SessionLocal
│  ├─ models.py                    # ORM 모델(User, Group 등 전체 테이블 정의)
│  ├─ db/
│  │  └─ docker-compose.yml        # MySQL DB 컨테이너 실행 설정 파일
│
├─ static/
│  └─ README.md                    # 정적 파일(현재 비어있음)
│
├─ requirements.txt                # FastAPI/SQLAlchemy 의존성 패키지 목록
└─ README.md                       # 백앤드 설명 문서
```

## 환경변수 파일

```
backend/.env,   
backend/core/db/.env
```

## Auth

| 메서드  | 경로                 | 설명   | Body            | 응답               |
| ---- | ------------------ | ---- | --------------- | ---------------- |
| POST | `/api/auth/signup` | 회원가입 | `SignUpRequest` | `SignUpResponse` |
| POST | `/api/auth/login`  | 로그인  | `LogInRequest`  | `LogInResponse`  |


## profile

| 메서드 | 경로                                | 설명       | 헤더        | 응답                    |
| --- | --------------------------------- | -------- | --------- | --------------------- |
| GET | `/api/profiles/me`                | 내 프로필 조회 | X-User-Id | ProfileInfo           |
| PUT | `/api/profiles/me`                | 내 프로필 수정 | X-User-Id | ProfileInfo           |
| GET | `/api/profiles/me/review_summary` | 후기 요약    | X-User-Id | ReviewSummaryResponse |


## meeting

| 메서드    | 경로                           | 설명             | 헤더        | Body                  | 응답                   |
| ------ | ---------------------------- | -------------- | --------- | --------------------- | -------------------- |
| GET    | `/api/meetings/main_list`    | 메인 목록          | X-User-Id | -                     | List[MeetingSummary] |
| POST   | `/api/meetings`              | 모임 생성          | X-User-Id | MeetingCreateRequest  | MeetingDetail        |
| GET    | `/api/meetings/{id}`         | 상세 조회          | X-User-Id | -                     | MeetingDetail        |
| PUT    | `/api/meetings/{id}`         | 수정             | X-User-Id | MeetingUpdateRequest  | MeetingDetail        |
| DELETE | `/api/meetings/{id}`         | 삭제             | X-User-Id | -                     | {detail:"deleted"}   |
| POST   | `/api/meetings/{id}/finish`  | 종료처리           | X-User-Id | -                     | MeetingDetail        |
| POST   | `/api/meetings/{id}/confirm` | 오픈채팅 / 진행상태 변경 | X-User-Id | MeetingConfirmRequest | MeetingDetail        |
| GET    | `/api/meetings/my_list`      | 내가 참여한 모임 목록   | X-User-Id | -                     | List[MeetingSummary] |


## Application

| 메서드  | 경로                                          | 설명            | 헤더        | Body | 응답                   |
| ---- | ------------------------------------------- | ------------- | --------- | ---- | -------------------- |
| POST | `/api/applications/meetings/{id}/apply`     | 신청            | X-User-Id | -    | applied              |
| POST | `/api/applications/meetings/{id}/cancel`    | 신청 취소         | X-User-Id | -    | canceled             |
| GET  | `/api/applications/meetings/{id}`           | 신청 현황 조회(호스트) | X-User-Id | -    | ApplicationsResponse |
| POST | `/api/applications/{application_id}/accept` | 승인            | X-User-Id | -    | accepted             |
| POST | `/api/applications/{application_id}/reject` | 거절            | X-User-Id | -    | rejected             |


## Review

| 메서드  | 경로                           | 설명       | 헤더        | Body                | 응답                       |
| ---- | ---------------------------- | -------- | --------- | ------------------- | ------------------------ |
| POST | `/api/reviews/meetings/{id}` | 후기 작성/수정 | X-User-Id | ReviewCreateRequest | List[ReviewItemResponse] |
| GET  | `/api/reviews/my_written`    | 내가 쓴 후기  | X-User-Id | -                   | MyWrittenReviewsResponse |



## 주요 모델, 변수명

- user 관련

| 개념    | 변수명             |
| ----- | --------------- |
| 유저 ID | `user_id`       |
| 이름    | `username`      |
| 이메일   | `email`         |
| 전공    | `major`         |
| 학년    | `grade`         |
| 소개글   | `intro_text`    |
| 관심사   | `interest_ids`  |
| 시간대   | `time_slot_ids` |


- meeting 관련

| 개념    | 변수명                 |
| ----- | ------------------- |
| 모임 ID | `id` / `meeting_id` |
| 제목    | `title`             |
| 설명    | `description`       |
| 관심사   | `interest_id`       |
| 시간대   | `time_slot_id`      |
| 날짜    | `meeting_date`      |
| 장소    | `place`             |
| 정원    | `max_participants`  |



## 실행 방법

```bash
cd backend/core/db
docker compose up -d

의존성 설치
pip install -r requirements.txt

FastAPI 실행
uvicorn app.main:app --reload
```
swagger 문서 주소 : http://localhost:8000/docs


## 버전정보

Python 3.11+ (본인 가상환경은 3.12 ver )

FastAPI 0.109+

SQLAlchemy 2.x

MySQL 8.0

Docker Engine 24+

Uvicorn 0.30+

## CORS 설정

프론트엔드가 브라우저 환경에서 실행되므로, CORS 허용이 필요합니다.

FastAPI에서는 다음 설정을 통해 모든 출처의 요청을 개발 환경에서 허용합니다:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # 개발 환경 전체 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

```

## 인증 전체 흐름

```
[1] 로그인 요청
      ↓
[2] backend: 이메일/비밀번호 확인
      ↓
[3] backend: user_id 반환
      ↓
[4] front: user_id localStorage 등에 저장
      ↓
[5] front: 모든 API 호출시 X-User-Id: user_id 헤더로 추가
      ↓
[6] backend: X-User-Id 로 인증 및 권한 체크
```
