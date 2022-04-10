import { createApp } from 'vue'
import ArcoVue from '@arco-design/web-vue'

import App from './App.vue'
import store from './store'
import router from './router/index'
import '@arco-design/web-vue/dist/arco.css'

const app = createApp(App)
app.use(ArcoVue, {
  componentPrefix: 'arco',
})

app.use(store)
app.use(router)
app.mount('#app')