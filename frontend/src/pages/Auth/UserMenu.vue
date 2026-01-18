<template>
    <v-container class="orange-card | justify-center">

      <v-row no-gutters class="justify-center">
        <v-avatar size="96" image="https://placehold.co/96X96"/>
      </v-row>
      <v-row no-gutters class="justify-center">
        <v-chip class="profile-chip | mt-4 | mb-12">{{ userName }}</v-chip>
      </v-row>
    </v-container>

    <v-container class="menu-container | justify-center | pr-4 | pl-4 | pt-0">
      <v-row no-gutters class="justify-start">
        <v-btn
          @click="handleClickBtn('goToProfile')"
          variant="outlined" class="menu-btn | border-radius-top" block
        >
          <template v-slot:prepend>
            <v-icon color="#364153" size="large" icon="$cus-profile" class="ml-1"/>
            <v-col>프로필 편집</v-col>
          </template>
          <template v-slot:append>
            <v-icon color="#9CA3AF" size="large" icon="mdi-chevron-right" class="ml-1"/>
          </template>
        </v-btn>
      </v-row>

      <v-row no-gutters class="justify-start">
        <v-btn
          @click="handleClickBtn('goToReview')"
          variant="outlined" class="menu-btn" block
        >
          <template v-slot:prepend>
            <v-icon color="#364153" size="large" icon="$cus-document" class="ml-1"/>
            <v-col>내가 쓴 후기</v-col>
          </template>
          <template v-slot:append>
            <v-icon color="#9CA3AF" size="large" icon="mdi-chevron-right" class="ml-1"/>
          </template>
        </v-btn>
      </v-row>

      <v-row no-gutters class="justify-start">
        <v-btn
          @click="handleClickBtn('logout')"
          variant="outlined" class="menu-btn | red-text | border-radius-bottom" block
        >
          <template v-slot:prepend>
            <v-icon color="#FB2C36" size="large" icon="$cus-logout" class="ml-1"/>
            <v-col>로그아웃</v-col>
          </template>
          <template v-slot:append>
            <v-icon color="#FB2C36" size="large" icon="mdi-chevron-right" class="ml-1"/>
          </template>
        </v-btn>
      </v-row>

    </v-container>

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
        <v-row no-gutters class="justify-space-between" style="gap: 8px;">
          <v-col v-if="!dialog.isOneBtn">
            <v-btn block variant="outlined" class="active-outline-btn" @click="dialog.isActive = false">취소</v-btn>
          </v-col>
          <v-col>
            <v-btn block class="active-btn" variant="outlined" @click="dialog.okButton" :loading="isSubmitting">{{ dialog.okText }}</v-btn>
          </v-col>
        </v-row>
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

const userName = ref("고예경")

const dialog = ref({
  title: '',
  text: '',
  isActive: false,
  isOneBtn: false,
  okText: '확인',
  okButton() {}
});

// ----- 라이프 사이클 ----- //
onMounted(() => {
  emit('hide-bottom-appbar');
});

onUnmounted(() => {
  // 필요한 경우 unmounted 시 로직 추가
});


// ----- 함수 정의 ----- //
function handleClickBtn(action) {
  switch (action) {
    case 'goToProfile':
      navigateTo(router, '/user/profile');
      break;

    case 'goToReview':
      navigateTo(router, '/review');
      break;

    case 'logout':
      openDialog(
        '로그아웃',
        '정말 로그아웃 하시겠습니까?',
        () => {
          dialog.value.isActive = false;
          logout();
          navigateTo(router, '/login');
        },
        false,
        '로그아웃'
      );
      break;

    default:
      console.error('알 수 없는 액션 타입:', action);
  }
}

function logout() {
  localStorage.removeItem('user');
  console.log('사용자가 로그아웃했습니다.');
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
.orange-card {
  background-color: #FF875C;
  position: relative;
  align-content: center;
  height: 280px;
}

.profile-chip {
  color: #FFFFFF;
  background-color: #171F1D;
  border-radius: 12px;
  padding: 8px 20px;
  font-size: 13px;
}

.menu-container {
  margin-top: -56px;

  position: relative;
  z-index: 10;
}

.menu-btn {
  min-height: 56px; 
  border: 0.7px solid #F3F4F6;
  background-color: #FFFFFF;
  color: #364153;
  
  justify-content: space-between;
  padding-left: 16px;
  padding-right: 16px;

  font-size: 15px;
  letter-spacing: -0.2px;

  overflow: hidden;
}

.border-radius-top {
  border-radius: 16px 16px 0px 0px;
}

.border-radius-bottom {
  border-radius: 0px 0px 16px 16px;
}

.red-text {
  color: #FB2C36;
}

.btn-top-radius {
  border-radius: 16px 16px 0px 0px;
}

</style>