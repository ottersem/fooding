<template>
    <v-container class="pa-0">
        <v-row no-gutters class="stat-box">
            <v-col class="stat-container | pt-3 | pb-3">
              <v-row no-gutters class="justify-center | stat-text">
                {{ reviewStats.totalParticipated }}
              </v-row>
              <v-row no-gutters class="justify-center | label-text">
                총 참여
              </v-row>
            </v-col>
            <v-col class="stat-container | pt-3 | pb-3">
              <v-row no-gutters class="justify-center | stat-text">
                {{ reviewStats.totalReviewed }}
              </v-row>
              <v-row no-gutters class="justify-center | label-text">
                작성한 후기
              </v-row>
            </v-col>
            <v-col class="stat-container | pt-3 | pb-3">
              <v-row no-gutters class="justify-center | align-center | stat-text">
                <v-icon 
                  icon="$cus-star-fill" 
                  size="20" 
                  color="#FFB800"
                  class=""
                />
                {{ reviewStats.averageRating.toFixed(1) }}
              </v-row>
              <v-row no-gutters class="justify-center | label-text">
                평균 별점
              </v-row>
            </v-col>
        </v-row>

        <v-row no-gutters class="justify-center | ml-4 | mr-4">
            <v-col 
                v-for="(group, index) in reviewList" 
                :key="index"
                cols="12"
                class="mb-4"
            >
                <v-card 
                    class="meeting-card | pa-4" 
                    variant="outlined"
                >
                    <v-row no-gutters class="pb-0 | align-center">
                      <v-row no-gutters class="align-center">
                          <v-chip 
                              v-if="group.status === 0" 
                              class="status-chip | review-completed"
                              variant="flat"
                          >
                              후기 작성 완료
                          </v-chip>
                          <v-chip 
                              v-if="group.status === 1" 
                              class="status-chip | review-not-completed"
                              variant="flat"
                          >
                              후기 미작성
                          </v-chip>
                      </v-row>
                    </v-row>

                    <v-row no-gutters class="mt-2 | align-center | card-title">
                        {{ group.title }}
                    </v-row>
                    <v-row no-gutters class="mt-1 | align-center | description-text">
                        {{ group.meetingDate }}
                    </v-row>

                    <v-row no-gutters class="pa-0 | mt-3 | mb-3">
                      <v-col cols="12" class="mb-1">
                          <v-row no-gutters class="align-center" style="gap: 2px;">
                              <v-icon 
                                  v-for="n in 5" 
                                  :key="n"
                              :icon="n <= group.score ? '$cus-star-fill' : '$cus-star-line'"
                                  size="16"
                              :color="n <= group.score ? '#FFB800' : '#E5E7EB'"
                              ></v-icon>
                          </v-row>
                      </v-col>
                        <v-col cols="12">
                            <v-row no-gutters class="align-center | description-text">
                                {{ group.comment }}
                            </v-row>
                        </v-col>
                    </v-row>

                    <v-row no-gutters class="align-center">
                        <v-chip v-if="group.categoryId === 1" size="small" variant="outline" class="category-chip" prepend-icon="mdi-coffee">일상/친목</v-chip>
                        <v-chip v-if="group.categoryId === 2" size="small" variant="outline" class="category-chip" prepend-icon="mdi-trophy">대외활동/공모전</v-chip>
                        <v-chip v-if="group.categoryId === 3" size="small" variant="outline" class="category-chip" prepend-icon="mdi-briefcase">커리어</v-chip>
                        <v-chip v-if="group.categoryId === 4" size="small" variant="outline" class="category-chip" prepend-icon="mdi-book-open-page-variant">스터디</v-chip>
                        <v-chip v-if="group.categoryId === 5" size="small" variant="outline" class="category-chip" prepend-icon="mdi-palette">취미/여가</v-chip>
                        <v-chip v-if="group.interestId === 1" size="small" variant="outline" class="tag-chip">일상/친목</v-chip>
                        <v-chip v-if="group.interestId === 2" size="small" variant="outline" class="tag-chip">대외활동/공모전</v-chip>
                        <v-chip v-if="group.interestId === 3" size="small" variant="outline" class="tag-chip">커리어</v-chip>
                        <v-chip v-if="group.interestId === 4" size="small" variant="outline" class="tag-chip">스터디</v-chip>
                        <v-chip v-if="group.interestId === 5" size="small" variant="outline" class="tag-chip">취미/여가</v-chip>
                    </v-row>
                    <v-btn
                      variant="outlined"
                      class="active-thin-btn | mt-3"
                      @click="handleClickBtn('goToReviewCreate')"
                    >후기 작성하기</v-btn>
                    <v-btn
                      variant="outlined"
                      class="unactive-thin-btn | mt-3"
                      @click="handleClickBtn('goToReviewCreate')"
                    >후기 수정하기</v-btn>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref } from "vue";
import { useRouter } from "vue-router";
import { navigateTo } from '@/common/RouterUtil.js';

const emit = defineEmits(['hide-top-appbar']);
const router = useRouter(); 

const title = "이번주 밥약/커피챗 신청";
const desc = "지금 선택한 관심사와 시간대에 맞춰 추천된 모임을 보여드릴게요";

const reviewStats = ref({
  totalParticipated: 12,
  totalReviewed: 8,
  averageRating: 4.5,
});

const reviewList = ref([
  {
    id: 1, // review id
    groupId: 101,
    reviewerId: 10,
    reviewedId: 20,
    score: 5,
    comment: "정말 즐거운 시간이었어요! 다음에도 함께하고 싶습니다.",

    // 모임 정보
    title: "점심 같이 먹을 사람 구해요",
    meetingDate: "2025-12-10",
    categoryId: 1, // 일상/친목
    interestId: 1,
    status: 0, // 후기 작성 완료
  },
  {
    id: 2,
    groupId: 102,
    reviewerId: 12,
    reviewedId: 22,
    score: 4,
    comment: "유익한 시간이었습니다. 함께 준비하면서 많이 배웠어요.",
    // 모임 정보
    title: "공모전 팀원 모집합니다",
    meetingDate: "2025-12-11",
    categoryId: 2, // 대외활동/공모전
    interestId: 2,
    status: 1, // 후기 미작성
  },
  {
    id: 3,
    groupId: 103,
    reviewerId: 15,
    reviewedId: 25,
    score: 3,
    comment: "같은 고민을 나누니 위로가 되었어요. 서로 응원하며 힘내봐요!",
    // 모임 정보
    title: "취업고민 같이 나눠요",
    meetingDate: "2025-12-12",
    categoryId: 3, // 커리어
    interestId: 3,
    status: 0, // 후기 작성 완료
  },
  {
    id: 4,
    groupId: 104,
    reviewerId: 18,
    reviewedId: 28,
    score: 4,
    comment: "알고리즘 문제 풀이가 정말 도움됐어요. 꾸준히 하면 좋겠네요.",
    // 모임 정보
    title: "알고리즘 스터디원 구합니다",
    meetingDate: "2025-12-13",
    categoryId: 4, // 스터디
    interestId: 4,
    status: 1, // 후기 미작성
  },
  {
    id: 5,
    groupId: 105,
    reviewerId: 20,
    reviewedId: 30,
    score: 5,
    comment: "운동 친구 생겨서 좋아요! 서로 동기부여 되면서 꾸준히 할 수 있을 것 같아요.",
    // 모임 정보
    title: "헬스 운동 친구 모집",
    meetingDate: "2025-12-14",
    categoryId: 5, // 취미/여가
    interestId: 5,
    status: 0, // 후기 작성 완료
  },
]);

// ----- 라이프 사이클 ----- //
onMounted(() => {
    
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

function handleClickBtn(action, value) {
  switch (action) {
    case 'goToReviewCreate':
      navigateTo(router, '/review/create', { id: value });
      break;

    default:
      console.error('알 수 없는 액션 타입:', action);
  }
}

</script> 

<style scoped>
.stat-box {
  padding: 16px 24px 24px 24px;
  gap: 8px;
}

.stat-container {
  background-color: #FFFFFF;
  border: 0.67px solid #E5E7EB;
  border-radius: 10px;
}

.meeting-card {
    box-shadow: 
    0 1px 2px -1px rgba(0, 0, 0, 0.1),
    0 1px 3px 0 rgba(0, 0, 0, 0.1);
    border-radius: 12px;
    border: 0.67px solid #F3F4F6;
    background-color: #FFFFFF;
}

.card-title {
    font-size: 16px;
    font-weight: 600;
    color: #364153;
}

.category-chip {
    background-color: #FFF4F0;
    border: 0.67px solid #FFE0D4;
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

.review-completed {
    background-color: #E6F0FF !important;
    color: #2B7FFF !important;
}

.review-not-completed {
    background-color: #F3F4F6 !important;
    color: #4A5565 !important;
}

.status-chip-completed {
    background-color: #F3F4F6 !important;
    color: #4A5565 !important;
}

.stat-text {
  font-size: 18px;
  font-weight: 600;
  color: #4A5565;
}

.label-text {
  font-size: 14px;
  font-weight: 450;
  color: #4A5565;
}

.categoryId-text {
    font-size: 12px;
    color: #8B95A1;
}

.description-text {
    font-size: 14px;
    color: #4A5565;
}

.info-section span {
    font-size: 13px;
    color: #6A7282;
}

.apply-chip {
    font-weight: 400;
    font-size: 13px;
    letter-spacing: -0.08px;
    padding: 4px 8px;
    border-radius: 12px;
    border: 0.67px solid #E5E7EB;
    background-color: #FFFFFF;
    color: #191F28;
}

.cancel-chip {
    font-weight: 400;
    font-size: 13px;
    letter-spacing: -0.08px;
    padding: 4px 8px;
    border-radius: 12px;
    border: 0.67px solid #E5E7EB;
    background-color: #FFFFFF;
    color: #191F28;
}

.accepted-chip {
    font-weight: 400;
    font-size: 13px;
    letter-spacing: -0.08px;
    padding: 4px 8px;
    border-radius: 12px;
    border: 0.67px solid #FF6129;
    background-color: #FFF5F0;
    color: #FF6129;
}

</style>