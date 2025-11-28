<template>
    <v-container 
      class="justify-center | mb-12"
      style="background-color: #FFFFFF; height: 100%;"
    >

      <v-row no-gutters class="justify-center | pt-6 | pb-8">
        <v-avatar class="profile-img-frame" size="96" image="https://placehold.co/96X96"/>
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
          v-model="userEmail"
          placeholder="email@cau.ac.kr" 
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
        한줄 소개
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-textarea
          placeholder="예: ENTJ, 1학년인데 취업에 관심 있는 사람들과 대화 나누고 싶어요" 
          hide-details
          variant="outlined" density="comfortable" rounded="lg" bg-color="#F9FAFB" base-color="#E5E8EB" color="#E5E8EB"
          class="inputbox"
          v-model="userDesc"
          @input="handleInputChange('input')"
          :maxlength="maxCharLength"
        />
      </v-row>
      <v-row no-gutters class="justify-end | label-text-small | mt-1 | mb-2">
        {{ userDesc.length }}/{{ maxCharLength }} 
      </v-row>

      <v-row no-gutters class="justify-start | label-text">
        관심분야
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
        희망시간
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-text-field
          v-model="userEmail"
          placeholder="email@cau.ac.kr" 
          class="inputbox"
          variant="outlined" density="comfortable" rounded="lg" bg-color="#F9FAFB" base-color="#E5E8EB" color="#E5E8EB"
        />
      </v-row>
    </v-container>

    <SaveFooter
      @go-next="handleClickBtn('goToNext')"
      :active="active"
    />
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref, watch, computed } from "vue";
import { useRouter, useRoute } from "vue-router";
import { navigateTo } from '@/common/RouterUtil.js';
import SaveFooter from "@/components/SaveFooter.vue";


const router = useRouter(); 

const emit = defineEmits(['hide-top-appbar']);

const active = ref(false);

const userDesc = ref("");
const maxCharLength = 100; // 최대 글자수 상수로 정의

// ----- 라이프 사이클 ----- //
onMounted(() => {
  // emit('hide-top-appbar');
});

onUnmounted(() => {
  // 필요한 경우 unmounted 시 로직 추가
});


// ----- 함수 정의 ----- //
function handleInputChange(action) {
  switch (action) {
    case 'input':
      const length = userDesc.value?.length ?? 0;

      if (length > maxCharLength) {
          userDesc.value = userDesc.value.slice(0, maxCharLength);
      }
      
      active.value = userDesc.value.length > 0 && userDesc.value.length <= maxCharLength;
      break;
  }
}

function handleClickBtn(action) {
  switch (action) {
    case 'goToProfile':
      navigateTo(router, '/user-profile');
      break;

    case 'goToReview':
      // navigateTo(router, '/user-profile');
      break;

    case 'logout':
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

.profile-img-frame {
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