<template>
    <v-container 
      class="justify-center | mb-12"
      style="height: 100%;"
    >
      <v-row no-gutters class="justify-start | label-text">
        제목
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-text-field
          v-model="groupTitle"
          placeholder="모임 제목을 입력하세요" 
          class="inputbox"
          variant="outlined" density="comfortable" rounded="lg" bg-color="#FFFFFF" base-color="#E5E8EB" color="#E5E8EB"
        />
      </v-row>

      <v-row no-gutters class="justify-start | label-text">
        설명
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-textarea
          placeholder="모임에 대한 설명을 입력하세요" 
          hide-details
          variant="outlined" density="comfortable" rounded="lg" bg-color="#FFFFFF" base-color="#E5E8EB" color="#E5E8EB"
          class="inputbox"
          v-model="groupDescription"
          @input="handleInputChange('input')"
          :maxlength="maxCharLength"
        />
      </v-row>
      <v-row no-gutters class="justify-end | label-text-small | mt-1 | mb-2">
        {{ groupDescription.length }}/{{ maxCharLength }} 
      </v-row>

      <v-row no-gutters class="justify-start | label-text">
        관심분야
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-select
          v-model="selectedInterestId"
          :items="interestList"
          item-title="text"
          item-value="interestId"
          placeholder="관심분야를 선택하세요 (최대 2개)" 
          class="inputbox"
          variant="outlined" density="comfortable" rounded="lg" bg-color="#FFFFFF" base-color="#E5E8EB" color="#E5E8EB"
          multiple chips closable-chips
          @update:model-value="handleInputChange('interest', $event)"
        />
      </v-row>

      <v-row no-gutters class="justify-start | label-text">
        날짜
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-text-field
          v-model="meetingDate"
          placeholder="YYYY-MM-DD" 
          class="inputbox"
          variant="outlined" density="comfortable" rounded="lg" bg-color="#FFFFFF" base-color="#E5E8EB" color="#E5E8EB"
        />
      </v-row>

      <v-row no-gutters class="justify-start | label-text">
        시간
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-select
          v-model="selectedTimeSlotId"
          :items="timeSlotList"
          item-value="timeSlotId"
          placeholder="시간대를 선택하세요" 
          class="inputbox"
          variant="outlined" density="comfortable" rounded="lg" bg-color="#FFFFFF" base-color="#E5E8EB" color="#E5E8EB"
        >
          <template v-slot:item="{ props, item }">
            <v-list-item v-bind="props" :title="`${item.raw.text} (${item.raw.time})`" />
          </template>
          <template v-slot:selection="{ item }">
            <span v-if="item">{{ item.raw.text }} ({{ item.raw.time }})</span>
          </template>
        </v-select>
      </v-row>

      <v-row no-gutters class="justify-start | label-text">
        최대인원
      </v-row>
      <v-row no-gutters class="justify-center | mt-1">
        <v-text-field
          v-model="maxParticipants"
          placeholder="최대 인원 수를 입력하세요" 
          type="number"
          class="inputbox"
          variant="outlined" density="comfortable" rounded="lg" bg-color="#FFFFFF" base-color="#E5E8EB" color="#E5E8EB"
        />
      </v-row>

      <v-row no-gutters class="justify-start | label-text">
        장소
      </v-row>
      <v-row no-gutters class="justify-center | mt-1 | mb-12">
        <v-text-field
          v-model="meetingPlace"
          placeholder="모임 장소를 입력하세요" 
          class="inputbox"
          variant="outlined" density="comfortable" rounded="lg" bg-color="#FFFFFF" base-color="#E5E8EB" color="#E5E8EB"
        />
      </v-row>
    </v-container>

    <v-row no-gutters class="justify-space-between | align-center | footer-container">
      <v-btn
        v-if="active"
        variant="outlined"
        class="active-btn"
        @click="handleClickBtn('createGroup')"
      >모임 생성하기</v-btn>
      <v-btn
        v-else
        variant="outlined"
        class="readonly-btn"
        readonly
      >모임 생성하기</v-btn>
    </v-row>


  <!-- 다이얼로그 -->
  <v-dialog v-model="dialog.dialogActive" width="100%">
    <v-card style="padding: 24px 16px; border-radius: 24px;">
      <v-btn 
        icon="mdi-close" variant="text" size="small"
        v-if="!dialog.isOneBtn"
        @click="dialog.dialogActive = false"
        style="position: absolute; top: 12px; right: 12px; color: #6B7280; z-index: 10;"
      />

      <v-card-title>
        <v-row no-gutters class="align-center | justify-center">
          <v-icon size="64" color="#FF6129" icon="$cus-complete"/>
        </v-row>
        <v-row no-gutters class="align-center | justify-center | mt-3"
          style="color: #101828; font-size: 20px; font-weight: 400; letter-spacing: -0.45px;"
        >
          {{ dialog.title }}
        </v-row>
      </v-card-title>

      <v-card-text style="padding: 0px; margin-bottom: 12px;">
        <v-row no-gutters
        style="justify-content: center; text-align: center; color: #6A7282; font-size: 14px; font-weight: 400; letter-spacing: -0.15px;"
        v-html="dialog.text"/>
      </v-card-text>

      <template v-slot:actions>
          <v-btn class="active-btn" style="border-radius: 16px;" variant="outlined" @click="dialog.okButton" :loading="isSubmitting">{{ dialog.okText }}</v-btn>
      </template>
    </v-card>
  </v-dialog>
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref, watch, computed } from "vue";
import { useRouter, useRoute } from "vue-router";
import { navigateTo } from '@/common/RouterUtil.js';


const router = useRouter(); 

const emit = defineEmits(['hide-bottom-appbar']);

const dialog = ref({
  title: '',
  text: '',
  isActive: false,
  isOneBtn: false,
  okText: '확인',
  okButton() {}
});

const active = ref(false);

// 모임 생성 폼 데이터
const groupTitle = ref("");
const groupDescription = ref("");
const selectedInterestId = ref([]);
const meetingDate = ref("");
const selectedTimeSlotId = ref(null);
const maxParticipants = ref(null);
const meetingPlace = ref("");

const maxCharLength = 100; // 최대 글자수 상수로 정의

const timeSlotList = ref([
  { 
    timeSlotId: 1,
    text: '평일 오전', 
    time: '09:00 - 12:00', 
    value: 'weekday_morning'
  },
  { 
    timeSlotId: 2,
    text: '평일 오후', 
    time: '12:00 - 18:00', 
    value: 'weekday_afternoon'
  },
  { 
    timeSlotId: 3,
    text: '평일 저녁', 
    time: '18:00 - 22:00', 
    value: 'weekday_evening'
  },
  { 
    timeSlotId: 4,
    text: '주말 오전', 
    time: '09:00 - 12:00', 
    value: 'weekend_morning'
  },
  { 
    timeSlotId: 5,
    text: '주말 오후', 
    time: '12:00 - 18:00', 
    value: 'weekend_afternoon'
  },
  { 
    timeSlotId: 6,
    text: '주말 저녁', 
    time: '18:00 - 22:00', 
    value: 'weekend_evening'
  },
]);

const interestList = ref([
  { interestId: 1, text: '일상/친목' },
  { interestId: 2, text: '대외활동/공모전' },
  { interestId: 3, text: '커리어' },
  { interestId: 4, text: '스터디' },
  { interestId: 5, text: '취미/여가' },
]);

// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-bottom-appbar');
});

onUnmounted(() => {
  // 필요한 경우 unmounted 시 로직 추가
});

watch([groupTitle, groupDescription, selectedInterestId, meetingDate, selectedTimeSlotId, maxParticipants, meetingPlace], () => {
  active.value = 
    groupTitle.value.trim() !== "" &&
    groupDescription.value.trim() !== "" &&
    selectedInterestId.value.length > 0 &&
    meetingDate.value.trim() !== "" &&
    selectedTimeSlotId.value !== null &&
    maxParticipants.value !== null &&
    maxParticipants.value > 0 &&
    meetingPlace.value.trim() !== "";
}, { deep: true });


// ----- 함수 정의 ----- //
function handleInputChange(action, value) {
  switch (action) {
    case 'input':
      const length = groupDescription.value?.length ?? 0;

      if (length > maxCharLength) {
          groupDescription.value = groupDescription.value.slice(0, maxCharLength);
      }
      break;
    
    case 'interest':
      if (value.length > 2) {
        selectedInterestId.value = value.slice(0, 2);
      }
      break;
  }
}

function handleClickBtn(action) {
  switch (action) {
    case 'createGroup':
      openDialog(
        "모임생성 완료!", 
        "이제 비슷한 관심사를 가진<br/>학우들과 연결될 준비가 완료되었어요.", 
        () => {
          dialog.value.dialogActive = false;
          navigateTo(router, '/group');
        },
        true, 
      );
      break;

    default:
      console.error('알 수 없는 액션 타입:', action);
  }
}

function openDialog(title, text, onConfirm, isOneBtn, okText) {
  dialog.value.title = title;
  dialog.value.text = text;
  dialog.value.okButton = onConfirm;
  dialog.value.dialogActive = true;
  dialog.value.isOneBtn = isOneBtn || false;
  dialog.value.okText = okText || '확인';
}
</script>

<style scoped>
.menu-btn {
  min-height: 56px; 
  border: 0.7px solid #F3F4F6;
  background-color: #FFFFFF;
  color: #364153;
  
  justify-content: space-between;
  padding-left: 16px;
  padding-right: 16px;
}

.inputbox :deep(.v-input__details) {
  padding-top: 4px !important;
}
.inputbox :deep(.v-icon) {
  color: #8B95A1 !important;
  opacity: 1;
}

.label-text {
  font-size: 14px;
  font-weight: 600;
  color: #364153;
}

.label-text-small {
  font-size: 12px;
  font-weight: 400;
  color: #364153;
}

.profile-img-frame {
  border: 1.35px solid #E5E7EB;
}

.footer-container {
  background-color: #FFFFFF;
  padding: 16px;
  border-top: 1px solid #E5E7EB;
  position: fixed;
  bottom: 0;
  width: 100%;
  z-index: 99;
}

.active-btn {
  width: 100%;
  height: 56px;
  border-radius: 16px;
  border: 1.35px solid #FF6129;
  background-color: #FF6129;
  color: #FFFFFF;
  font-size: 16px;
  font-weight: 600;
}

.readonly-btn {
  width: 100%;
  height: 56px;
  border-radius: 16px;
  border: 1.35px solid #E5E7EB;
  background-color: #F3F4F6;
  color: #9CA3AF;
  font-size: 16px;
  font-weight: 600;
}
</style>