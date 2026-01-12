<template>
    <v-container class="pa-0 | pl-4 | pr-4">
        <v-row no-gutters class="align-center | mt-8">
          <v-col class="tags-stack">
            <v-chip v-if="groupInfo.status === 0" class="status-chip | status-chip-recruiting" variant="flat">모집중</v-chip>
            <v-chip v-if="groupInfo.status === 1" class="status-chip | status-chip-applied" variant="flat">신청</v-chip>
            <v-chip v-if="groupInfo.status === 2" class="status-chip | status-chip-ongoing" variant="flat">진행</v-chip>
            <v-chip v-if="groupInfo.status === 3" class="status-chip | status-chip-completed" variant="flat">완료</v-chip>
            
            <v-chip v-if="groupInfo.categoryId === 1" size="small" variant="text" class="category-chip" prepend-icon="mdi-coffee">일상/친목</v-chip>
            <v-chip v-if="groupInfo.categoryId === 2" size="small" variant="text" class="category-chip" prepend-icon="mdi-trophy">대외활동/공모전</v-chip>
            <v-chip v-if="groupInfo.categoryId === 3" size="small" variant="text" class="category-chip" prepend-icon="mdi-briefcase">커리어</v-chip>
            <v-chip v-if="groupInfo.categoryId === 4" size="small" variant="text" class="category-chip" prepend-icon="mdi-book-open-page-variant">스터디</v-chip>
            <v-chip v-if="groupInfo.categoryId === 5" size="small" variant="text" class="category-chip" prepend-icon="mdi-palette">취미/여가</v-chip>
          </v-col>
        </v-row>
        <v-row 
            no-gutters justify="start" 
            class="text-title | mb-1"
        >
            <v-col>{{ groupInfo.title }} {{ groupInfo.id }} {{ groupId }}</v-col>
        </v-row>
        <v-row 
            no-gutters justify="start"
            class="text-subtitle"
        >
            <v-col v-html="groupInfo.description"></v-col>
        </v-row>

        <v-card 
            class="meeting-card | pa-4 | mt-6" 
            variant="outlined"
        >
            <v-row no-gutters class="align-center | card-title">
              관심사
            </v-row>
            <v-row no-gutters class="align-center | mt-3">
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
            <v-row no-gutters class="align-center | card-title">
              모임 정보
            </v-row>

            <v-row no-gutters class="pa-0 | mt-3">
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
        </v-card>

        <v-card 
            class="meeting-card | pa-4 | mt-6" 
            variant="outlined"
        >
            <v-row no-gutters class="align-center | card-title | mb-1">
              참여자
            </v-row>
            <v-row no-gutters class="d-flex | align-center | justify-space-between | card-desc">
              <span>{{ groupInfo.participants.current }}/{{ groupInfo.participants.max }}명 참여중</span>
              <v-btn variant="text" class="manage-btn" @click="handleClickBtn('gotoJoin')">신청자 관리 ></v-btn>
            </v-row>

            <!-- 호스트 -->
            <v-row v-for="host in groupInfo.participants.list.filter(p => p.role === 'HOST')" :key="host.id" no-gutters class="align-center | mt-3">
              <v-icon class="profile-icon" color="#364153" icon="$cus-profile"/>
              <v-col class="d-flex | align-center | justify-space-between | ml-3">
                <div class="card-desc">{{ host.user.name }}</div>
                <v-chip class="part-chip" size="small" variant="flat" prepend-icon="mdi-star-outline">호스트</v-chip>
              </v-col>
            </v-row>

            <!-- 참여자 -->
            <v-row v-for="member in groupInfo.participants.list.filter(p => p.role === 'MEMBER')" :key="member.id" no-gutters class="align-center | mt-3">
              <v-icon class="profile-icon" color="#364153" icon="$cus-profile"/>
              <v-col class="d-flex | align-center | justify-space-between | ml-3">
                <div class="card-desc">{{ member.user.name }}</div>
                <v-chip class="part-chip" size="small" variant="flat">참여자</v-chip>
              </v-col>
            </v-row>
        </v-card>


        <v-row no-gutters class="justify-center | align-center | info-box | mt-6">
          카카오톡 그룹 채팅방에서 그룹원들과 자유롭게 소통하고 만남을 조율해보세요!
        </v-row>

        <v-row no-gutters class="justify-center | align-center | mt-10 | mb-10">
          <v-btn
            variant="outlined"
            class="active-kakao-btn"
            @click="handleClickBtn('gotoKakao')"
          >카카오톡 그룹 채팅 시작하기</v-btn>
          <v-btn
            variant="outlined"
            class="active-outline-btn | mt-2"
            @click="handleClickBtn('goToNext')"
          >신청 취소하기</v-btn>
          <v-btn
            variant="outlined"
            class="active-btn | mt-2"
            @click="handleClickBtn('goToNext')"
          >모임 종료하기</v-btn>
          <v-btn
            variant="outlined"
            class="active-outline-btn | mt-2"
            @click="handleClickBtn('goToNext')"
          >모임 삭제하기</v-btn>
        </v-row>

    </v-container>

  <!-- 카카오 다이얼로그 -->
  <v-dialog v-model="kakaoDialog.dialogActive" width="100%">
    <v-card style="padding: 24px 16px; border-radius: 24px;">
      <v-btn 
        icon="mdi-close" variant="text" size="small"
        @click="kakaoDialog.dialogActive = false"
        style="position: absolute; top: 12px; right: 12px; color: #6B7280; z-index: 10;"
      />

      <v-card-title>
        <v-row no-gutters class="align-center | justify-center">
          <v-icon size="64" color="#FF6129" icon="$cus-complete-icon"/>
        </v-row>
        <v-row no-gutters class="align-center | justify-center | mt-3"
          style="color: #101828; font-size: 20px; font-weight: 400; letter-spacing: -0.45px;"
        >
          {{ kakaoDialog.title }}
        </v-row>
      </v-card-title>

      <v-card-text style="padding: 0px; margin-bottom: 12px;">
        <v-row no-gutters
        style="justify-content: center; text-align: center; color: #6A7282; font-size: 14px; font-weight: 400; letter-spacing: -0.15px;"
        v-html="kakaoDialog.text"/>
      </v-card-text>

      <template v-slot:actions>
          <v-btn class="active-btn" style="border-radius: 16px;" variant="outlined" @click="kakaoDialog.okButton">그룹 채팅 시작하기</v-btn>
      </template>
    </v-card>
  </v-dialog>
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, computed, ref } from "vue";
import { useRouter, useRoute } from "vue-router";
import { navigateTo } from '@/common/RouterUtil.js';
import SaveFooter from '@/components/SaveFooter.vue';

const emit = defineEmits(['hide-top-appbar', 'hide-bottom-appbar']);
const route = useRoute();
const router = useRouter(); 

// 쿼리 파라미터에서 id 가져오기
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

const kakaoDialog = ref({
  title: '',
  text: '',
  isActive: false,
  okButton() {}
});


// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-bottom-appbar');
  
  // 쿼리 파라미터에서 id 가져와서 groupInfo에 적용
  if (groupId.value) {
    groupInfo.value.id = groupId.value;
  }
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
    case 'manageApplicants':
      // 신청자 관리 페이지로 이동
      console.log('신청자 관리');
      break;

    case 'gotoJoin':
      navigateTo(router, '/group/join', { id: groupInfo.value.id });
      break;

    case 'gotoKakao':
      openKakaoDialog(
        '그룹 채팅을 시작하시겠습니까?',
        '그룹 채팅을 시작하면 현재 참여 인원이 확정되며, 모임 상태가 \'진행\'으로 변경됩니다.',
        () => {
          kakaoDialog.value.dialogActive = false;
          navigateTo(router, '/group/link', { id: groupInfo.value.id });
        }
      );
      
      break;

    default:
      console.error('알 수 없는 액션 타입:', action);
  }
}

function openKakaoDialog(title, text, onConfirm) {
  kakaoDialog.value.title = title;
  kakaoDialog.value.text = text;
  kakaoDialog.value.okButton = onConfirm;
  kakaoDialog.value.dialogActive = true;
}


</script> 

<style scoped>
.text-title {
  margin-top: 24px;
  font-size: 18px;
  font-weight: 600;
  color: #101828;
}

.text-subtitle {
  font-size: 14px;
  font-weight: 400;
  color: #4A5565;
}

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
  padding: 16px;
  border-radius: 12px;
  border: 0.7px solid #FFE0D4;
  background-color: #FFEFEA;
  color: #FF6129;
  font-size: 12px;
  font-weight: 400;
}

.profile-icon {
  width: 40px;
  height: 40px;
  border-radius: 100%;
  background-color: #E5E7EB;
  color: #6A7282;
  display: flex;
  align-items: center;
  justify-content: center;
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
  color: #4A5565;
  font-size: 12px;
}

.part-chip {
  background-color: #FFEFEA;
  color: #FF6129;
  font-size: 12px;
}
.part-chip :deep(.v-icon) {
  color: #FF6129 !important;
}

.active-kakao-btn {
  width: 100%;
  height: 48px;
  min-height: 48px;
  background-color: #FEE500;
  border: 0px;
  border-radius: 10px;
  color: #3C1E1E;
  font-size: 16px;
  font-weight: 600;
  letter-spacing: -0.15px;
}

.manage-btn {
  color: #364153 !important;
  font-size: 12px !important;
  font-weight: 400 !important;
  padding: 0 !important;
  min-width: auto !important;
  height: auto !important;
  text-transform: none !important;
  letter-spacing: normal !important;
}

.tag-chip {
  background-color: #F3F4F6;
  color: #4A5565;
  font-size: 12px;
  margin-right: 8px;
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

.description-text {
  font-size: 14px;
  color: #4A5565;
}

.tags-stack {
  display: flex;
  gap: 8px;
  align-content: center;
  justify-content: start;
}

</style>