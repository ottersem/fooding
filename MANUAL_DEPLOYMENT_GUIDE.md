# Render 수동 배포 가이드 (Step-by-Step)

## 에러 해결

`failed to read dockerfile: open Dockerfil: no such file or directory` 에러는 Dockerfile 경로가 잘못 설정된 것입니다.

## 수동 배포 단계

### 1단계: Backend 배포 (FastAPI)

1. [Render 대시보드](https://dashboard.render.com)에 접속
2. **New +** 버튼 클릭
3. **Web Service** 선택
4. GitHub 저장소 선택 또는 연결
5. 다음 설정 입력:

   | 항목 | 값 |
   |------|-----|
   | **Name** | `fooding-backend` |
   | **Region** | Singapore (Asia) 또는 원하는 지역 |
   | **Branch** | `production` (또는 배포할 브랜치) |
   | **Runtime** | `Docker` |
   | **Dockerfile Path** | `backend/Dockerfile` |
   | **Docker Context** | `backend` |

6. **Environment** 탭 → 환경 변수 추가:
   ```
   MYSQL_ROOT_PASSWORD=your_secure_password
   MYSQL_DATABASE=fooding
   DATABASE_URL=mysql://root:your_secure_password@localhost:3306/fooding
   ```

7. **Advanced** → **Port**: `8000`

8. **Create Web Service** 클릭

### 2단계: Frontend 배포 (Vue.js)

1. **New +** 클릭
2. **Web Service** 선택 (또는 **Static Site**)
3. GitHub 저장소 선택
4. 다음 설정 입력:

   | 항목 | 값 |
   |------|-----|
   | **Name** | `fooding-frontend` |
   | **Region** | 백엔드와 동일 지역 |
   | **Branch** | `production` |
   | **Runtime** | `Docker` |
   | **Dockerfile Path** | `frontend/Dockerfile` |
   | **Docker Context** | `frontend` |

5. **Environment** 탭:
   ```
   VITE_API_URL=https://fooding-backend.onrender.com/api
   ```
   (Backend 배포 후 정확한 URL로 변경)

6. **Advanced** → **Port**: `3000`

7. **Create Web Service** 클릭

### 3단계: Database 배포 (MySQL)

#### 옵션 A: Render의 PostgreSQL 사용 (권장)
```
MySQL 대신 PostgreSQL을 사용하면 설정이 더 간단합니다.
```

#### 옵션 B: MySQL Database as a Service

1. **New +** 클릭
2. **MySQL** 선택 (또는 다른 DB 서비스)
3. 설정:
   - **Name**: `fooding-db`
   - **Region**: 백엔드와 동일
   - **MySQL Version**: `8.0`
   - **Database**: `fooding`
   - **Username**: `root`
   - **Password**: 안전한 비밀번호

4. **Create Database** 클릭

5. 제공되는 **Internal Database URL** 복사

### 4단계: 서비스 연결

Backend의 **Environment** 수정:
```
DATABASE_URL=mysql://root:password@host:port/fooding
```

## 주의사항

### ✅ Dockerfile 경로 올바른 예시
- `backend/Dockerfile` ✓
- `frontend/Dockerfile` ✓
- `./backend/Dockerfile` ✓

### ❌ Dockerfile 경로 잘못된 예시
- `Dockerfile` (루트 디렉토리에 없음)
- `Dockerfil` (오타)
- `/backend/Dockerfile` (절대 경로)

### Docker Context 설정

**render.yaml에서 설정한 경우:**
```yaml
dockerContext: ./frontend
```

**수동 배포 시 Render 대시보드:**
- `Docker Context`: `frontend` (또는 `backend`)
- 공란으로 둬도 대부분 자동 감지됨

## 배포 상태 확인

1. 각 서비스의 **Logs** 탭 확인
2. 정상 메시지:
   ```
   Building Docker image
   Starting service
   ```

3. Backend 정상 시작:
   ```
   INFO:     Application startup complete
   INFO:     Uvicorn running on http://0.0.0.0:8000
   ```

## 서비스 URL 확인

배포 완료 후:
- **Frontend**: https://fooding-frontend.onrender.com
- **Backend API**: https://fooding-backend.onrender.com/api
- **Health Check**: https://fooding-backend.onrender.com/api/health

## 문제 해결

### "failed to read dockerfile: open Dockerfil"

**원인**: Dockerfile 경로가 잘못됨

**해결책**:
1. Dockerfile이 존재하는지 확인
   ```bash
   ls backend/Dockerfile
   ls frontend/Dockerfile
   ```

2. Render 대시보드 → 서비스 → **Settings**
3. **Dockerfile Path** 재확인: `backend/Dockerfile`
4. **Redeploy** 클릭

### "Cannot GET /"

Frontend가 실행 중이지만 라우팅 문제
- 로그 확인: https://fooding-frontend.onrender.com/health
- Dockerfile의 `serve` 명령어 확인

### Database 연결 실패

1. Backend 로그 확인
2. DATABASE_URL 환경 변수 확인
3. MySQL 서비스가 실행 중인지 확인

### CORS 오류

Backend의 `app/main.py`에서:
```python
allow_origins=["https://fooding-frontend.onrender.com"]
```

## 자동 배포 활성화

각 서비스 → **Settings** → **Auto-Deploy**
- 선택 사항: `Yes` (main/production 브랜치에 푸시 시 자동 배포)

## Render.yaml 대신 수동 배포하는 이유

- render.yaml 문법 오류 시 해결 용이
- 각 서비스를 개별적으로 미세 조정 가능
- 환경 변수를 한곳에서 관리 가능
