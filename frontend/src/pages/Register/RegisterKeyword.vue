<template>
    <ProgressHeader 
      @go-back="handleClickBtn('goToBack')"
      :totalSteps="4" :currentStep="2"
    />

    <v-row no-gutters class="justify-center | pr-4 | pl-4">
      <v-col cols="12">
        <RegisterHeader :title="title" :desc="desc"/>
      </v-col>
  
      <v-col cols="12" class="justify-center | mt-4 | mb-4">
        <v-btn
          variant="outlined"
          class="active-btn"
          @click="handleClickBtn('goToNext')"
        >다음</v-btn>
      </v-col>
    </v-row>
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref, watch } from "vue";
import { useRouter, useRoute } from "vue-router";
import RegisterHeader from "@/components/RegisterHeader.vue";
import { navigateTo } from '@/common/RouterUtil.js';
const router = useRouter(); 

const emit = defineEmits(['hide-top-appbar']);

const title = "관심 있는 주제를 선택해주세요 (최대 2개)";
const desc = "비슷한 관심사를 가진 사람과 연결될 확률이 높아져요";

// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-top-appbar');
});

onUnmounted(() => {

});

// ----- 함수 정의 ----- //
function handleClickBtn(action) {
  switch (action) {
    case 'goToBack':
      navigateTo(router, '/register/detail');
      break;

    case 'goToNext':
      navigateTo(router, '/register/time');
      break;

    default:
      console.error('알 수 없는 액션 타입:', action);
  }
}

</script> 

<style scoped>
.register-detail {
  padding: 20px;
  text-align: center;
}

.register-detail h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

.register-detail p {
  font-size: 16px;
  color: #666;
  margin-bottom: 30px;
}

.button-group {
  display: flex;
  gap: 10px;
  justify-content: center;
}

.next-button {
  padding: 12px 30px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.next-button:hover {
  background-color: #0056b3;
}
</style>