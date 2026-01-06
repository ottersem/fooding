/**
 * HTTP 요청을 처리하는 클래스
 * 공통 헤더, 베이스 URL, 에러 핸들링 등을 관리합니다.
 */
class HttpClient {
  constructor() {
    this.baseURL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';
    this.timeout = import.meta.env.VITE_API_TIMEOUT || 10000;
    this.defaultHeaders = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    };
  }

  /**
   * Authorization 토큰 설정
   * @param {string} token - 인증 토큰
   */
  setAuthToken(token) {
    if (token) {
      this.defaultHeaders['Authorization'] = `Bearer ${token}`;
    } else {
      delete this.defaultHeaders['Authorization'];
    }
  }

  /**
   * 커스텀 헤더 추가
   * @param {object} headers - 추가할 헤더 객체
   */
  setHeaders(headers) {
    this.defaultHeaders = { ...this.defaultHeaders, ...headers };
  }

  /**
   * 공통 fetch 요청 메서드
   * @param {string} endpoint - API 엔드포인트
   * @param {object} options - fetch 옵션
   * @returns {Promise<any>} - 응답 데이터
   */
  async request(endpoint, options = {}) {
    const url = `${this.baseURL}${endpoint}`;
    
    const config = {
      ...options,
      headers: {
        ...this.defaultHeaders,
        ...options.headers,
      },
    };

    // 타임아웃 설정
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), this.timeout);
    config.signal = controller.signal;

    try {
      console.log(`[HTTP] ${config.method || 'GET'} ${url}`, config.body ? JSON.parse(config.body) : '');
      
      const response = await fetch(url, config);
      clearTimeout(timeoutId);

      // 응답 상태 코드 체크
      if (!response.ok) {
        await this.handleError(response);
      }

      // 응답이 비어있을 경우 처리
      const contentType = response.headers.get('content-type');
      if (contentType && contentType.includes('application/json')) {
        return await response.json();
      }
      
      return await response.text();
    } catch (error) {
      clearTimeout(timeoutId);
      
      if (error.name === 'AbortError') {
        console.error('[HTTP] 요청 타임아웃:', url);
        throw new Error('요청 시간이 초과되었습니다.');
      }
      
      console.error('[HTTP] 요청 실패:', error);
      throw error;
    }
  }

  /**
   * 에러 처리
   * @param {Response} response - fetch 응답 객체
   */
  async handleError(response) {
    let errorMessage = `HTTP ${response.status}: ${response.statusText}`;
    
    try {
      const errorData = await response.json();
      errorMessage = errorData.message || errorData.detail || errorMessage;
    } catch {
      // JSON 파싱 실패 시 기본 메시지 사용
    }

    // 상태 코드별 처리
    switch (response.status) {
      case 400:
        throw new Error(`잘못된 요청입니다: ${errorMessage}`);
      case 401:
        // 인증 실패 시 토큰 제거 및 로그인 페이지로 리다이렉트 처리 가능
        this.setAuthToken(null);
        throw new Error('인증이 필요합니다. 다시 로그인해주세요.');
      case 403:
        throw new Error('접근 권한이 없습니다.');
      case 404:
        throw new Error('요청한 리소스를 찾을 수 없습니다.');
      case 500:
        throw new Error('서버 오류가 발생했습니다.');
      default:
        throw new Error(errorMessage);
    }
  }

  /**
   * API 요청
   * @param {string} method - HTTP 메서드 ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')
   * @param {string} endpoint - API 엔드포인트
   * @param {object} options - 요청 옵션
   * @param {object} options.body - 요청 본문
   * @param {object} options.params - 쿼리 파라미터
   * @param {boolean} options.isFormData - FormData 여부
   * @returns {Promise<any>} - 응답 데이터
   */
  async apiRequest(method, endpoint, { body = null, params = null, isFormData = false } = {}) {
    let url = endpoint;
    
    // 쿼리 파라미터 처리
    if (params) {
      const queryString = new URLSearchParams(params).toString();
      url = `${endpoint}?${queryString}`;
    }

    const options = {
      method: method.toUpperCase(),
    };

    // FormData 처리
    if (isFormData && body) {
      const headers = { ...this.defaultHeaders };
      delete headers['Content-Type'];
      options.headers = headers;
      options.body = body;
    } 
    // 일반 JSON 데이터 처리
    else if (body) {
      options.body = JSON.stringify(body);
    }

    return this.request(url, options);
  }
}

// 싱글톤 인스턴스 생성 및 export
const httpClient = new HttpClient();

export default httpClient;

// ==================== API 함수 정의 ==================== //

// ----- 인증 관련 API ----- //
export async function login(params) {
  const email = params.email;
  const password = params.password;
  const body = {
    email,
    password
  };
  return httpClient.apiRequest('POST', '/api/auth/login', { body });
}

export async function signup(params) {
  const email = params.email;
  const password = params.password;
  const userName = params.userName;
  const major = params.major;
  const grade = params.grade;
  const body = {
    email,
    password,
    user_name: userName,
    major,
    grade
  };
  return httpClient.apiRequest('POST', '/api/auth/signup', { body });
}

export async function logout() {
  return httpClient.apiRequest('POST', '/api/auth/logout');
}

export async function refreshToken(params) {
  const refreshToken = params.refreshToken;
  const body = {
    refresh_token: refreshToken
  };
  return httpClient.apiRequest('POST', '/api/auth/refresh', { body });
}

// ----- 프로필 관련 API ----- //
export async function getMyProfile() {
  return httpClient.apiRequest('GET', '/api/profile/me');
}

export async function getUserProfile(params) {
  const userId = params.userId;
  return httpClient.apiRequest('GET', `/api/profile/${userId}`);
}

export async function updateProfile(params) {
  const major = params.major;
  const grade = params.grade;
  const introText = params.introText;
  const profileImageUrl = params.profileImageUrl;
  const body = {
    major,
    grade,
    intro_text: introText
  };
  if (profileImageUrl) body.profile_image_url = profileImageUrl;
  return httpClient.apiRequest('PUT', '/api/profile/me', { body });
}

export async function uploadProfileImage(params) {
  const imageFile = params.imageFile;
  const body = new FormData();
  body.append('file', imageFile);
  return httpClient.apiRequest('POST', '/api/profile/image', { body, isFormData: true });
}

// ----- 모임 관련 API ----- //
export async function getMeetings(params) {
  const query = params;
  return httpClient.apiRequest('GET', '/api/meetings', { params: query });
}

export async function getMeeting(params) {
  const meetingId = params.meetingId;
  return httpClient.apiRequest('GET', `/api/meetings/${meetingId}`);
}

export async function createMeeting(params) {
  const title = params.title;
  const description = params.description;
  const maxParticipants = params.maxParticipants;
  const meetingTime = params.meetingTime;
  const category = params.category;
  const body = {
    title,
    description,
    max_participants: maxParticipants,
    meeting_time: meetingTime,
    category
  };
  return httpClient.apiRequest('POST', '/api/meetings', { body });
}

export async function updateMeeting(params) {
  const meetingId = params.meetingId;
  const title = params.title;
  const description = params.description;
  const maxParticipants = params.maxParticipants;
  const meetingTime = params.meetingTime;
  const category = params.category;
  const body = {
    title,
    description,
    max_participants: maxParticipants,
    meeting_time: meetingTime,
    category
  };
  return httpClient.apiRequest('PUT', `/api/meetings/${meetingId}`, { body });
}

export async function deleteMeeting(params) {
  const meetingId = params.meetingId;
  return httpClient.apiRequest('DELETE', `/api/meetings/${meetingId}`);
}

export async function joinMeeting(params) {
  const meetingId = params.meetingId;
  return httpClient.apiRequest('POST', `/api/meetings/${meetingId}/join`);
}

export async function leaveMeeting(params) {
  const meetingId = params.meetingId;
  return httpClient.apiRequest('POST', `/api/meetings/${meetingId}/leave`);
}

// ----- 신청 관련 API ----- //
export async function getMyApplications(params) {
  const query = params;
  return httpClient.apiRequest('GET', '/api/applications/me', { params: query });
}

export async function getApplicationsByMeeting(params) {
  const meetingId = params.meetingId;
  return httpClient.apiRequest('GET', `/api/applications/meeting/${meetingId}`);
}

export async function approveApplication(params) {
  const applicationId = params.applicationId;
  return httpClient.apiRequest('POST', `/api/applications/${applicationId}/approve`);
}

export async function rejectApplication(params) {
  const applicationId = params.applicationId;
  return httpClient.apiRequest('POST', `/api/applications/${applicationId}/reject`);
}

// ----- 리뷰 관련 API ----- //
export async function getReviews(params) {
  const query = params;
  return httpClient.apiRequest('GET', '/api/reviews', { params: query });
}

export async function createReview(params) {
  const meetingId = params.meetingId;
  const targetUserId = params.targetUserId;
  const rating = params.rating;
  const comment = params.comment;
  const body = {
    meeting_id: meetingId,
    target_user_id: targetUserId,
    rating,
    comment
  };
  return httpClient.apiRequest('POST', '/api/reviews', { body });
}

export async function updateReview(params) {
  const reviewId = params.reviewId;
  const rating = params.rating;
  const comment = params.comment;
  const body = {
    rating,
    comment
  };
  return httpClient.apiRequest('PUT', `/api/reviews/${reviewId}`, { body });
}

export async function deleteReview(params) {
  const reviewId = params.reviewId;
  return httpClient.apiRequest('DELETE', `/api/reviews/${reviewId}`);
}

// 사용 예시:
// import { getMyProfile, updateProfile, getMeetings, createMeeting } from '@/common/HttpHandler.js';
//
// // 프로필 조회
// const profile = await getMyProfile();
//
// // 프로필 업데이트
// await updateProfile({ major: '예술공학부', grade: '3학년' });
//
// // 모임 목록 조회
// const meetings = await getMeetings({ page: 1, limit: 10 });
//
// // 모임 생성
// await createMeeting({ title: '점심 모임', description: '같이 밥 먹어요' });
