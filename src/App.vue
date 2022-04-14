<template>
  <a-config-provider :locale="locale">
    <router-view></router-view>
  </a-config-provider> 
</template>

<script lang="ts" setup>
import { computed } from 'vue'
import enUS from '@arco-design/web-vue/es/locale/lang/en-us'
import zhCN from '@arco-design/web-vue/es/locale/lang/zh-cn'
import useLocale from '@/hooks/locale'

if (performance.navigation.type !== 1) {
  localStorage.clear()
}
const { currentLocale } = useLocale()
document.body.removeAttribute('arco-theme')
const locale = computed(() => {
  switch (currentLocale.value) {
    case 'zh-CN':
      return zhCN
    case 'en-US':
      return enUS
    default:
      return enUS
  }
})
</script>

<style>

</style>
