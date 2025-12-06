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

## Database

### 테이블 목록

```
users

interests

time_slots

user_profiles

user_interests

user_time_slots

groups

group_members

reviews
```

### users – 사용자 기본 정보

| 컬럼명         | 타입          | 제약 조건                     | 설명                 |
| ----------- | ----------- | ------------------------- | ------------------ |
| `id`        | INT         | PK, AUTO INCREMENT, INDEX | 사용자 고유 ID          |
| `username`  | VARCHAR(10) | NOT NULL, UNIQUE          | 닉네임 (10자 제한)       |
| `email`     | VARCHAR(30) | NOT NULL, UNIQUE          | 이메일                |
| `password`  | VARCHAR(30) | NOT NULL                  | 비밀번호 (평문 저장 – 과제용) |
| `is_active` | BOOLEAN     | NOT NULL, DEFAULT TRUE    | 활성화 여부             |

관계

1 : 1 → user_profiles.user_id

1 : N → user_interests.user_id

1 : N → user_time_slots.user_id

1 : N → groups.creator_id

1 : N → group_members.user_id

1 : N → reviews.reviewer_id, reviews.review_ed_id (받은/쓴 리뷰)

### interests – 관심사 마스터

| 컬럼명    | 타입          | 제약 조건                     | 설명     |
| ------ | ----------- | ------------------------- | ------ |
| `id`   | INT         | PK, AUTO INCREMENT, INDEX | 관심사 ID |
| `name` | VARCHAR(20) | NOT NULL                  | 관심사 이름 |
| `code` | VARCHAR(20) | NOT NULL, UNIQUE          | 관심사 코드 |

관계

1 : N → user_interests.interest_id

1 : N → groups.interest_id

### time_slots – 시간대 마스터

| 컬럼명     | 타입          | 제약 조건                     | 설명         |
| ------- | ----------- | ------------------------- | ---------- |
| `id`    | INT         | PK, AUTO INCREMENT, INDEX | 시간대 ID     |
| `label` | VARCHAR(50) | NOT NULL                  | 시간대 라벨(표기) |
| `code`  | VARCHAR(50) | NOT NULL, UNIQUE          | 시간대 코드     |

관계

1 : N → user_time_slots.time_slot_id

1 : N → groups.time_slot_id

### user_profiles – 유저 프로필(전공/학년/소개글)

| 컬럼명                 | 타입           | 제약 조건                     | 설명                       |
| ------------------- | ------------ | ------------------------- | ------------------------ |
| `id`                | INT          | PK, AUTO INCREMENT, INDEX | 프로필 ID                   |
| `user_id`           | INT          | NOT NULL, FK → `users.id` | 연결된 유저 ID                |
| `major`             | VARCHAR(30)  | NULL 허용                   | 전공                       |
| `grade`             | VARCHAR(10)  | NULL 허용                   | 학년/학년 텍스트                |
| `intro_text`        | VARCHAR(100) | NULL 허용                   | 한 줄 소개 (최대 100자)         |
| `profile_image_url` | VARCHAR(255) | NULL 허용                   | 프로필 이미지 URL (지금은 안 써도 됨) |

관계

N : 1 → users.id (실제론 1:1 관계로 사용)

### user_interests – 유저 ↔ 관심사 매핑 (N:M)

| 컬럼명           | 타입  | 제약 조건                         | 설명     |
| ------------- | --- | ----------------------------- | ------ |
| `id`          | INT | PK, AUTO INCREMENT, INDEX     | 매핑 ID  |
| `user_id`     | INT | NOT NULL, FK → `users.id`     | 유저 ID  |
| `interest_id` | INT | NOT NULL, FK → `interests.id` | 관심사 ID |

관계

N : 1 → users

N : 1 → interests

### user_time_slots – 유저 ↔ 시간대 매핑 (N:M)

| 컬럼명            | 타입  | 제약 조건                          | 설명     |
| -------------- | --- | ------------------------------ | ------ |
| `id`           | INT | PK, AUTO INCREMENT, INDEX      | 매핑 ID  |
| `user_id`      | INT | NOT NULL, FK → `users.id`      | 유저 ID  |
| `time_slot_id` | INT | NOT NULL, FK → `time_slots.id` | 시간대 ID |

관계

N : 1 → users

N : 1 → time_slots

### groups – 모임(매칭/소모임) 본체

| 컬럼명                | 타입           | 제약 조건                          | 설명                                |
| ------------------ | ------------ | ------------------------------ | --------------------------------- |
| `id`               | INT          | PK, AUTO INCREMENT, INDEX      | 모임 ID                             |
| `creator_id`       | INT          | NOT NULL, FK → `users.id`      | 방장 유저 ID                          |
| `interest_id`      | INT          | NOT NULL, FK → `interests.id`  | 모임 관심사 ID                         |
| `title`            | VARCHAR(30)  | NOT NULL                       | 모임 제목                             |
| `description`      | VARCHAR(200) | NOT NULL                       | 모임 설명                             |
| `meeting_date`     | DATE         | NOT NULL                       | 모임 날짜                             |
| `time_slot_id`     | INT          | NOT NULL, FK → `time_slots.id` | 모임 시간대 ID                         |
| `place`            | VARCHAR(50)  | NOT NULL                       | 모임 장소                             |
| `max_participants` | INT          | NOT NULL                       | 정원                                |
| `status`           | VARCHAR(10)  | NOT NULL                       | 상태(`RECRUITING/ONGOING/FINISHED`) |
| `open_chat_link`   | VARCHAR(255) | NULL 허용                        | 카카오 오픈채팅 링크 등                     |


관계

N : 1 → users (creator)

N : 1 → interests

N : 1 → time_slots

1 : N → group_members.group_id

1 : N → reviews.group_id

### group_members – 모임 참여자/신청자

| 컬럼명        | 타입          | 제약 조건                      | 설명                                                    |
| ---------- | ----------- | -------------------------- | ----------------------------------------------------- |
| `id`       | INT         | PK, AUTO INCREMENT, INDEX  | 멤버 레코드 ID                                             |
| `group_id` | INT         | NOT NULL, FK → `groups.id` | 속한 모임 ID                                              |
| `user_id`  | INT         | NOT NULL, FK → `users.id`  | 유저 ID                                                 |
| `role`     | VARCHAR(20) | NOT NULL                   | 역할 (`HOST` / `MEMBER`)                                |
| `status`   | VARCHAR(20) | NOT NULL                   | 상태 (`APPLIED` / `ACCEPTED` / `REJECTED` / `CANCELED`) |

관계

N : 1 → groups

N : 1 → users

### reviews – 모임 후기

| 컬럼명            | 타입           | 제약 조건                      | 설명                          |
| -------------- | ------------ | -------------------------- | --------------------------- |
| `id`           | INT          | PK, AUTO INCREMENT, INDEX  | 리뷰 ID                       |
| `group_id`     | INT          | NOT NULL, FK → `groups.id` | 어느 모임에 대한 후기인지              |
| `reviewer_id`  | INT          | NOT NULL, FK → `users.id`  | 작성자 유저 ID                   |
| `review_ed_id` | INT          | NOT NULL, FK → `users.id`  | 대상 유저 ID (논리명: reviewed_id) |
| `score`        | INT          | NOT NULL                   | 1~5 점수                      |
| `comment`      | VARCHAR(100) | NOT NULL                   | 후기 내용                       |

관계

N : 1 → groups

N : 1 → users (reviewer)

N : 1 → users (reviewed)