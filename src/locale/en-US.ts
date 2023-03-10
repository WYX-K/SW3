import localeLogin from '@/views/login/locale/en-US'
import localeSettings from './en-US/settings'
import localeHome from '@/views/home/intro/locale/en-US'
import localePosterVote from '@/views/poster/show&vote/locale/en-US'
import localePosterUpload from '@/views/poster/upload/locale/en-US'
import localePosterEdit from '@/views/poster/edit/locale/en-US'
import localePosterGrade from '@/views/poster/grade/locale/en-US'
import localeLuckydrawChoose from '@/views/luckydraw/choose/locale/en-US'
import localeRules from '@/views/home/rules/locale/en-US'

export default {
  'menu.home': 'Home',
  'menu.home.intro': 'Introduction',
  'navbar.action.locale': 'Switch to English',
  'menu.luckydraw': 'Lucky Draw',
  'menu.home.rules': 'Rules',
  'menu.poster': 'Poster',
  'menu.poster.show': 'Show & Vote',
  'menu.poster.upload': 'Upload',	
  'menu.poster.edit': 'Edit',
  'menu.poster.grade': 'Grade',
  'menu.luckydraw.choose': 'Choose',
  'navbar.search.placeholder': 'Please enter the keywords of title',
  ...localeSettings,
  ...localeLogin,
  ...localeHome,
  ...localePosterVote,
  ...localePosterUpload,
  ...localePosterEdit,
  ...localePosterGrade,
  ...localeLuckydrawChoose,
  ...localeRules
}
