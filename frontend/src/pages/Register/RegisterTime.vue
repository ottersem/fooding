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
          v-for="(actTime, index) in actTimeList" :key="index"
          cols="12" class="mt-2"
        >
          <v-btn
            @click="toggleKeyword(actTime.tag)"
            variant="outlined" rounded="lg" block
            :class="{ 'selected-btn': selectTime.includes(actTime.tag) }"
            :disabled="isButtonDisabled(actTime.tag)"
            class="time-btn"
          >
            <template v-slot:prepend>
              <v-icon
                class="radio-icon"
                :color="selectTime.includes(actTime.tag) ? '#FF6129' : '#9CA3AF'"
              >
                {{ selectTime.includes(actTime.tag) ? 'mdi-radiobox-marked' : 'mdi-radiobox-blank' }}
              </v-icon>
              <span class="btn-text" :class="{ 'selected-text': selectTime.includes(actTime.tag) }" style="text-align: left;">{{ actTime.text }}</span>
            </template>

            <template v-slot:append>
              <span class="btn-time" :class="{ 'selected-text': selectTime.includes(actTime.tag) }" style="text-align: right;">{{ actTime.time }}</span>
              <v-icon
                class="trailing-icon"
                color="#9CA3AF"
                size="20"
              >
                mdi-chevron-right
              </v-icon>
            </template>
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

const title = "활동 가능한 시간대는?";
const desc = "여러 개를 선택할 수 있어요 (3/4개 선택)"; 

const active = ref(false);

// 다중 선택을 위한 배열과 최대 개수 원본 복원
const maxSelection = 4;
const selectTime = ref([]); 

const actTimeList = ref([
  { 
    text: '평일 오전', 
    time: '09:00 - 12:00', 
    tag: 'weekday_morning' 
  },
  { 
    text: '평일 오후', 
    time: '12:00 - 18:00', 
    tag: 'weekday_afternoon' 
  },
  { 
    text: '평일 저녁', 
    time: '18:00 - 22:00', 
    tag: 'weekday_evening' 
  },
  { 
    text: '주말 오전', 
    time: '09:00 - 12:00', 
    tag: 'weekend_morning' 
  },
  { 
    text: '주말 오후', 
    time: '12:00 - 18:00', 
    tag: 'weekend_afternoon' 
  },
  { 
    text: '주말 저녁', 
    time: '18:00 - 22:00', 
    tag: 'weekend_evening' 
  },
]);

// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-top-appbar');
});

onUnmounted(() => {
  // 필요한 경우 unmounted 시 로직 추가
});

watch(selectTime, (newTimes) => {
  active.value = newTimes.length > 0;
}, { deep: true });

// ----- 함수 정의 ----- //
function handleClickBtn(action) {
  switch (action) {
    case 'goToBack':
      navigateTo(router, '/register/keyword');
      break;

    case 'goToNext':
      if (active.value) {
        console.log('선택된 시간대:', selectTime.value);
        navigateTo(router, '/register/desc');
      }
      break;

    default:
      console.error('알 수 없는 액션 타입:', action);
  }
}

// 다중 선택 토글 로직
function toggleKeyword(keywordTag) {
    const index = selectTime.value.indexOf(keywordTag);
    
    if (index === -1) {
        if (selectTime.value.length < maxSelection) {
            selectTime.value.push(keywordTag);
        }
    } else {
        selectTime.value.splice(index, 1);
    }

    console.log(selectTime.value);
}

// 버튼 비활성화 로직
function isButtonDisabled(keywordTag) {
  return selectTime.value.length >= maxSelection && !selectTime.value.includes(keywordTag);
}
</script>

<style scoped>
.info-chips {
  min-height: 32px; 
  padding-left: 12px;
  padding-right: 12px;
  border-radius: 16px;
  border: 1.35px solid #E5E7EB;
  background-color: #F9FAFB;
  color: #6B7280;
  font-size: 12px;
  font-weight: 400;
}

.time-btn {
  padding-left: 16px !important; 
  padding-right: 16px !important;
  
  min-height: 56px; 
  border-radius: 16px;
  border: 1.35px solid #E5E7EB;
  background-color: #FFFFFF;
  color: #364153;
  
  text-transform: none !important;
}

.selected-btn {
  background-color: #FFF5F2 !important;
  border: 1.35px solid #FF6129 !important;
}

.radio-icon {
    margin-right: 12px; 
    font-size: 20px; 
}

.btn-text, .btn-time {
  font-size: 14px;
  font-weight: 400;
  color: #364153;
}

.selected-btn .selected-text {
  color: #FF6129;
}
</style>