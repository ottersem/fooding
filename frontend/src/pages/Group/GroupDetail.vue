<template>
  <v-container class="pa-0">
    <v-row no-gutters class="justify-center | pa-4">
      <v-col cols="12">
        <h2>모임 상세 정보</h2>
        <p class="mt-4">모임 ID: {{ groupId }}</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref, computed } from "vue";
import { useRouter, useRoute } from "vue-router";

const emit = defineEmits(['hide-top-appbar', 'hide-bottom-appbar']);
const router = useRouter();
const route = useRoute();

// 쿼리 파라미터에서 id 가져오기
const groupId = computed(() => route.query.id);

// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-bottom-appbar');
  console.log('GroupDetail mounted with ID:', groupId.value);
});

onUnmounted(() => {

});

// ----- 함수 정의 ----- //


</script> 

<style scoped>

</style>