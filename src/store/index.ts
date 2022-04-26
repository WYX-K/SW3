import { createPinia } from 'pinia'
import useUserStore from './modules/user'
import useAppStore from './modules/app'
import useGradeStore from './modules/grade'

const pinia = createPinia()

export { useAppStore, useUserStore, useGradeStore }

export default pinia