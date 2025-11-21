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
    <v-row no-gutters class="justify-center">
      <v-text-field
        v-model="Username"
        placeholder="username"
        class="inputbox"
        variant="outlined" density="comfortable" rounded="lg" bg-color="#F9FAFB" base-color="#E5E8EB" color="#E5E8EB"
      />
    </v-row>
    <v-row no-gutters class="justify-center">
      <v-text-field
        v-model="Username"
        placeholder="email@cau.ac.kr"
        class="inputbox"
        variant="outlined" density="comfortable" rounded="lg" bg-color="#F9FAFB" base-color="#E5E8EB" color="#E5E8EB"
      />
    </v-row>
    <v-row no-gutters class="justify-center">
      <v-text-field
        v-model="password"
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
        variant="outlined"
        class="active-btn"
      >회원가입</v-btn>
      <v-btn
        variant="outlined"
        class="readonly-btn"
        readonly
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

const emit = defineEmits(['hide-top-appbar']);
const router = useRouter(); 

// v-model 변수 선언
const username = ref('');
const email = ref('');
const password = ref('');
// 비밀번호 보이기/가리기 상태 변수
const showPassword = ref(false);

// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-top-appbar');
});

onUnmounted(() => {

});

// ----- 함수 정의 ----- //

function handleClickBtn(action) {
  switch (action) {
    case 'gotoLogin':
      navigateTo(router, '/login');
      break;

    case 'login':
      console.log('로그인 버튼 클릭. 이메일:', email.value, '비밀번호:', password.value);
      // 로그인 처리 로직
      // 예: loginUser(email.value, password.value);
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
  border: 0.67px solid #E5E8EB;
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