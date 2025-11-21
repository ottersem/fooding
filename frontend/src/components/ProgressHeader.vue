<template>
  <v-row no-gutters class="justify-space-between | align-center | header-container">
    <v-col cols="auto" class="pl-2">
        <v-btn
          icon="mdi-chevron-left" 
          variant="text" density="comfortable"
          @click="goBack"
        ></v-btn>
    </v-col>

    <div class="right-container">
      <div class="progress-indicator">
        <div 
          v-for="n in totalStepsComputed" 
          :key="n" 
          :class="['step-bar', { 'active': n <= currentStepComputed }]"
        ></div>
      </div>
      
      <span class="step-text">
        {{ currentStepComputed }} / {{ totalStepsComputed }}
      </span>
    </div>
  </v-row>
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref, computed } from "vue";
import { useRouter } from 'vue-router'; // goBack 함수를 위해 추가

const router = useRouter();

// Props 정의 및 기본값 지정
const props = defineProps({
    // 기본값: 4
    totalSteps: {
        type: Number,
        default: 4
    },
    // 기본값: 1
    currentStep: {
        type: Number,
        default: 1
    }
});

const totalStepsComputed = computed(() => props.totalSteps);
const currentStepComputed = computed(() => props.currentStep);

// ----- 라이프 사이클 ----- //
onMounted(() => {
    
});

onUnmounted(() => {

});

// ----- 함수 정의 ----- //
const goBack = () => {
  console.log('뒤로가기 버튼 클릭됨');
};


</script>

<style scoped>
.header-container {
  padding: 12px 16px 12px 0px;
  border-bottom: 1px solid #E5E7EB;
  background-color: #FFFFFF;
}

.right-container {
  display: flex;
  align-items: center;
}

.progress-indicator {
  display: flex;
  align-items: center;
  gap: 4px;
  margin-right: 8px; 
}

.step-bar {
  width: 30px;
  height: 4px;
  background-color: #E5E7EB;
  border-radius: 2px;
  transition: background-color 0.3s;
}

.step-bar.active {
    background-color: #FF6129; 
}

.step-text {
  font-size: 12px;
  font-weight: 400;
  color: #88919C; 
}
</style>