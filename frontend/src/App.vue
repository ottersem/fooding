<template>
  <v-app class="background">
    <v-app-bar app color="#FFFFFF" flat height="100" v-if="sAppBar">
      <v-row class="align-center | justify-space-between | padding-32 | padding-top-56 | padding-bottom-16">
        <!-- 로고 -->
        <v-col cols="auto">
          <v-row class="align-center | pl-3">
            <v-img 
            src="@/assets/logo.svg"
            :width="84" :height="30"
            min-width="84px" min-height="30px" 
            ></v-img>
          </v-row>
        </v-col>
        <v-col cols="8">
          <v-row v-if="sHeader" class="align-center | justify-end | pr-2">
            <v-col cols="auto" class="progress-bar">
                <div
                v-for="(step, index) in 7"
                :key="index"
                class="circle"
                :class="{ active: index === pageIndex }"
                >
                <div class="line" v-if="index !== 6"></div>
                </div>
            </v-col>
          </v-row>
        </v-col>
        <v-divider class="margin-top-16" />
      </v-row>
    </v-app-bar>

    <v-main>
      <router-view
        @hide-appbar="emitHideAppbar"
      ></router-view>
    </v-main>

  </v-app>

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
          <v-icon size="64" color="#FF6129" icon="$cus-complete-icon"/>
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
  console.log(import.meta.env)
});

onUnmounted(() => {

});


// ----- 함수 정의 ----- //
function initSurvey() {
  localStorage.setItem('appInitialized', 'true');
  localStorage.setItem('userSurvey', JSON.stringify(survey.value));
  localStorage.removeItem('surveyId');
  surveyId.value = null;

  console.log("set localStorage appInitialized:", localStorage.getItem('appInitialized'))
  console.log("set localStorage userSurvey:", localStorage.getItem('userSurvey'))
}

function emitHideAppbar() {
  console.log('Event Received: hide appbar');
  sFooter.value = false;
};

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

</style>
