import { createApp } from 'vue'
import ArcoVue from '@arco-design/web-vue'

import { createPinia } from 'pinia'
import router from './router/index'
import '@arco-design/web-vue/dist/arco.css'
import App from './App.vue'

const app = createApp(App)

app.use(ArcoVue, {
  componentPrefix: 'arco',
}).use(createPinia()).use(router)
app.mount('#app')