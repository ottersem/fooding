<template>
    <ProgressHeader 
      @go-back="handleClickBtn('goToBack')"
      :totalSteps="4" :currentStep="3"
    />

    <v-container class="justify-center | pr-4 | pl-4 | pt-0">
      <RegisterHeader :title="title" :desc="desc"/>

      <v-row no-gutters class="justify-start">
          <v-chip
            variant="outlined" append-icon=""
            class="info-chips"
          >
            학우들이 가장 많이 선택한 시간을 추천드렸어요!
          </v-chip>
      </v-row>

      <v-row no-gutters class="justify-start | mt-6">
        <v-col 
          v-for="(actTime, index) in actTimeList"
          :key="index"
          cols="12"   class="pa-1" 
        >
          <v-chip
            @click="toggleKeyword(actTime.tag)"
            variant="outlined"
            :class="{ 'selected-actTime': selectTime.includes(actTime.tag) }"
            :disabled="isChipDisabled(actTime.tag)" 
            :style="{ 
              width: '100%', height: '100%', justifyContent: 'start',
              opacity: isChipDisabled(actTime.tag) && !selectTime.includes(actTime.tag) ? 0.4 : 1,
            }"
          >
            {{ actTime.text }} 
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
import { onMounted, onUnmounted, ref, watch } from "vue";
import { useRouter, useRoute } from "vue-router";
import RegisterHeader from "@/components/RegisterHeader.vue";
import { navigateTo } from '@/common/RouterUtil.js';
const router = useRouter(); 

const emit = defineEmits(['hide-top-appbar']);

const title = "활동 가능한 시간대는?";
const desc = "여러 개를 선택할 수 있어요 (3/4개 선택)";

const active = ref(false);

const maxSelection = 4;
const selectTime = ref([]);
const actTimeList = ref([
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

watch(selectTime, (newKeywords) => {
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
    const index = selectTime.value.indexOf(keywordTag);
    
    if (index === -1) {
        // 선택되지 않은 키워드일 경우
        if (selectTime.value.length < maxSelection) {
            selectTime.value.push(keywordTag);
        }
    } else {
        // 이미 선택된 키워드일 경우 제거
        selectTime.value.splice(index, 1);
    }

    console.log(selectTime.value);
}

function isChipDisabled(keywordTag) {
  return selectTime.value.length >= maxSelection && !selectTime.value.includes(keywordTag);
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

.selected-actTime {
  background-color: #FFF5F2;
  border: 1.35px solid #FF6129;
}
</style>