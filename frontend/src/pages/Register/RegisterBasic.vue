<template>
    <ProgressHeader 
      @go-back="handleClickBtn('goToBack')"
      :totalSteps="4" :currentStep="1"
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
import ProgressHeader from "@/components/ProgressHeader.vue";
const router = useRouter(); 

const emit = defineEmits(['hide-top-appbar']);

const title = "기본 정보를 입력해주세요";
const desc = "학과와 학년 정보를 알려주세요";

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

</style>