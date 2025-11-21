<template>
  <div class="register-keyword">
    <h2>키워드 선택</h2>
    <p>그룹의 키워드를 선택해주세요.</p>
    
    <div class="button-group">
      <button class="prev-button" @click="goToPrev">이전</button>
      <button class="next-button" @click="goToNext">다음</button>
    </div>
  </div>
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref, watch } from "vue";
import { useRouter, useRoute } from "vue-router";

const emit = defineEmits(['hide-top-appbar']);
const router = useRouter(); 


// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-top-appbar');
});

onUnmounted(() => {

});

// ----- 함수 정의 ----- //
const goToPrev = () => {
  router.push({ name: 'RegisterTime' });
};

const goToNext = () => {
  router.push({ name: 'RegisterDesc' });
};

</script> 

<style scoped>
.register-keyword {
  padding: 20px;
  text-align: center;
}

.register-keyword h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

.register-keyword p {
  font-size: 16px;
  color: #666;
  margin-bottom: 30px;
}

.button-group {
  display: flex;
  gap: 10px;
  justify-content: center;
}

.prev-button,
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

.prev-button {
  background-color: #6c757d;
}

.prev-button:hover {
  background-color: #5a6268;
}

.next-button:hover {
  background-color: #0056b3;
}
</style>