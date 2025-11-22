<template>
    <ProgressHeader 
      @go-back="handleClickBtn('goToBack')"
      :totalSteps="4" :currentStep="2"
    />

    <v-container class="justify-center | pr-4 | pl-4 | pt-0">
      <RegisterHeader :title="title" :desc="desc"/>

      <v-row no-gutters class="justify-start | mt-1">
        <v-col 
          v-for="(keyword, index) in keywordList"
          :key="index"
          cols="6"   class="pa-1" 
        >
            <v-btn
                class="keyword-btn"
                variant="outlined" rounded="lg" block
                :class="{ 'selected-keyword': keywords.includes(keyword.tag) }"
                @click="toggleKeyword(keyword.tag)"
            >
                {{ keyword.text }} 
            </v-btn>
        </v-col>
      </v-row>
    </v-container>

    <ProgressFooter
      @go-next="handleClickBtn('goToNext')"
      :active="active"
    />
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref, watch } from "vue";
import { useRouter, useRoute } from "vue-router";
import RegisterHeader from "@/components/RegisterHeader.vue";
import { navigateTo } from '@/common/RouterUtil.js';
const router = useRouter(); 

const emit = defineEmits(['hide-top-appbar']);

const title = "관심 있는 주제를 선택해주세요 (최대 2개)";
const desc = "비슷한 관심사를 가진 사람과 연결될 확률이 높아져요";

const active = ref(false);

const maxSelection = 2;
const keywords = ref([]);
const keywordList = ref([
  { text: '☕️ 일상/친목', tag: 'daily_social' },
  { text: '🏆 대외활동/공모전', tag: 'activities_contest' },
  { text: '💼 커리어', tag: 'career_job' },
  { text: '📚 스터디', tag: 'study_group' },
  { text: '🎨 취미/여가', tag: 'hobby_leisure' },
]);


// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-top-appbar');
});

onUnmounted(() => {

});

// ----- 함수 정의 ----- //
function handleClickBtn(action) {
  switch (action) {
    case 'goToBack':
      navigateTo(router, '/register/basic');
      break;

    case 'goToNext':
      navigateTo(router, '/register/time');
      break;

    default:
      console.error('알 수 없는 액션 타입:', action);
  }
}

function toggleKeyword(keywordTag) {
    const index = keywords.value.indexOf(keywordTag);
    
    if (index === -1) {
        // 선택되지 않은 키워드일 경우
        if (keywords.value.length < maxSelection) {
            keywords.value.push(keywordTag);
        }
    } else {
        // 이미 선택된 키워드일 경우 제거
        keywords.value.splice(index, 1);
    }

    console.log(keywords.value);
}

</script> 

<style scoped>

</style>