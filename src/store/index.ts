import { createPinia } from 'pinia'
import useUserStore from './modules/user'
import useAppStore from './modules/app'

const pinia = createPinia()

export { useAppStore, useUserStore }

export default pinia