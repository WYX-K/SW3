import { createApp } from 'vue'
import ArcoVue from '@arco-design/web-vue'

import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router/index'
import '@arco-design/web-vue/dist/arco.css'

const app = createApp(App)
app.use(ArcoVue, {
  componentPrefix: 'arco',
})

.use(createPinia())
app.use(router)
app.mount('#app')