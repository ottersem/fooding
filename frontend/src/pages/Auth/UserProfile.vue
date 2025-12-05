<template>
    <v-container 
      class="justify-center | mb-12"
      style="background-color: #FFFFFF; height: 100%;"
    >

      <v-row no-gutters class="justify-center | pt-6 | pb-8">
        <v-avatar class="userData-img-frame" size="96" :image="userData.profileImageUrl"/>
      </v-row>
      <!-- TODO img button -->
      <!-- <v-row no-gutters class="justify-center | pb-8">
        <v-icon icon="mdi-camera"/>
      </v-row> -->

      <v-row no-gutters class="justify-start | label-text">
        이름
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-text-field
          v-model="userData.userName"
          placeholder="이름을 입력하세요" 
          class="inputbox"
          variant="outlined" density="comfortable" rounded="lg" bg-color="#F9FAFB" base-color="#E5E8EB" color="#E5E8EB"
        />
      </v-row>

      <v-row no-gutters class="justify-start | label-text">
        전공
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-text-field
          v-model="userData.major"
          placeholder="예: 소프트웨어학부" 
          class="inputbox"
          variant="outlined" density="comfortable" rounded="lg" bg-color="#F9FAFB" base-color="#E5E8EB" color="#E5E8EB"
        />
      </v-row>

      <v-row no-gutters class="justify-start | label-text">
        학년
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-text-field
          v-model="userData.grade"
          placeholder="예: 3학년" 
          class="inputbox"
          variant="outlined" density="comfortable" rounded="lg" bg-color="#F9FAFB" base-color="#E5E8EB" color="#E5E8EB"
        />
      </v-row>

      <v-row no-gutters class="justify-start | label-text">
        이메일
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-text-field
          v-model="userData.email"
          placeholder="email@cau.ac.kr" 
          class="inputbox"
          variant="outlined" density="comfortable" rounded="lg" bg-color="#F9FAFB" base-color="#E5E8EB" color="#E5E8EB"
        />
      </v-row>

      <v-row no-gutters class="justify-start | label-text">
        한줄 소개
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-textarea
          v-model="userData.introText"
          placeholder="예: ENTJ, 1학년인데 취업에 관심 있는 사람들과 대화 나누고 싶어요" 
          hide-details
          variant="outlined" density="comfortable" rounded="lg" bg-color="#F9FAFB" base-color="#E5E8EB" color="#E5E8EB"
          class="inputbox"
          @input="handleInputChange('input')"
          :maxlength="maxCharLength" max-rows="5" auto-grow
        />
      </v-row>
      <v-row no-gutters class="justify-end | label-text-small | mt-1 | mb-2">
        {{ userData.introText.length }}/{{ maxCharLength }} 
      </v-row>

      <v-row no-gutters class="justify-start | label-text">
        관심분야
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-text-field
          v-model="userData.interests"
          placeholder="예: IT, 창업, 여행" 
          class="inputbox"
          variant="outlined" density="comfortable" rounded="lg" bg-color="#F9FAFB" base-color="#E5E8EB" color="#E5E8EB"
        />
      </v-row>

      <v-row no-gutters class="justify-start | label-text">
        희망시간
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-text-field
          v-model="userData.preferredTime"
          placeholder="예: 평일 저녁, 주말 오후" 
          class="inputbox"
          variant="outlined" density="comfortable" rounded="lg" bg-color="#F9FAFB" base-color="#E5E8EB" color="#E5E8EB"
        />
      </v-row>
    </v-container>

    <SaveFooter
      @go-next="handleClickBtn('saveProfile')"
      :active="active"
    />
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref } from "vue";
import { useRouter } from "vue-router";
import { navigateTo } from '@/common/RouterUtil.js';
import SaveFooter from "@/components/SaveFooter.vue";

const router = useRouter(); 
const emit = defineEmits(['hide-bottom-appbar']);

const active = ref(false);
const maxCharLength = 100; // 최대 글자수 상수로 정의

// [수정] user_profiles 테이블 컬럼 기반 CamelCase 변수 정의
const userData = ref({
    id: null,               // id
    userId: null,           // user_id
    userName: '',           // (UI용) 이름
    email: '',              // (UI용) 이메일
    major: '',              // major
    grade: '',              // grade
    introText: '',          // intro_text
    profileImageUrl: 'https://placehold.co/96X96', // profile_image_url
    interests: '',          // (UI용) 관심분야
    preferredTime: ''       // (UI용) 희망시간
});

// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-bottom-appbar');
});

onUnmounted(() => {
  // 필요한 경우 unmounted 시 로직 추가
});

// ----- 함수 정의 ----- //
function handleInputChange(action) {
  switch (action) {
    case 'input':
      const text = userData.value.introText;
      const length = text?.length ?? 0;

      if (length > maxCharLength) {
        userData.value.introText = text.slice(0, maxCharLength);
      }
      
      // 필수값 체크 로직 (필요시 조건 추가)
      active.value = length > 0 && length <= maxCharLength;
      break;
  }
}

function handleClickBtn(action) {
  switch (action) {
    case 'saveProfile':
      // 저장 로직 수행 후 이동
      console.log("저장할 프로필 데이터:", userData.value);
      break;

    default:
      console.error('알 수 없는 액션 타입:', action);
  }
}
</script>

<style scoped>
.menu-btn {
  min-height: 56px; 
  border: 0.7px solid #F3F4F6;
  background-color: #FFFFFF;
  color: #364153;
  
  justify-content: space-between;
  padding-left: 16px;
  padding-right: 16px;
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

.label-text-small {
  font-size: 12px;
  font-weight: 400;
  color: #364153;
}

.userData-img-frame {
  border: 1.35px solid #E5E7EB;
}
/* 
.img-btn {
  width: 100%;
  height: 48px;
  min-height: 48px;
  background-color: #FF6129;
  border: 0px;
  border-radius: 10px;
  color: #FFFFFF;
  font-size: 16px;
  font-weight: 600;
  letter-spacing: -0.15px;
} */
</style>