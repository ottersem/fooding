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
                    class="meeting-card | pa-5" 
                    variant="outlined"
                >
                    <v-row no-gutters class="pb-0 | align-center">
                        <v-col cols="auto" class="mr-4">
                            <v-avatar size="48" color="#E0E0E0"></v-avatar> 
                        </v-col>
                        <v-col>
                            <div class="card-title">{{ group.title }}</div>
                            <v-row no-gutters class="align-center | mt-1">
                                <v-chip size="small" class="tag-chip | mr-2" prepend-icon="mdi-coffee">커피챗</v-chip>
                                <v-col class="category-text">커리어</v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="auto">
                            <div class="people-count">
                                <v-icon size="20" class="mr-1" icon="$cus-people"/>
                                <span>2/4</span>
                            </div>
                        </v-col>
                    </v-row>

                    <v-card-text class="pa-0 | mt-4 | mb-4 | description-text">
                        {{ group.description }}
                    </v-card-text>

                    <v-row no-gutters class="info-section">
                        <v-col cols="auto" class="mr-4 | align-center | d-flex">
                            <v-icon color="#6A7282" size="18" class="mr-1">mdi-clock-time-four-outline</v-icon>
                            <span>{{ group.meetingTime }}</span>
                        </v-col>
                        <v-col cols="auto" class="align-center | d-flex">
                            <v-icon color="#6A7282" size="18" class="mr-1">mdi-map-marker-outline</v-icon>
                            <span>{{ group.meetingLocation }}</span>
                        </v-col>
                    </v-row>

                    <v-card-actions class="pa-0 | mt-4">
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
    background-color: #F0F5FF;
    color: #3B82F6;
    font-size: 12px;
    padding-left: 8px;
    padding-right: 8px;
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

.apply-button {
    font-weight: 600;
    font-size: 13px;
    letter-spacing: -0.08px;
    min-height: 40px;
    border-radius: 12px;
    border: 0.67px solid #E5E7EB;
    background-color: #FFFFFF;
    color: #191F28;
}

.cancel-button {
    font-weight: 600;
    font-size: 13px;
    letter-spacing: -0.08px;
    min-height: 40px;
    border-radius: 12px;
    border: 0.67px solid #E5E7EB;
    background-color: #FFFFFF;
    color: #191F28;
}

.accepted-button {
    font-weight: 600;
    font-size: 13px;
    letter-spacing: -0.08px;
    min-height: 40px;
    border-radius: 12px;
    border: 0.67px solid #FF6129;
    background-color: #FFF5F0;
    color: #FF6129;
}
</style>