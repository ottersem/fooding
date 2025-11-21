<template>
  <div class="register-time">
    <h2>시간 설정</h2>
    <p>그룹의 시간을 설정해주세요.</p>
    
    <div class="button-group">
      <button class="prev-button" @click="goToPrev">이전</button>
      <button class="next-button" @click="goToNext">다음</button>
    </div>
  </div>
</template>

<script setup>
// ----- 선언부 ----- //
import { useRouter } from "vue-router";

const router = useRouter();

// ----- 라이프 사이클 ----- //

// ----- 함수 정의 ----- //
const goToPrev = () => {
  router.push({ name: 'RegisterDetail' });
};

const goToNext = () => {
  router.push({ name: 'RegisterKeyword' });
};

</script> 

<style scoped>
.register-time {
  padding: 20px;
  text-align: center;
}

.register-time h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

.register-time p {
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
