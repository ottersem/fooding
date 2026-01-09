<template>
    <v-container class="pa-0 | pl-4 | pr-4">

        <v-row no-gutters class="justify-center | mt-8 | mb-6">
            <v-icon
                color="#9CA3AF" size="20" icon="$cus-shine-line"  class="mb-1"
            />
            <v-col cols="12" class="info-text | text-center | mb-2">
                5초만 투자하면 더 좋은 모임 문화를 만들 수 있어요 
            </v-col>
        </v-row>

        <v-card 
            class="meeting-card | pa-4" 
            variant="outlined"
        >
            <v-row no-gutters class="align-center | card-title">
                {{ groupInfo.title }}
            </v-row>

            <v-row no-gutters class="pa-0 | mt-3 | mb-3">
                <v-col cols="12" class="mb-1">
                    <v-row no-gutters class="align-center">
                        <v-icon color="#6A7282" size="18" class="mr-1">mdi-clock-time-four-outline</v-icon>
                        <span class="description-text">{{ groupInfo.meetingDate }} {{ getTimeSlotText(groupInfo.timeSlotId) }}</span>
                    </v-row>
                </v-col>
                <v-col cols="12">
                    <v-row no-gutters class="align-center">
                        <v-icon color="#6A7282" size="18" class="mr-1">mdi-map-marker-outline</v-icon>
                        <span class="description-text">{{ groupInfo.place }}</span>
                    </v-row>
                </v-col>
            </v-row>

            <v-row no-gutters class="align-center">
                <v-chip v-if="groupInfo.categoryId === 1" size="small" variant="outline" class="category-chip" prepend-icon="mdi-coffee">일상/친목</v-chip>
                <v-chip v-if="groupInfo.categoryId === 2" size="small" variant="outline" class="category-chip" prepend-icon="mdi-trophy">대외활동/공모전</v-chip>
                <v-chip v-if="groupInfo.categoryId === 3" size="small" variant="outline" class="category-chip" prepend-icon="mdi-briefcase">커리어</v-chip>
                <v-chip v-if="groupInfo.categoryId === 4" size="small" variant="outline" class="category-chip" prepend-icon="mdi-book-open-page-variant">스터디</v-chip>
                <v-chip v-if="groupInfo.categoryId === 5" size="small" variant="outline" class="category-chip" prepend-icon="mdi-palette">취미/여가</v-chip>
                
                <v-chip v-if="groupInfo.interestId === 1" size="small" variant="outline" class="tag-chip">일상/친목</v-chip>
                <v-chip v-if="groupInfo.interestId === 2" size="small" variant="outline" class="tag-chip">대외활동/공모전</v-chip>
                <v-chip v-if="groupInfo.interestId === 3" size="small" variant="outline" class="tag-chip">커리어</v-chip>
                <v-chip v-if="groupInfo.interestId === 4" size="small" variant="outline" class="tag-chip">스터디</v-chip>
                <v-chip v-if="groupInfo.interestId === 5" size="small" variant="outline" class="tag-chip">취미/여가</v-chip>
            </v-row>
        </v-card>

        <v-card 
            class="meeting-card | pa-4 | mt-6" 
            variant="outlined"
        >
            <v-row no-gutters class="align-center | card-title | mb-1">
                후기 작성하기
            </v-row>
            <v-row no-gutters class="align-center | card-desc">
                모임에 대한 만족도와 후기를 작성해주세요.
            </v-row>

            <v-row no-gutters class="justify-center | mt-4 | mb-4">
                <v-rating
                    v-model="review.rating"
                    background-color="#E5E7EB"
                    color="#FFB800" density="compact"
                    size="36"
                    length="5"
                    empty-icon="$cus-star-line"
                    full-icon="$cus-star-fill"
                />
            </v-row>
            <v-row no-gutters class="justify-center | mt-1">
                <v-textarea
                    placeholder="간단한 후기를 작성해주세요" 
                    hide-details
                    variant="outlined" density="comfortable" rounded="lg" bg-color="#F9FAFB" base-color="#E5E7EB" color="#ADB6C2"
                    class="inputbox" 
                    v-model="review.comment"
                    @input="handleInputChange('input')"
                    :maxlength="maxCharLength"
                />
            </v-row>
            <v-row no-gutters class="justify-end | label-text-small | mt-1 | mb-2">
                {{ review.comment.length }}/{{ maxCharLength }} 
            </v-row>
        </v-card>


        <v-row no-gutters class="justify-center | align-center | info-box | mt-6">
            작성하신 후기는 신뢰할 수 있는 모임 문화를 만드는데 활용됩니다.
        </v-row>

    </v-container>
    <SaveFooter
        @go-next="handleClickBtn('saveReview')"
        :active="active"
    />
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref } from "vue";
import { useRouter } from "vue-router";
import { navigateTo } from '@/common/RouterUtil.js';
import SaveFooter from '@/components/SaveFooter.vue';

const emit = defineEmits(['hide-top-appbar']);
const router = useRouter(); 

const groupInfo = ref({
  id: 1,
  creatorId: 10,
  categoryId: 1, // 일상/친목
  interestId: 1,
  title: "점심 같이 먹을 사람 구해요",
  description: "혼밥보다는 함께 밥 먹으면서 수다떨 사람 찾아요. 편하게 이야기 나눠요!",
  meetingDate: "2025-12-10",
  timeSlotId: 2,
  place: "학생식당 2층",
  maxParticipants: 4,
  currentParticipants: 2,
  status: 0, // 모집중
});

// 후기 작성 시 사용할 단일 객체
const review = ref({
    rating: 0,
    comment: '',
});

const maxCharLength = 100; // 최대 글자수 상수로 정의
const active = ref(true); // 다음 버튼 활성화 여부

// ----- 라이프 사이클 ----- //
onMounted(() => {
    emit('hide-bottom-appbar');
});

onUnmounted(() => {

});

// ----- 함수 정의 ----- //

function getTimeSlotText(timeSlotId) {
  const timeSlots = {
    1: '평일 오전 (09:00 - 12:00)',
    2: '평일 오후 (12:00 - 18:00)',
    3: '평일 저녁 (18:00 - 22:00)',
    4: '주말 오전 (09:00 - 12:00)',
    5: '주말 오후 (12:00 - 18:00)',
    6: '주말 저녁 (18:00 - 22:00)'
  };
  return timeSlots[timeSlotId] || '';
}

function handleInputChange(action, value) {
  switch (action) {
    case 'input':
      const length = groupDescription.value?.length ?? 0;

      if (length > maxCharLength) {
          groupDescription.value = groupDescription.value.slice(0, maxCharLength);
      }
      break;
  }
}

function handleClickBtn(action, value) {
  switch (action) {
    case 'saveReview':
      break;

    default:
      console.error('알 수 없는 액션 타입:', action);
  }
}

</script> 

<style scoped>
.meeting-card {
    border-radius: 12px;
    border: 0.7px solid #E5E7EB;
    background-color: #FFFFFF;
}

.card-title {
    font-size: 16px;
    font-weight: 600;
    color: #364153;
}

.card-desc {
    font-size: 14px;
    color: #4A5565;
}

.info-text {
    font-size: 14px;
    color: #FF6129;
}

.info-box {
  min-height: 36px; 
  border-radius: 12px;
  border: 0.7px solid #E5E7EB;
  background-color: #F3F4F6;
  color: #4A5565;
  font-size: 12px;
  font-weight: 400;
}

.inputbox :deep(.v-input__details) {
  padding-top: 4px !important;
}
.inputbox :deep(.v-icon) {
  color: #8B95A1 !important;
  opacity: 1;
}

.label-text-small {
  font-size: 12px;
  font-weight: 400;
  color: #364153;
}

.category-chip {
    background-color: #FFF4F0;
    border: 0.7px solid #FFE0D4;
    color: #FF6129;
    font-size: 12px;
    padding-left: 16px !important;
    padding-right: 12px !important;
}

.tag-chip {
    background-color: #F3F4F6;
    color: #4A5565;
    font-size: 12px;
    margin-left: 8px;
    padding-left: 12px !important;
    padding-right: 12px !important;
}

.status-chip {
    height: 24px !important;
    padding: 4px 8px !important;
    font-size: 12px !important;
    font-weight: 400 !important;
    border-radius: 4px !important;
    border: none !important;
    box-shadow: none !important;
}

.description-text {
    font-size: 14px;
    color: #4A5565;
}

</style>