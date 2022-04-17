import localeLogin from '@/views/login/locale/zh-CN'
import localeSettings from './zh-CN/settings'
import localeHome from '@/views/home/intro/locale/zh-CN'

export default {
  'menu.home': '主页',
  'menu.home.intro': '介绍',
  'menu.poster': '海报',
  'menu.poster.show': '展示',
  'navbar.action.locale': '切换为中文',
  ...localeSettings,
  ...localeLogin,
  ...localeHome
}
