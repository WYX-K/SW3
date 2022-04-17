import localeLogin from '@/views/login/locale/en-US'
import localeSettings from './en-US/settings'
import localeWorkplace from '@/views/dashboard/home/locale/en-US'

export default {
  'menu.dashboard': 'Dashboard',
  'navbar.action.locale': 'Switch to English',
  ...localeSettings,
  ...localeLogin,
  ...localeWorkplace
}
