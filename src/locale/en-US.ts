import localeLogin from '@/views/login/locale/en-US'
import localeSettings from './en-US/settings'
import localeHome from '@/views/home/intro/locale/en-US'

export default {
  'navbar.action.locale': 'Switch to English',
  ...localeSettings,
  ...localeLogin,
  ...localeHome
}
