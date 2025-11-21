<template>
    <ProgressHeader 
      @go-back="handleClickBtn('goToBack')"
      :totalSteps="4" :currentStep="2"
    />

    <v-row no-gutters class="justify-center | pr-4 | pl-4">
      <v-col cols="12">
        <RegisterHeader :title="title" :desc="desc"/>
      </v-col>

    </v-row>

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

const emit = defineEmits(['hide-top-appbar']);

const title = "관심 있는 주제를 선택해주세요 (최대 2개)";
const desc = "비슷한 관심사를 가진 사람과 연결될 확률이 높아져요";

const active = ref(false);

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
      navigateTo(router, '/register/basic');
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

</style>