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
              icon="$cus-profile-icon" 
              variant="outlined" density="comfortable" rounded="circle" base-color="#F3F4F6" color="#F3F4F6"
              @click="handleClickBtn('goToMypage')"
            ></v-btn>
        </v-col>

      </v-row>
    </v-app-bar>

    <v-main>
      <router-view
        @hide-top-appbar="hideTopNav"
      ></router-view>
    </v-main>

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
  () => route.path, // 현재 경로(path)를 감시합니다.
  (newPath, oldPath) => {
    showTopNav.value = true;
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

// 버튼 클릭 이벤트 핸들러
function handleClickBtn(action) {
  switch (action) {
    case 'goToMypage':
      navigateTo(router, '/myPage');
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

</style>
