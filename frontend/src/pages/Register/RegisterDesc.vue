<template>
    <ProgressHeader 
      @go-back="handleClickBtn('goToBack')"
      :totalSteps="4" :currentStep="4"
    />

    <v-container class="justify-center | pr-4 | pl-4 | pt-0">
      <RegisterHeader :title="title" :desc="desc"/>

      <v-row no-gutters class="justify-center">
        <v-textarea
          placeholder="예: ENTJ, 1학년인데 취업에 관심 있는 사람들과 대화 나누고 싶어요" 
          hide-details
          variant="outlined" density="comfortable" rounded="lg" bg-color="#FFFFFF" base-color="#E5E8EB" color="#E5E8EB"
          class="inputbox"
          v-model="userDesc"
          @input="handleInputChange('input')"
          :maxlength="maxCharLength"
        />
      </v-row>
      <v-row no-gutters class="justify-end | label-text-small | mt-1">
        {{ userDesc.length }}/{{ maxCharLength }} 
      </v-row>

      <v-row no-gutters class="justify-start | label-text | mt-10">
        💡 이런 내용을 추천해요
      </v-row>
      <v-row 
          v-for="(text, index) in recmList" :key="index"
          cols="12" class="recm-item | mt-2" no-gutters
          :style="{ cursor: 'default' }" 
      >
        {{ text }}
      </v-row>

    </v-container>

    <ProgressFooter
      @go-next="handleClickBtn('goToNext')"
      :active="active"
    />

    <!-- 다이얼로그 -->
    <v-dialog v-model="dialog.isActive" width="100%">
    <v-card style="padding: 24px 16px; border-radius: 24px;">
      <v-btn 
        icon="mdi-close" variant="text" size="small"
        v-if="!dialog.isOneBtn"
        @click="dialog.isActive = false"
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
import { onMounted, onUnmounted, ref, watch } from "vue";
import { useRouter, useRoute } from "vue-router";
import ProgressFooter from "@/components/ProgressFooter.vue";
import RegisterHeader from "@/components/RegisterHeader.vue";
import { navigateTo } from '@/common/RouterUtil.js';
const router = useRouter(); 
const active = ref(false);

const emit = defineEmits(['hide-top-appbar', 'hide-bottom-appbar']);

const dialog = ref({
  title: '',
  text: '',
  isActive: false,
  isOneBtn: false,
  okText: '확인',
  okButton() {}
});


const title = "한줄 소개";
const desc = "나를 소개할 수 있는 한마디를 작성해주세요";

const userDesc = ref("");
const maxCharLength = 100; // 최대 글자수 상수로 정의

const recmList = ref([
    '• MBTI와 학년 정보',
    '• 관심 분야나 목표',
    '• 함께하고 싶은 활동'
]);

// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-top-appbar');
  emit('hide-bottom-appbar');
});

onUnmounted(() => {

});

// ----- 함수 정의 ----- //

function handleInputChange(action) {
  switch (action) {
    case 'input':
      const length = userDesc.value?.length ?? 0;

      if (length > maxCharLength) {
          userDesc.value = userDesc.value.slice(0, maxCharLength);
      }
      
      active.value = userDesc.value.length > 0 && userDesc.value.length <= maxCharLength;
      break;
  }
}

function handleClickBtn(action) {
  switch (action) {
    case 'goToBack':
      navigateTo(router, '/register/time');
      break;

    case 'goToNext':
      openDialog(
        "회원가입 완료!", 
        "이제 비슷한 관심사를 가진<br/>학우들과 연결될 준비가 완료되었어요.", 
        () => {
          dialog.value.isActive = false;
          navigateTo(router, '/');
        },
        true, 
        "시작하기"
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
  dialog.value.isActive = true;
  dialog.value.isOneBtn = isOneBtn || false;
  dialog.value.okText = okText || '확인';
}
</script> 

<style scoped>
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

.recm-item {
  color: #4A5565;
  padding: 8px 12px;
  font-size: 14px;
  font-weight: 400;
  background-color: #FFFFFF;
  border-radius: 12px;
  border: #E5E7EB 0.6px solid;
}
</style>