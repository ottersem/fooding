<template>
  <BoxContainer>
    <ProgressHeader :totalSteps="4" :currentStep="currentStep"></ProgressHeader>
    <RouterView />
  </BoxContainer>
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref, watch, computed } from "vue";
import { useRouter, useRoute } from "vue-router";
import ProgressHeader from "@/components/ProgressHeader.vue";
import BoxContainer from "@/components/BoxContainer.vue";

const emit = defineEmits(['hide-top-appbar']);
const router = useRouter();
const route = useRoute();

// 현재 단계를 계산하는 computed property
const currentStep = computed(() => {
  const stepMap = {
    'RegisterDetail': 1,
    'RegisterTime': 2,
    'RegisterKeyword': 3,
    'RegisterDesc': 4,
  };
  return stepMap[route.name] || 0;
});

// 다음 단계로 이동
const goToNextStep = (nextRouteName) => {
  router.push({ name: nextRouteName });
};

// 이전 단계로 이동
const goToPreviousStep = (previousRouteName) => {
  router.push({ name: previousRouteName });
};

// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-top-appbar');
  // 첫 진입 시 RegisterDesc로 리다이렉트
  if (!route.name || route.name === 'Register') {
    router.push({ name: 'RegisterDesc' });
  }
});

onUnmounted(() => {

});

// ----- 함수 정의 ----- //
// 이 함수들을 자식 컴포넌트에서 사용할 수 있도록 제공
defineExpose({
  goToNextStep,
  goToPreviousStep
});

</script> 

<style scoped>

</style>