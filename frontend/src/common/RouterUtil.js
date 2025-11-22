/**
 * 주어진 경로(path)로 라우팅하는 유틸리티 함수
 * @param {object} router Vue Router 인스턴스 (useRouter()의 반환 값)
 * @param {string} path 이동할 페이지 경로 (예: '/auth/sign-up', '/main')
 */
export function navigateTo(router, path) {
  if (router && path) {
    console.log(`[Router Util] Navigating to: ${path}`);
    router.push(path);
  } else {
    console.error("[Router Util] Router 인스턴스 또는 경로(path)가 유효하지 않습니다.");
  }
}