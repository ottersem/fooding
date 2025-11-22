<template>
    <v-row 
        no-gutters justify="start" 
        class="text-title | mb-4"
    >
        <v-col>{{ title }}</v-col>
    </v-row>
    <v-row 
        no-gutters justify="start"
        class="text-subtitle | mb-10"
    >
        <v-col v-html="props.desc"></v-col>
    </v-row>
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref, computed, watch} from "vue";

const props = defineProps({
    title: String,
    desc: String
});

// ----- 라이프 사이클 ----- //
onMounted(() => {
    
});

onUnmounted(() => {

})

// ----- 함수 정의 ----- //


</script>

<style scoped>
.text-title {
    font-size: 19.5px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
    letter-spacing: -0.5px;
}

.text-subtitle {
    font-size: 14px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    letter-spacing: -0.4px;
    color: #404040;
}
</style>