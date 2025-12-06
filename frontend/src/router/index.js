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
    redirect: '/group' // Redirect root path to dashboard
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
    path: '/user',
    name: 'UserMenu',
    component: () => import(/* webpackChunkName: "user-menu" */ "@/pages/Auth/UserMenu.vue")
  },
  {
    path: '/user/profile',
    name: 'UserProfile',
    component: () => import(/* webpackChunkName: "user-profile" */ "@/pages/Auth/UserProfile.vue")
  },
  {
    path: '/user/review',
    name: 'UserReview',
    component: () => import(/* webpackChunkName: "user-review" */ "@/pages/Auth/UserReview.vue")
  },
  {
    path: '/group',
    name: 'GroupList',
    component: () => import(/* webpackChunkName: "group-list" */ "@/pages/Group/GroupList.vue")
  },
  {
    path: '/group/detail',
    name: 'GroupDetail',
    component: () => import(/* webpackChunkName: "group-detail" */ "@/pages/Group/GroupDetail.vue")
  },
  {
    path: '/group/create',
    name: 'GroupCreate',
    component: () => import(/* webpackChunkName: "group-create" */ "@/pages/Group/GroupCreate.vue")
  },
  {
    path: '/group/user',
    name: 'GroupUser',
    component: () => import(/* webpackChunkName: "group-user" */ "@/pages/Group/GroupUser.vue")
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import(/* webpackChunkName: "sign-up" */ "@/pages/Register/Register.vue")
  },
  {
    path: '/register/desc',
    name: 'RegisterDesc',
    component: () => import(/* webpackChunkName: "register-desc" */ "@/pages/Register/RegisterDesc.vue")
  },
  {
    path: '/register/basic',
    name: 'RegisterBasic',
    component: () => import(/* webpackChunkName: "register-basic" */ "@/pages/Register/RegisterBasic.vue")
  },
  {
    path: '/register/keyword',
    name: 'RegisterKeyword',
    component: () => import(/* webpackChunkName: "register-keyword" */ "@/pages/Register/RegisterKeyword.vue")
  },
  {
    path: '/register/time',
    name: 'RegisterTime',
    component: () => import(/* webpackChunkName: "register-time" */ "@/pages/Register/RegisterTime.vue")
  },
];

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
});

export default router;
export { routes }