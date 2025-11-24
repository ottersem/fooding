<template>
    <v-container class="pa-0">
        <v-row no-gutters>
            <RegisterHeader :title="title" :desc="desc"/>
        </v-row>

        <v-row no-gutters class="justify-center mt-4">
            <v-col 
                v-for="(group, index) in groupList" 
                :key="index"
                cols="12"
                class="mb-4"
            >
                <v-card 
                    class="meeting-card" 
                    variant="outlined"
                >
                    <v-row no-gutters class="pa-4 pb-0 align-center">
                        <v-col cols="auto" class="mr-3">
                            <v-avatar size="56" color="#E0E0E0"></v-avatar> 
                        </v-col>
                        <v-col>
                            <div class="card-title">{{ group.title }}</div>
                            <v-row no-gutters class="align-center mt-1">
                                <v-chip size="small" class="tag-chip mr-2" prepend-icon="mdi-coffee">커피챗</v-chip>
                                <span class="category-text">커리어</span>
                            </v-row>
                        </v-col>
                        <v-col cols="auto">
                            <div class="people-count">
                                <v-icon size="20" class="mr-1">mdi-account-group</v-icon>
                                <span>2/4</span>
                            </div>
                        </v-col>
                    </v-row>

                    <v-card-text class="pt-2 pb-4 description-text">
                        {{ group.description }}
                    </v-card-text>

                    <v-row no-gutters class="px-4 pb-4 info-section">
                        <v-col cols="auto" class="mr-4 align-center d-flex">
                            <v-icon size="18" class="mr-1">mdi-clock-time-four-outline</v-icon>
                            <span>{{ group.meetingTime }}</span>
                        </v-col>
                        <v-col cols="auto" class="align-center d-flex">
                            <v-icon size="18" class="mr-1">mdi-map-marker-outline</v-icon>
                            <span>{{ group.meetingLocation }}</span>
                        </v-col>
                    </v-row>

                    <v-card-actions class="pa-4 pt-0">
                        <v-btn 
                            v-if="group.status === 'PENDING'"
                            block 
                            class="apply-button" 
                            flat
                            @click="handleAction('apply', group.status)"
                        >
                            매칭 신청하기
                        </v-btn>
                        
                        <v-btn 
                            v-else-if="group.status === 'APPLIED'"
                            block 
                            class="apply-button cancel-button" 
                            flat
                            @click="handleAction('cancel', group.status)"
                        >
                            매칭 취소하기
                        </v-btn>

                        <v-btn 
                            v-else-if="group.status === 'ACCEPTED'"
                            block 
                            class="apply-button accepted-button" 
                            flat
                            @click="handleAction('accept', group.status)"
                        >
                            매칭 수락완료
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref, watch } from "vue";
import { useRouter, useRoute } from "vue-router";

const emit = defineEmits(['hide-top-appbar']);
const router = useRouter(); 


const title = "이번주 밥약/커피챗 신청";
const desc = "지금 선택한 관심사와 시간대에 맞춰 추천된 모임을 보여드릴게요";


const groupList = ref([
  {
    title: "취업고민 같이 나눠요.",
    description: "취업 준비하면서 느끼는 고민들 편하게 얘기해요. 같은 목표를 가진 사람끼리 정보도 공유하고 동기부여도 받아요!",
    meetingTime: "19:00-20:00",
    meetingLocation: "카페 블루보틀",
    status: 'PENDING', 
  },
  {
    title: "취업고민 같이 나눠요.",
    description: "새로운 학기 시작! 함께 공부할 동기나 선후배를 찾아요. 전공 지식 공유와 팀플을 위한 모임입니다.",
    meetingTime: "14:00-16:00",
    meetingLocation: "학교 도서관 3층 스터디룸",
    status: 'APPLIED', 
  },
  {
    title: "취업고민 같이 나눠요.",
    description: "운동 친구 구합니다! 주 3회 저녁 시간대에 헬스장 같이 갈 사람 모여라~ 초보자 환영!",
    meetingTime: "20:30-22:00",
    meetingLocation: "학교 체육관 헬스장",
    status: 'ACCEPTED', 
  },
]);


// ----- 라이프 사이클 ----- //
onMounted(() => {
    
});

onUnmounted(() => {

});

// ----- 함수 정의 ----- //
function handleAction(actionType, currentStatus) {
    console.log(`모임 액션 발생: ${actionType} (현재 상태: ${currentStatus})`);
}

</script> 

<style scoped>
.meeting-card {
    border-radius: 12px;
}

.card-title {
    font-size: 16px;
    font-weight: 600;
    color: #364153;
}

.tag-chip {
    background-color: #E6F3FF;
    color: #1A73E8;
    font-size: 12px;
}

.category-text {
    font-size: 12px;
    color: #6A7282;
}

.people-count {
    display: flex;
    align-items: center;
    font-size: 14px;
    color: #364153;
}

.description-text {
    font-size: 14px;
    color: #4A5565;
    line-height: 1.4;
}

.info-section span {
    font-size: 13px;
    color: #6A7282;
}

.apply-button {
    text-transform: none; 
    font-weight: 600;
    min-height: 48px;
    border-radius: 8px;
    background-color: #FF6129;
    color: #FFFFFF;
}

.cancel-button {
    background-color: #F4F6F9;
    color: #6A7282;
    border: 1px solid #E5E7EB;
}

.accepted-button {
    background-color: #F4F6F9;
    color: #6A7282;
}
</style>