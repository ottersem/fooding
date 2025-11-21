<template>
  <div class="register-detail">
    <h2>상세 정보</h2>
    <p>그룹의 상세 정보를 입력해주세요.</p>
    
    <div class="button-group">
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
const goToNext = () => {
  router.push({ name: 'RegisterTime' });
};

</script> 

<style scoped>
.register-detail {
  padding: 20px;
  text-align: center;
}

.register-detail h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

.register-detail p {
  font-size: 16px;
  color: #666;
  margin-bottom: 30px;
}

.button-group {
  display: flex;
  gap: 10px;
  justify-content: center;
}

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

.next-button:hover {
  background-color: #0056b3;
}
</style>