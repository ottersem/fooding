<template>
    <ProgressHeader 
      @go-back="handleClickBtn('goToBack')"
      :totalSteps="4" :currentStep="4"
    />

    <v-container class="justify-center | pr-4 | pl-4 | pt-0">
      <RegisterHeader :title="title" :desc="desc"/>

      <v-row no-gutters class="justify-center">
        <v-textarea
          placeholder="예: ENTJ, 1학년인데 취업에 관심 있는 사람들과 대화 나누고 싶어요" 
          hide-details
          variant="outlined" density="comfortable" rounded="lg" bg-color="#FFFFFF" base-color="#E5E8EB" color="#E5E8EB"
          class="inputbox"
          v-model="userDesc"
          @input="handleInputChange('input')"
          :maxlength="maxCharLength"
        />
      </v-row>
      <v-row no-gutters class="justify-end | label-text-small | mt-1">
        {{ userDesc.length }}/{{ maxCharLength }} 
      </v-row>

      <v-row no-gutters class="justify-start | label-text | mt-10">
        💡 이런 내용을 추천해요
      </v-row>
      <v-row 
          v-for="(text, index) in recmList" :key="index"
          cols="12" class="recm-item | mt-2" no-gutters
          :style="{ cursor: 'default' }" 
      >
        {{ text }}
      </v-row>

    </v-container>

    <ProgressFooter
      @go-next="handleClickBtn('goToNext')"
      :active="active"
    />
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref, watch } from "vue";
import { useRouter, useRoute } from "vue-router";
import RegisterHeader from "@/components/RegisterHeader.vue";
import { navigateTo } from '@/common/RouterUtil.js';
const router = useRouter(); 
const active = ref(false);

const emit = defineEmits(['hide-top-appbar']);

const title = "한줄 소개";
const desc = "나를 소개할 수 있는 한마디를 작성해주세요";

const userDesc = ref("");
const maxCharLength = 100; // 최대 글자수 상수로 정의

const recmList = ref([
    '• MBTI와 학년 정보',
    '• 관심 분야나 목표',
    '• 함께하고 싶은 활동'
]);

// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-top-appbar');
});

onUnmounted(() => {

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
    case 'goToBack':
      navigateTo(router, '/register/time');
      break;

    case 'goToNext':
      // navigateTo(router, '/register/desc');
      break;

    default:
      console.error('알 수 없는 액션 타입:', action);
  }
}

</script> 

<style scoped>
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

.recm-item {
  color: #4A5565;
  padding: 8px 12px;
  font-size: 14px;
  font-weight: 400;
  background-color: #FFFFFF;
  border-radius: 12px;
  border: #E5E7EB 0.6px solid;
}
</style>