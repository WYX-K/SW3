import localeLogin from '@/views/login/locale/zh-CN'
import localeSettings from './zh-CN/settings'
import localeWorkplace from '@/views/dashboard/home/locale/zh-CN'

export default {
  'menu.dashboard': '仪表盘',
  'navbar.action.locale': '切换为中文',
  ...localeSettings,
  ...localeLogin,
  ...localeWorkplace
}
