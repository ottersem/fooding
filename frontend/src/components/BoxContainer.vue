<template>
  <div class="container-box | pt-4">
    <slot></slot>
  </div>
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref, computed, watch} from "vue";
import { useRouter, useRoute } from "vue-router";
import { routes } from "@/router"

// ----- 라이프 사이클 ----- //
onMounted(() => {

});

onUnmounted(() => {

})

// ----- 함수 정의 ----- //




</script>

<style scoped>

.container-box {
  padding-left: 36px; 
  padding-right: 36px;           
  width: 100%;
  height: 100%;
  max-width: 1290px;
  align-items: center;
  justify-items: auto;
}

</style>