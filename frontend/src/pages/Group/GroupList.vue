<template>
    <v-container class="pa-0">
        <v-row no-gutters class="header-box">
            <RegisterHeader :title="title" :desc="desc"/>
        </v-row>

        <v-row no-gutters class="justify-center | ml-4 | mr-4 | mt-6">
            <v-col 
                v-for="(group, index) in groupList" 
                :key="index"
                cols="12"
                class="mb-4"
            >
                <v-card 
                    class="meeting-card | pa-4" 
                    variant="outlined"
                    @click="handleClickBtn('goToDetail', group.id)"
                    style="cursor: pointer;"
                >
                    <v-row no-gutters class="pb-0 | align-center">
                        <v-col>
                            <v-row no-gutters class="align-center">
                                <v-chip 
                                    v-if="group.status === 0" 
                                    class="status-chip | status-chip-recruiting"
                                    variant="flat"
                                >
                                    모집중
                                </v-chip>
                                <v-chip 
                                    v-if="group.status === 1" 
                                    class="status-chip | status-chip-applied"
                                    variant="flat"
                                >
                                    신청
                                </v-chip>
                                <v-chip 
                                    v-if="group.status === 2" 
                                    class="status-chip | status-chip-ongoing"
                                    variant="flat"
                                >
                                    진행
                                </v-chip>
                                <v-chip 
                                    v-if="group.status === 3" 
                                    class="status-chip | status-chip-completed"
                                    variant="flat"
                                >
                                    완료
                                </v-chip>
                            </v-row>
                        </v-col>
                        <v-col cols="auto">
                            <div class="people-count">
                                <v-icon size="20" class="mr-1" icon="$cus-people"/>
                                <span>{{ group.currentParticipants || 0 }}/{{ group.maxParticipants }}</span>
                            </div>
                        </v-col>
                    </v-row>

                    <div class="card-title | mt-2">{{ group.title }}</div>

                    <v-row no-gutters class="pa-0 | mt-3 | mb-3">
                        <v-col cols="12" class="mb-1">
                            <v-row no-gutters class="align-center">
                                <v-icon color="#6A7282" size="18" class="mr-1">mdi-clock-time-four-outline</v-icon>
                                <span class="description-text">{{ group.meetingDate }} {{ getTimeSlotText(group.timeSlotId) }}</span>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row no-gutters class="align-center">
                                <v-icon color="#6A7282" size="18" class="mr-1">mdi-map-marker-outline</v-icon>
                                <span class="description-text">{{ group.place }}</span>
                            </v-row>
                        </v-col>
                    </v-row>

                    <v-row no-gutters class="align-center">
                        <v-chip v-if="group.interestId === 1" size="small" class="tag-chip" prepend-icon="mdi-coffee">일상/친목</v-chip>
                        <v-chip v-if="group.interestId === 2" size="small" class="tag-chip" prepend-icon="mdi-trophy">대외활동/공모전</v-chip>
                        <v-chip v-if="group.interestId === 3" size="small" class="tag-chip" prepend-icon="mdi-briefcase">커리어</v-chip>
                        <v-chip v-if="group.interestId === 4" size="small" class="tag-chip" prepend-icon="mdi-book-open-page-variant">스터디</v-chip>
                        <v-chip v-if="group.interestId === 5" size="small" class="tag-chip" prepend-icon="mdi-palette">취미/여가</v-chip>
                    </v-row>
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

const groupList = ref([
  {
    id: 1,
    creatorId: 10,
    interestId: 1, // 일상/친목
    title: "점심 같이 먹을 사람 구해요",
    description: "혼밥보다는 함께 밥 먹으면서 수다떨 사람 찾아요. 편하게 이야기 나눠요!",
    meetingDate: "2025-12-10",
    timeSlotId: 2,
    place: "학생식당 2층",
    maxParticipants: 4,
    currentParticipants: 2,
    status: 0, // 모집중
  },
  {
    id: 2,
    creatorId: 12,
    interestId: 2, // 대외활동/공모전
    title: "공모전 팀원 모집합니다",
    description: "마케팅 공모전 준비할 팀원을 찾습니다. 적극적이고 열정 있는 분 환영해요!",
    meetingDate: "2025-12-11",
    timeSlotId: 3,
    place: "카페 스타벅스",
    maxParticipants: 5,
    currentParticipants: 3,
    status: 1, // 신청
  },
  {
    id: 3,
    creatorId: 15,
    interestId: 3, // 커리어
    title: "취업고민 같이 나눠요",
    description: "취업 준비하면서 느끼는 고민들 편하게 얘기해요. 같은 목표를 가진 사람끼리 정보도 공유하고 동기부여도 받아요!",
    meetingDate: "2025-12-12",
    timeSlotId: 4,
    place: "카페 블루보틀",
    maxParticipants: 4,
    currentParticipants: 4,
    status: 2, // 진행
  },
  {
    id: 4,
    creatorId: 18,
    interestId: 4, // 스터디
    title: "알고리즘 스터디원 구합니다",
    description: "코딩테스트 준비를 위한 알고리즘 스터디 모집합니다. 주 2회 정기 모임 예정이에요.",
    meetingDate: "2025-12-13",
    timeSlotId: 3,
    place: "학교 도서관 3층 스터디룸",
    maxParticipants: 6,
    currentParticipants: 5,
    status: 3, // 완료
  },
  {
    id: 5,
    creatorId: 20,
    interestId: 5, // 취미/여가
    title: "헬스 운동 친구 모집",
    description: "운동 친구 구합니다! 주 3회 저녁 시간대에 헬스장 같이 갈 사람 모여라~ 초보자 환영!",
    meetingDate: "2025-12-14",
    timeSlotId: 5,
    place: "학교 체육관 헬스장",
    maxParticipants: 4,
    currentParticipants: 1,
    status: 0, // 모집중
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
    case 'goToDetail':
      navigateTo(router, '/group/detail', { id: value });
      break;

    default:
      console.error('알 수 없는 액션 타입:', action);
  }
}

</script> 

<style scoped>
.header-box {
    padding-left: 16px;
    padding-right: 16px;
    background-color: #FFFFFF;
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

.tag-chip {
    background-color: #F3F4F6;
    color: #4A5565;
    font-size: 12px;
    padding-left: 16px !important;
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

.status-chip-recruiting {
    background-color: #FEF9C2 !important;
    color: #A65F00 !important;
}

.status-chip-applied {
    background-color: #E6F0FF !important;
    color: #2B7FFF !important;
}

.status-chip-completed {
    background-color: #F3F4F6 !important;
    color: #4A5565 !important;
}

.status-chip-ongoing {
    background-color: #D4F5E9 !important;
    color: #0D9F6E !important;
}

.category-text {
    font-size: 12px;
    color: #8B95A1;
}

.people-count {
    display: flex;
    align-items: center;
    font-size: 14px;
    color: #6A7282;
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