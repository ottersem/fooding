<template>
  <BoxContainer style="background-color: #FFFFFF; padding: 0px 16px 0px 16px;">
    <v-row 
      no-gutters
      class="justify-center | pt-12 | mb-8"
    >
      <v-col cols="12" class="mt-1 | header-title">다시 만나서 반가워요!</v-col>
      <v-col cols="12" class="mt-1 | header-subtitle">학교 이메일로 로그인해주세요.</v-col>
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

    <v-row no-gutters class="justify-space-between | align-item-center | mt-1 | mb-8">
      <v-col cols="auto">
        <v-checkbox
          label="자동로그인"
          hide-details
          density="comfortable"
          bg-color="#CDD1E0"
          color="#CDD1E0"
        />
      </v-col>
      <v-col
        cols="auto"
        class="info-text"
        style="color: #E86969;"
        @click="handleClickBtn('findIdPw')"
      >
        아이디/비밀번호 찾기
      </v-col>

    </v-row>


    <v-row no-gutters class="justify-center | mt-4 | mb-4">
      <v-btn
        @click="handleClickBtn('login')"
        variant="outlined"
        class="active-btn"
        :disabled="!active"
        v-if="active"
      >로그인</v-btn>
      <v-btn
        variant="outlined"
        class="readonly-btn"
        readonly
        v-else
      >로그인</v-btn>
    </v-row>

    <v-row no-gutters class="justify-center | align-item-center | mt-12">
      <v-col 
        cols="auto" 
        class="info-text | mr-2"
      >
        계정이 없으신가요?
      </v-col>
      <v-col
        cols="auto"
        class="info-text | underline | login-text-link"
        @click="handleClickBtn('goToRegister')"
      >
        회원가입
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

const userEmail = ref('');
const userPassword = ref('');

const showPassword = ref(false);
const active = ref(false);

watch([userEmail, userPassword], ([newUserEmail, newUserPassword]) => {
  // 두 항목 모두 null, undefined, 또는 빈 문자열이 아닐 때만 true
  const isEmailValid = !!newUserEmail && newUserEmail.trim() !== '';
  const isPasswordValid = !!newUserPassword && newUserPassword.trim() !== '';
  
  active.value = isEmailValid && isPasswordValid;
}, { immediate: true });


// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-top-appbar');
  emit('hide-bottom-appbar');
});


onUnmounted(() => {

});

// ----- 함수 정의 ----- //

function handleClickBtn(action) {
  switch (action) {
    case 'findIdPw':
      // 아이디/비밀번호 찾기 로직 추가
      break;

    case 'goToRegister':
      navigateTo(router, '/register');
      break;

    case 'login':
      if (active.value) {
        console.log('로그인 버튼 클릭. 이메일:', userEmail.value, '비밀번호:', userPassword.value);
        // 로그인 처리 로직
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