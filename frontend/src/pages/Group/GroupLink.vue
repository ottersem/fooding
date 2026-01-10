<template>
    <v-row no-gutters class="header-box">
        <RegisterHeader :title="title" :desc="desc"/>
    </v-row>
    <v-container class="pa-0 | pl-4 | pr-4">
    
        <v-row no-gutters class="justify-center | align-center | info-box | mt-6">
            <v-col cols="12" class="info-title | mb-1">
                카카오톡 오픈채팅 링크 생성 방법
            </v-col>
            <v-col cols="12" class="info-content | pl-2">
                카카오톡 앱을 열어주세요<br/>
                채팅 탭에서 '+' 버튼을 눌러주세요<br/>
                '오픈채팅' 선택<br/>
                '오픈채팅 시작하기' 선택<br/>
                채팅방 이름을 "내리 숨은 맛집 탐방"(으)로 설정<br/>
                생성 후 '초대하기' → '링크 복사'<br/>
                아래 입력란에 링크를 붙여넣기
            </v-col>
        </v-row>

        <v-row no-gutters class="justify-start | label-text | mt-8">
            오픈 채팅 링크
        </v-row>
        <v-row no-gutters class="justify-center | mt-2 | align-center">
            <v-col>
                <v-text-field
                    v-model="grade"
                    placeholder="https://open.kakao.com/o/" 
                    class="inputbox" hide-details
                    variant="outlined" density="comfortable" rounded="lg" bg-color="#FFFFFF" base-color="#E5E8EB" color="#E5E8EB"
                />
            </v-col>
            <v-btn
                icon variant="outlined"
                class="copy-btn"
                @click="handleClickBtn"
            >
                <v-icon color="#99A1AF" size="20">mdi-content-copy</v-icon>
            </v-btn>
        </v-row>
        <v-row no-gutters class="justify-start | label-text-small | mt-2">
            * 링크를 입력하면 모든 참여자에게 자동으로 알림이 전송됩니다.
        </v-row>
    </v-container>
    <SaveFooter
        @go-next="handleClickBtn('saveLink')"
        :active="active"
    />
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, computed, ref } from "vue";
import { useRouter, useRoute } from "vue-router";

const emit = defineEmits(['hide-top-appbar', 'hide-bottom-appbar']);
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
    emit('hide-bottom-appbar');
});

onUnmounted(() => {

});

// ----- 함수 정의 ----- //
const copyLink = () => {
    if (grade.value) {
        navigator.clipboard.writeText(grade.value).then(() => {
            alert('링크가 복사되었습니다!');
        }).catch(err => {
            console.error('복사 실패:', err);
        });
    }
};

const grade = ref('');

function handleClickBtn(action, value) {
  switch (action) {
    case 'saveLink':
      break;

    case 'copyLink':
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

.info-box {
    min-height: 36px; 
    border-radius: 12px;
    border: 0.7px solid #FFE0D4;
    background-color: #FFF4F0;
    color: #FF6129;
    font-size: 12px;
    font-weight: 400;
    padding: 16px 20px;
}

.info-title {
    font-weight: 700;
    line-height: 20px;
}

.info-content {
    font-weight: 400;
    padding-left: 2px;
    line-height: 20px;
}

.label-text {
  font-size: 14px;
  font-weight: 600;
  color: #364153;
}

.label-text-small {
  font-size: 12px;
  font-weight: 400;
  color: #6A7282;
}

.copy-btn {
  margin-left: 8px;
  background-color: #F9FAFB !important;
  border: 0.7px solid #D1D5DC;
  border-radius: 10px;
  padding: 0 16px !important;
  min-width: 52px !important;
  height: 48px !important;
}

.copy-icon {
  color: #99A1AF !important;
}

</style>