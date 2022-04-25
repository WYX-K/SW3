import localeLogin from '@/views/login/locale/en-US'
import localeSettings from './en-US/settings'
import localeHome from '@/views/home/intro/locale/en-US'
import localePosterVote from '@/views/poster/show&vote/locale/en-US'
import localePosterUpload from '@/views/poster/upload/locale/en-US'
import localePosterEdit from '@/views/poster/edit/locale/en-US'

export default {
  'menu.home': 'Home',
  'menu.home.intro': 'Introduction',
  'navbar.action.locale': 'Switch to English',
  'menu.poster': 'Poster',
  'menu.poster.show': 'Show & Vote',
  'menu.poster.upload': 'Upload',	
  'menu.poster.edit': 'Edit',
  'navbar.search.placeholder': 'Please enter the keyword',
  ...localeSettings,
  ...localeLogin,
  ...localeHome,
  ...localePosterVote,
  ...localePosterUpload,
  ...localePosterEdit,
}
