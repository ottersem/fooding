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
</template>

<script setup>
// ----- 선언부 ----- //
import { onMounted, onUnmounted, ref, watch, computed } from "vue";
import { useRouter, useRoute } from "vue-router";
import { navigateTo } from '@/common/RouterUtil.js';

const router = useRouter(); 

const emit = defineEmits(['hide-bottom-appbar']);

const userName = ref("고예경")

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
      navigateTo(router, '/user-profile');
      break;

    case 'goToReview':
      // navigateTo(router, '/user-profile');
      break;

    case 'logout':
      break;

    default:
      console.error('알 수 없는 액션 타입:', action);
  }
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