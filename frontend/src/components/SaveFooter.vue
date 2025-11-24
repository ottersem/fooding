<template>
  <v-row no-gutters class="justify-space-between | align-center | footer-container">
    <v-btn
      v-if="props.active"
      variant="outlined"
      class="active-btn"
      @click="handleClickBtn('goToNext')"
    >저장하기</v-btn>
    <v-btn
      v-else
      variant="outlined"
      class="readonly-btn"
      readonly
    >저장하기</v-btn>
  </v-row>
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref, computed } from "vue";
import { useRouter } from 'vue-router'; // goBack 함수를 위해 추가

const emit = defineEmits(['go-next']);
const router = useRouter();

// Props 정의 및 기본값 지정
const props = defineProps({
    active: {
        type: Boolean,
        default: false
    }
});

// ----- 라이프 사이클 ----- //
onMounted(() => {
    
});

onUnmounted(() => {

});

// ----- 함수 정의 ----- //
function handleClickBtn(action) {
  switch (action) {
    case 'goToNext':
      console.log('Go Next button clicked');
      emit('go-next');
      break;

    default:
      console.error('알 수 없는 액션 타입:', action);
  }
}


</script>

<style scoped>
.footer-container {
  background-color: #FFFFFF;
  padding: 16px;
  border-top: 1px solid #E5E7EB;
  position: fixed;
  bottom: 0;
  width: 100%;
  z-index: 99;
}
</style>