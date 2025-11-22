<template>
    <ProgressHeader 
      @go-back="handleClickBtn('goToBack')"
      :totalSteps="4" :currentStep="3"
    />

    <v-row no-gutters class="justify-center | pr-4 | pl-4 | pt-0">
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

const title = "활동 가능한 시간대는?";
const desc = "여러 개를 선택할 수 있어요 (3/4개 선택)";

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
      navigateTo(router, '/register/keyword');
      break;

    case 'goToNext':
      navigateTo(router, '/register/desc');
      break;

    default:
      console.error('알 수 없는 액션 타입:', action);
  }
}

</script> 

<style scoped>

</style>