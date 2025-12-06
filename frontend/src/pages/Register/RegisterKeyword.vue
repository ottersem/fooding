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
          cols="6" class="pa-1" 
        >
          <v-chip
            @click="toggleKeyword(keyword.tag)"
            variant="outlined"
            :class="{ 'selected-keyword': keywords.includes(keyword.tag) }"
            :disabled="isChipDisabled(keyword.tag)" 
            :style="{ 
              width: '100%', height: '100%', justifyContent: 'start',
              opacity: isChipDisabled(keyword.tag) && !keywords.includes(keyword.tag) ? 0.4 : 1,
            }"
          >
            {{ keyword.text }} 
          </v-chip>
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
// [수정 1] computed 추가
import { onMounted, onUnmounted, ref, watch, computed } from "vue"; 
import { useRouter, useRoute } from "vue-router";
import ProgressFooter from "@/components/ProgressFooter.vue";
import RegisterHeader from "@/components/RegisterHeader.vue";
import { navigateTo } from '@/common/RouterUtil.js';

const router = useRouter(); 
const emit = defineEmits(['hide-top-appbar', 'hide-bottom-appbar']);

// [수정 2] desc(computed)에서 참조하기 위해 데이터 변수들을 먼저 선언
const maxSelection = 2;
const keywords = ref([]); // 선택된 키워드 배열
const active = ref(false);

const keywordList = ref([
  { text: '☕️ 일상/친목', tag: 'daily_social' },
  { text: '🏆 대외활동/공모전', tag: 'activities_contest' },
  { text: '💼 커리어', tag: 'career_job' },
  { text: '📚 스터디', tag: 'study_group' },
  { text: '🎨 취미/여가', tag: 'hobby_leisure' },
]);

const title = "관심 있는 주제를 선택해주세요 (최대 2개)";

// [수정 3] desc를 일반 문자열에서 computed로 변경하여 동적으로 개수 표시
const desc = computed(() => {
  return `비슷한 관심사를 가진 사람과 연결될 확률이 높아져요 <br>(${keywords.value.length}/${maxSelection}개 선택)`;
});


// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-top-appbar');
  emit('hide-bottom-appbar');
});

onUnmounted(() => {
  // 필요 시 로직 추가
});

watch(keywords, (newKeywords) => {
  active.value = newKeywords.length > 0;
}, { deep: true });


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

function isChipDisabled(keywordTag) {
  return keywords.value.length >= maxSelection && !keywords.value.includes(keywordTag);
}
</script> 

<style scoped>
.v-chip {
  min-height: 56px; 
  padding-left: 16px;
  padding-right: 16px;
  border-radius: 16px;
  border: 1.35px solid #E5E7EB;
  background-color: #FFFFFF;
  color: #364153;
  font-size: 14px;
  font-weight: 400;
}

.selected-keyword {
  background-color: #FFF5F2;
  border: 1.35px solid #FF6129;
}
</style>