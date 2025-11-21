<template>
  <v-row 
    no-gutters
    class="justify-center | mt-12"
  >
    <v-chip>
      학교 이메일로 가입
    </v-chip>
  </v-row>
  <v-row 
    no-gutters
    class="justify-center | mt-6"
  >
    <v-col cols="12" class="mt-9">비슷한 사람들과 가벼운 밥약부터 시작해요.</v-col>
    <v-col cols="12" class="mt-9">학교 인증으로 더욱 안전하게 이용해요.</v-col>
  </v-row>

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


</script> 

<style scoped>

</style>