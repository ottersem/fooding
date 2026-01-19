<template>
    <v-row 
        no-gutters justify="start" 
        class="text-title | mb-1"
    >
        <v-col cols="12">{{ title }}</v-col>
    </v-row>
    <v-row 
        no-gutters justify="start"
        class="text-subtitle | mb-10"
    >
        <v-col cols="12" v-html="props.desc"></v-col>
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
    width: 100%;
    padding-top: 32px;
    font-size: 16px;
    font-weight: 600;
    color: #101828;
}

.text-subtitle {
    width: 100%;
    font-size: 14px;
    font-weight: 400;
    color: #4A5565;
}
</style>