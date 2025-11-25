<template>
    <v-container class="justify-center | pr-4 | pl-4 | pt-0">

      <v-row no-gutters class="justify-center">
        <v-avatar size="96" image="https://placehold.co/96X96"/>
      </v-row>
      <v-row no-gutters class="justify-center">
        <v-icon icon="mdi-camera"/>
      </v-row>

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
        <v-text-field
          v-model="userEmail"
          placeholder="email@cau.ac.kr" 
          class="inputbox"
          variant="outlined" density="comfortable" rounded="lg" bg-color="#F9FAFB" base-color="#E5E8EB" color="#E5E8EB"
        />
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

// ----- 라이프 사이클 ----- //
onMounted(() => {
  // emit('hide-top-appbar');
});

onUnmounted(() => {
  // 필요한 경우 unmounted 시 로직 추가
});


// ----- 함수 정의 ----- //
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
</style>