import localeLogin from '@/views/login/locale/zh-CN'
import localeSettings from './zh-CN/settings'
import localeHome from '@/views/home/intro/locale/zh-CN'
import localePosterVote from '@/views/poster/show&vote/locale/zh-CN'
import localePosterUpload from '@/views/poster/upload/locale/zh-CN'
import localePosterEdit from '@/views/poster/edit/locale/zh-CN'
import localePosterGrade from '@/views/poster/grade/locale/zh-CN'

export default {
  'menu.home': '主页',
  'menu.home.intro': '介绍',
  'menu.poster': '海报',
  'menu.luckydraw': '抽奖',
  'menu.poster.show': '展示 & 投票',
  'menu.poster.upload': '上传',
  'menu.poster.edit': '编辑',
  'menu.poster.grade': '评分',
  'menu.luckydraw.choose': '选择',
  'navbar.action.locale': '切换为中文',
  'navbar.search.placeholder': '请输入关键字',
  ...localeSettings,
  ...localeLogin,
  ...localeHome,
  ...localePosterVote,
  ...localePosterUpload,
  ...localePosterEdit,
  ...localePosterGrade
}
