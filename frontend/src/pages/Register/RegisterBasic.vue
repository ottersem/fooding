<template>
    <ProgressHeader 
      @go-back="handleClickBtn('goToBack')"
      :totalSteps="4" :currentStep="1"
    />

    <v-container class="justify-center | pr-4 | pl-4 | pt-0">
      <RegisterHeader :title="title" :desc="desc"/>

      <v-row no-gutters class="justify-start | label-text">
        학과
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-combobox
          v-model="major"
          :items="majorOptions"
          placeholder="예술공학과" 
          class="inputbox"
          variant="outlined" density="comfortable" rounded="lg" bg-color="#FFFFFF" base-color="#E5E8EB" color="#E5E8EB"
          clearable
        />
      </v-row>

      <v-row no-gutters class="justify-start | label-text">
        학년
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-select
          v-model="grade"
          :items="gradeOptions"
          placeholder="학년" 
          class="inputbox"
          variant="outlined" density="comfortable" rounded="lg" bg-color="#FFFFFF" base-color="#E5E8EB" color="#E5E8EB"
        />
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
import ProgressHeader from "@/components/ProgressHeader.vue";
import ProgressFooter from "@/components/ProgressFooter.vue";

const router = useRouter(); 

const emit = defineEmits(['hide-top-appbar']);

const title = "기본 정보를 입력해주세요";
const desc = "학과와 학년 정보를 알려주세요";

const active = ref(false);

const major = ref(null);
const majorOptions = ref([
    '예술공학과',
    '소프트웨어학부',
]);

const grade = ref(null);
const gradeOptions = ref([
  '1학년',
  '2학년',
  '3학년',
  '4학년',
  '5학년 이상',
]);

// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-top-appbar');
});

onUnmounted(() => {

});

watch([major, grade], ([newMajor, newGrade]) => {
  const isMajorValid = newMajor !== null && newMajor !== '';
  const isGradeValid = newGrade !== null && newGrade !== '';
  
  // 두 조건이 모두 true일 때만 다음 버튼 활성화
  active.value = isMajorValid && isGradeValid;
}, { immediate: true });

// ----- 함수 정의 ----- //

function handleClickBtn(action) {
  switch (action) {
    case 'goToBack':
      navigateTo(router, '/register');
      break;

    case 'goToNext':
      navigateTo(router, '/register/keyword');
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

</style>