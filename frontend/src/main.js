/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

// router
import router from './router'


const app = createApp(App)

registerPlugins(app)
app.use(router); // 라우터 사용 설정
app.mount('#app')
