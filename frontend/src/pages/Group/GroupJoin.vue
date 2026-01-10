<template>
    <v-container class="pa-0">
        <v-row no-gutters class="header-box">
            <RegisterHeader :title="title" :desc="desc"/>
        </v-row>

        <v-row no-gutters class="justify-center | ml-4 | mr-4 | mt-6">
            <v-col 
                v-for="member in groupInfo.participants.list" 
                :key="member.id"
                cols="12"
                class="mb-5"
            >
                <v-card 
                    class="meeting-card | pa-4" 
                    variant="outlined"
                >
                    <v-row no-gutters align="center">
                        <v-col cols="auto">
                            <v-icon class="profile-icon" color="#364153" icon="$cus-profile"/>
                        </v-col>

                        <v-col class="pl-3">
                            <v-row no-gutters>
                                <v-col cols="12" class="member-name">
                                    {{ member.user.name }}
                                </v-col>
                            </v-row>

                            <v-row no-gutters class="mt-1">
                                <v-col cols="12">
                                    <v-chip v-if="groupInfo.interestId === 1" size="small" variant="outlined" class="tag-chip">일상/친목</v-chip>
                                    <v-chip v-if="groupInfo.interestId === 2" size="small" variant="outlined" class="tag-chip">대외활동/공모전</v-chip>
                                    <v-chip v-if="groupInfo.interestId === 3" size="small" variant="outlined" class="tag-chip">커리어</v-chip>
                                    <v-chip v-if="groupInfo.interestId === 4" size="small" variant="outlined" class="tag-chip">스터디</v-chip>
                                    <v-chip v-if="groupInfo.interestId === 5" size="small" variant="outlined" class="tag-chip">취미/여가</v-chip>
                                </v-col>
                            </v-row>
                        </v-col>
                    </v-row>

                    <v-row no-gutters class="justify-center | align-center | mt-4">
                        <v-col cols="6" class="pr-1">
                            <v-btn
                                block variant="outlined" class="refuse-btn"
                                @click="handleClickBtn('joinRefuse')"
                            >
                                거절
                            </v-btn>
                        </v-col>

                        <v-col cols="6" class="pl-1">
                            <v-btn
                                block variant="outlined" class="accept-btn"
                                @click="handleClickBtn('joinAccept')"
                            >
                                수락
                            </v-btn>
                        </v-col>
                    </v-row>

                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, computed, ref } from "vue";
import { useRouter, useRoute } from "vue-router";
import { navigateTo } from '@/common/RouterUtil.js';

const emit = defineEmits(['hide-top-appbar']);
const route = useRoute();
const router = useRouter();  

const groupId = computed(() => route.query.id);

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
  participants: {
    max: 4,
    current: 2,
    list: [
      {
        id: 1,
        userId: 10,
        role: 'HOST',
        status: 'ACCEPTED',
        user: {
          id: 10,
          name: '김철수',
          profileImage: null
        }
      },
      {
        id: 2,
        userId: 15,
        role: 'MEMBER',
        status: 'ACCEPTED',
        user: {
          id: 15,
          name: '이영희',
          profileImage: null
        }
      }
    ]
  },
  status: 0, // 모집중
});

const title = "내리 숨은 맛집 탐방";
const desc = `${groupInfo.value.participants.current || 0}/${groupInfo.value.participants.max}명 참여 중`;

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

    case 'joinRefuse':
      break;

    case 'joinAccept':
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
  border-radius: 12px;
  border: 0.7px solid #E5E7EB;
  background-color: #FFFFFF;
}

.member-row {
    display: grid;
    grid-template-columns: auto 1fr;
    grid-template-rows: auto auto;
    column-gap: 12px;
    row-gap: 6px;
    align-items: center;
}

.profile-icon {
  width: 48px;
  height: 48px;
  border-radius: 100%;
  background-color: #E5E7EB;
  color: #6A7282;
  display: flex; /* 아이콘 내부 정렬용 */
  align-items: center;
  justify-content: center;
}

.member-name {
    font-size: 16px;
    font-weight: 600;
    color: #364153;
    line-height: 20px;
}

.member-tags {
    row-gap: 4px;
}

.card-title {
    font-size: 16px;
    font-weight: 600;
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
    background-color: #FFEFEA;
    border: 0.7px solid #FFE0D4;
    color: #FF6129;
    font-size: 12px;
    margin-right: 8px;
    padding-left: 8px !important;
    padding-right: 8px !important;
}


.refuse-btn {
    width: 100%;
    height: 40px;
    min-height: 40px;
    background-color: #F3F4F6;
    border: 0px;
    border-radius: 10px;
    color: #364153;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: -0.15px;
}
.accept-btn {
    width: 100%;
    height: 40px;
    min-height: 40px;
    background-color: #FF6129;
    border: 0px;
    border-radius: 10px;
    color: #FFFFFF;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: -0.15px;
}

</style>