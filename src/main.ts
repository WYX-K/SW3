import { createApp } from 'vue'

import '@arco-design/web-vue/dist/arco.css'
import '@/assets/style/global.less'
import { createPinia } from 'pinia'
import ArcoVue from '@arco-design/web-vue'
import ArcoVueIcon from '@arco-design/web-vue/es/icon'
import i18n from './locale'
import router from './router/index'
import App from './App.vue'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(ArcoVue, {})
app.use(i18n)
app.use(ArcoVueIcon)
app.mount('#app')