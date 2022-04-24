import localeLogin from '@/views/login/locale/en-US'
import localeSettings from './en-US/settings'
import localeHome from '@/views/home/intro/locale/en-US'
import localePoster from '@/views/poster/show&vote/locale/en-US'

export default {
  'menu.home': 'Home',
  'menu.home.intro': 'Introduction',
  'navbar.action.locale': 'Switch to English',
  'menu.poster': 'Poster',
  'menu.poster.show': 'Show & Vote',
  ...localeSettings,
  ...localeLogin,
  ...localeHome,
  ...localePoster,
}
