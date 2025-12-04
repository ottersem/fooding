/**
 * 주어진 경로(path)로 라우팅하는 유틸리티 함수
 * @param {object} router Vue Router 인스턴스 (useRouter()의 반환 값)
 * @param {string} path 이동할 페이지 경로 (예: '/auth/sign-up', '/main')
 * @param {object} query 쿼리 파라미터 객체 (예: { id: 1, name: 'test' })
 */
export function navigateTo(router, path, query = null) {
  if (router && path) {
    const destination = query ? { path, query } : path;
    console.log(`[Router Util] Navigating to: ${path}`, query ? `with query: ${JSON.stringify(query)}` : '');
    router.push(destination);
  } else {
    console.error("[Router Util] Router 인스턴스 또는 경로(path)가 유효하지 않습니다.");
  }
}