import { createRouter, createWebHistory, createWebHashHistory } from 'vue-router';
import { defineAsyncComponent } from "vue";

/* INFO rule
 * path
    1. camelCase 로 작성
    2. 파일 path와 동일하게 작성 예) folder1/folder2/my-file
 * name
    1. 파일명 작성 -> PascalCase 사용.
 * component
    1. 파일 path 작성
 */

const routes = [
  {
    path: '/',
    redirect: '/home' // Redirect root path to dashboard
  },
  {
    path: '/home',
    name: 'Home',
    component: () => import(/* webpackChunkName: "home" */ "@/pages/Home.vue")
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import(/* webpackChunkName: "login" */ "@/pages/Auth/Login.vue")
  },
  {
    path: '/my-page',
    name: 'MyPage',
    component: () => import(/* webpackChunkName: "my-page" */ "@/pages/Auth/MyPage.vue")
  },
  {
    path: '/user-profile',
    name: 'UserProfile',
    component: () => import(/* webpackChunkName: "user-profile" */ "@/pages/Auth/UserProfile.vue")
  },
  {
    path: '/group-detail',
    name: 'GroupDetail',
    component: () => import(/* webpackChunkName: "group-detail" */ "@/pages/Group/GroupDetail.vue")
  },
  {
    path: '/group-list',
    name: 'GroupList',
    component: () => import(/* webpackChunkName: "group-list" */ "@/pages/Group/GroupList.vue")
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import(/* webpackChunkName: "register" */ "@/pages/Register/Register.vue")
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: () => import(/* webpackChunkName: "sign-up" */ "@/pages/Auth/SignUp.vue")
  },
];

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
});

export default router;
export { routes }