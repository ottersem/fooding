/**
 * plugins/vuetify.js
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'
import { aliases, mdi } from 'vuetify/iconsets/mdi'

// SVG Icons (assets/icons)
import IconCalendar from '@/assets/icons/calender.svg?component'
import IconClock from '@/assets/icons/clock-icon.svg?component'
import IconLocation from '@/assets/icons/location-icon.svg?component'
import IconPeople from '@/assets/icons/people-icon.svg?component'
import IconShineFill from '@/assets/icons/shine-icon-fill.svg?component'
import IconShineLine from '@/assets/icons/shine-icon-line.svg?component'

const customAliases = {
  ...aliases,

  'cus-calendar': IconCalendar,
  'cus-clock': IconClock,
  'cus-location': IconLocation,
  'cus-people': IconPeople,
  'cus-shine-fill': IconShineFill,
  'cus-shine-line': IconShineLine,
}

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
export default createVuetify({
  theme: {
    defaultTheme: 'light',
    themes: {
      light: {
        colors: {
          surface: '#F9FAFB', // 배경색을 설정
          background: '#F9FAFB', // 배경색을 설정
        },
        variables: {
          'body-font-family': '"Pretendard Variable", Pretendard, -apple-system, BlinkMacSystemFont, system-ui, Roboto, "Helvetica Neue", "Segoe UI", "Apple SD Gothic Neo", "Noto Sans KR", "Malgun Gothic", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", sans-serif',
        },
      }
    }
  },
      
  icons: {
    defaultSet: 'mdi',
    aliases: customAliases,
    sets: {
      mdi,
    },
  }
})
