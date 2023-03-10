import { computed } from 'vue'
import { useI18n } from 'vue-i18n/index'
import { Message } from '@arco-design/web-vue'

export default function useLocale() {
  const i18 = useI18n()
  const currentLocale = computed(() => i18.locale.value)
  const changeLocale = (value: string) => {
    i18.locale.value = value
    sessionStorage.setItem('arco-locale', value)
    Message.success(i18.t('navbar.action.locale'))
  }
  return {
    currentLocale,
    changeLocale,
  }
}
