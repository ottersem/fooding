<template>
  <v-app class="background">
    <v-app-bar 
      app color="#FFFFFF" flat
      v-if="showTopNav"
    >
      <v-row no-gutters class="justify-space-between | align-center | header-container">
        <v-col cols="auto" class="pl-2">
            <v-btn
              icon="mdi-chevron-left" 
              variant="text" density="comfortable"
              @click="handleClickBtn('goToBack')"
            ></v-btn>
        </v-col>

        <v-col cols="auto" class="nav-text">
          {{ 'asdf' }}
        </v-col>

        <v-col cols="auto" class="nav-icon | pr-2">
            <v-btn
              icon="$cus-profile" 
              variant="outlined" density="comfortable" rounded="circle" base-color="#F3F4F6" color="#F3F4F6"
              @click="handleClickBtn('goToMypage')"
            ></v-btn>
        </v-col>
      </v-row>
    </v-app-bar>

    <v-main>
      <router-view
        @hide-top-appbar="hideTopNav"
        @hide-bottom-appbar="hideBotNav"
      ></router-view>
    </v-main>

      <v-slide-y-reverse-transition>
      <div v-if="isFabOpen && showBotNav" class="fab-menu-container">
        <div 
          v-for="(item, index) in fabMenus" 
          :key="index"
          class="fab-menu-item"
          @click="handleMenuClick(item.action)"
        >
          <div class="fab-icon-box">
            <v-icon color="#FFFFFF" size="20">{{ item.icon }}</v-icon>
          </div>
          <span class="fab-text">{{ item.text }}</span>
        </div>
      </div>
    </v-slide-y-reverse-transition>
    <v-btn
      v-if="showBotNav"
      class="floating-btn"
      color="#FF6129"
      elevation="4"
      icon="mdi-plus"
      @click="toggleFab"
    >
      <v-icon 
        color="#FFFFFF" size="32" 
        :icon="isFabOpen ? 'mdi-close' : '$cus-fooding'"
        :style="{ transform: isFabOpen ? 'rotate(90deg)' : 'rotate(0deg)', transition: '0.3s' }"
      />
    </v-btn>
  </v-app>

  <!-- 다이얼로그 -->
  <v-dialog v-model="dialog.dialogActive" width="100%">
    <v-card style="padding: 24px 16px; border-radius: 24px;">
      <v-btn 
        icon="mdi-close" variant="text" size="small"
        v-if="!dialog.isOneBtn"
        @click="dialog.dialogActive = false"
        style="position: absolute; top: 12px; right: 12px; color: #6B7280; z-index: 10;"
      />

      <v-card-title>
        <v-row no-gutters class="align-center | justify-center">
          <v-icon size="64" color="#FF6129" icon="$cus-complete-icon"/>
        </v-row>
        <v-row no-gutters class="align-center | justify-center | mt-3"
          style="color: #101828; font-size: 20px; font-weight: 400; letter-spacing: -0.45px;"
        >
          {{ dialog.title }}
        </v-row>
      </v-card-title>

      <v-card-text style="padding: 0px; margin-bottom: 12px;">
        <v-row no-gutters
        style="justify-content: center; text-align: center; color: #6A7282; font-size: 14px; font-weight: 400; letter-spacing: -0.15px;"
        v-html="dialog.text"/>
      </v-card-text>

      <template v-slot:actions>
          <v-btn class="active-btn" style="border-radius: 16px;" variant="outlined" @click="dialog.okButton" :loading="isSubmitting">{{ dialog.okText }}</v-btn>
      </template>
    </v-card>
  </v-dialog>
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref, watch } from "vue";
import { useRouter, useRoute } from "vue-router";
import { navigateTo } from '@/common/RouterUtil.js';

// 라우터 인스턴스 가져오기
const router = useRouter();
const route = useRoute(); // (추가) 현재 라우트 정보 가져오기

// 네비게이션 표시 상태
const showTopNav = ref(true);
const showBotNav = ref(true);

// [추가] FAB 상태 및 메뉴 데이터
const isFabOpen = ref(false);
const fabMenus = [
  { text: '내 모임', icon: '$cus-people', action: 'myMeeting' },
  { text: '모임 만들기', icon: 'mdi-plus', action: 'createMeeting' },
  { text: '내 후기', icon: '$cus-document', action: 'myReview' },
  { text: '프로필', icon: '$cus-profile', action: 'profile' },
];

const dialog = ref({
  title: '',
  text: '',
  isActive: false,
  isOneBtn: false,
  okText: '확인',
  okButton() {}
});


// ----- 라이프 사이클 ----- //
onMounted(() => {
  console.log(import.meta.env)
});

onUnmounted(() => {

});

watch(
  () => route.path, // 현재 경로(path)를 감시
  (newPath, oldPath) => {
    showTopNav.value = true;
    showBotNav.value = true;

    // 페이지 이동 시 메뉴 닫기
    isFabOpen.value = false;
  }
);

// ----- 함수 정의 ----- //
function initSurvey() {
  localStorage.setItem('appInitialized', 'true');
  localStorage.setItem('userSurvey', JSON.stringify(survey.value));
  localStorage.removeItem('surveyId');
  surveyId.value = null;

  console.log("set localStorage appInitialized:", localStorage.getItem('appInitialized'))
  console.log("set localStorage userSurvey:", localStorage.getItem('userSurvey'))
}

// 상단 앱 바 숨기기
function hideTopNav() {
  showTopNav.value = false;
}

// 하단 앱 바 숨기기
function hideBotNav() {
  showBotNav.value = false;
}

// FAB 토글 함수
function toggleFab() {
  isFabOpen.value = !isFabOpen.value;
}

// 메뉴 클릭 핸들러
function handleMenuClick(action) {
  console.log('Menu Clicked:', action);
  isFabOpen.value = false; // 클릭 후 닫기
  
  // 액션에 따른 라우팅 처리 예시
  switch (action) {
    case 'createMeeting':
      // navigateTo(router, '/meeting/create');
      break;
    case 'profile':
      navigateTo(router, '/my-page');
      break;
  }
}

// 버튼 클릭 이벤트 핸들러
function handleClickBtn(action) {
  switch (action) {
    case 'goToMypage':
      navigateTo(router, '/my-page');
      break;

    case 'goToBack':
      navigateTo(router, '/');
      break;

    default:
      console.error('알 수 없는 인증 액션 타입:', action);
  }
}

function openDialog(title, text, onConfirm, isOneBtn, okText) {
  dialog.value.title = title;
  dialog.value.text = text;
  dialog.value.okButton = onConfirm;
  dialog.value.dialogActive = true;
  dialog.value.isOneBtn = isOneBtn || false;
  dialog.value.okText = okText || '확인';
}

</script>

<style scoped>
.floating-btn {
  position: fixed !important;
  bottom: 24px;
  right: 24px;
  width: 56px !important;
  height: 56px !important;
  border-radius: 50% !important;
  z-index: 100;
}

/* FAB 메뉴 컨테이너 */
.fab-menu-container {
  position: fixed;
  bottom: 96px;
  right: 24px;
  display: flex;
  flex-direction: column-reverse; /* 아래에서 위로 쌓이게 */
  gap: 12px;
  z-index: 99;
  align-items: flex-end; /* 오른쪽 정렬 */
}

/* 개별 메뉴 아이템 (칩 스타일) */
.fab-menu-item {
  display: flex;
  align-items: center;
  background-color: #FFFFFF;
  padding: 8px;
  border-radius: 30px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  cursor: pointer;
  transition: transform 0.2s;
  min-width: 140px;
}

.fab-menu-item:active {
  transform: scale(0.95);
}

.fab-icon-box {
  width: 32px;
  height: 32px;
  background-color: #FF6129;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 12px;
}

.fab-text {
  font-size: 14px;
  font-weight: 500;
  color: #111827;
}
</style>
