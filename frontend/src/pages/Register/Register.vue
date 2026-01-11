<template>
  <BoxContainer style="background-color: #FFFFFF; padding: 0px 16px 0px 16px;">    
    <v-row 
      no-gutters
      class="justify-center | pt-12"
    >
      <v-chip variant="outlined" class="header-chip">
        학교 이메일로 가입
      </v-chip>
    </v-row>
    <v-row 
      no-gutters
      class="justify-center | mt-7 | mb-8"
    >
      <v-col cols="12" class="mt-1 | header-title">비슷한 사람들과 가벼운 밥약부터 시작해요.</v-col>
      <v-col cols="12" class="mt-1 | header-subtitle">학교 인증으로 더욱 안전하게 이용해요.</v-col>
    </v-row>

    <v-row no-gutters class="justify-start | label-text">
      사용자 이름
    </v-row>
    <v-row no-gutters class="justify-center | mt-1">
      <v-text-field
        v-model="userName"
        placeholder="username"
        class="inputbox"
        variant="outlined" density="comfortable" rounded="lg" bg-color="#F9FAFB" base-color="#E5E8EB" color="#E5E8EB"
      />
    </v-row>

    <v-row no-gutters class="justify-start | label-text">
      이메일
    </v-row>
    <v-row no-gutters class="justify-center | mt-1">
      <v-text-field
        v-model="userEmail"
        placeholder="email@cau.ac.kr"
        class="inputbox"
        variant="outlined" density="comfortable" rounded="lg" bg-color="#F9FAFB" base-color="#E5E8EB" color="#E5E8EB"
      />
    </v-row>

    <v-row no-gutters class="justify-start | label-text">
      비밀번호
    </v-row>
    <v-row no-gutters class="justify-center | mt-1">
      <v-text-field
        v-model="userPassword"
        placeholder="password"
        :type="showPassword ? 'text' : 'password'"
        :append-inner-icon="showPassword ? 'mdi-eye-outline' : 'mdi-eye-off-outline'"
        @click:append-inner="showPassword = !showPassword"
        class="inputbox"
        variant="outlined" density="comfortable" rounded="lg" bg-color="#F9FAFB" base-color="#E5E8EB" color="#E5E8EB"
      />
    </v-row>
    <v-row no-gutters class="justify-center | mt-4 | mb-4">
      <v-btn
        @click="handleClickBtn('register')"
        variant="outlined"
        class="active-btn"
        :disabled="!active"
        v-if="active"
      >회원가입</v-btn>
      <v-btn
        variant="outlined"
        class="readonly-btn"
        readonly
        v-else
      >회원가입</v-btn>
    </v-row>

    <v-row no-gutters class="justify-center | align-item-center | mt-12">
      <v-col 
        cols="auto" 
        class="info-text | mr-2"
      >
        이미 계정이 있으신가요?
      </v-col>
      <v-col
        cols="auto"
        class="info-text | underline | login-text-link"
        @click="handleClickBtn('gotoLogin')"
      >
        로그인
      </v-col>
    </v-row>
  </BoxContainer>

</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref, watch } from "vue";
import { useRouter, useRoute } from "vue-router";
import BoxContainer from "@/components/BoxContainer.vue";
import { navigateTo } from '@/common/RouterUtil.js';

const emit = defineEmits(['hide-top-appbar', 'hide-bottom-appbar']);
const router = useRouter(); 

const userName = ref('');
const userEmail = ref('');
const userPassword = ref('');

const active = ref(false);
const showPassword = ref(false);

// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-top-appbar');
  emit('hide-bottom-appbar');
});

onUnmounted(() => {

});

watch([userName, userEmail, userPassword], ([newUserName, newUserEmail, newUserPassword]) => {
  // 세 항목 모두 null, undefined, 또는 빈 문자열이 아닐 때만 true
  const isUsernameValid = !!newUserName && newUserName.trim() !== '';
  const isEmailValid = !!newUserEmail && newUserEmail.trim() !== '';
  const isPasswordValid = !!newUserPassword && newUserPassword.trim() !== '';
  
  active.value = isUsernameValid && isEmailValid && isPasswordValid;
}, { immediate: true });

// ----- 함수 정의 ----- //

function handleClickBtn(action) {
  switch (action) {
    case 'gotoLogin':
      navigateTo(router, '/login');
      break;

    case 'register':
      if (active.value) {
        console.log('회원가입 버튼 클릭. 이름:', userName.value, '이메일:', userEmail.value, '비밀번호:', userPassword.value);
        navigateTo(router, '/register/basic');
      } else {
        console.log('입력 필드 미완료로 회원가입 버튼 비활성화');
      }
      break;

    default:
      console.error('알 수 없는 인증 액션 타입:', action);
  }
}

</script>

<style scoped>
.align-item-center {
  align-items: center;
}

.header-title {
  font-size: 16px;
  font-weight: 600;
  text-align: center;
}

.header-subtitle {
  font-size: 15px;
  font-weight: 400;
  text-align: center;
}

.header-chip {
  background-color: #F9FAFB;
  border: 0.7px solid #E5E8EB;
  font-size: 14px;
  font-weight: 400;
  min-height: 38px;
}

.inputbox :deep(.v-input__details) {
  padding-top: 4px !important;
}
.inputbox :deep(.v-icon) {
  color: #8B95A1 !important;
  opacity: 1;
}

.label-text {
  font-size: 14px;
  font-weight: 600;
  color: #364153;
}

.info-text {
  font-size: 16px;
  font-weight: 400;
  cursor: default; 
}

.login-text-link {
  cursor: pointer; 
  text-decoration: underline;
  color: #2F89FC;
  font-size: 16px;
  font-weight: 800;
}

</style>