<template>
  <a-config-provider :locale="locale">
    <router-view></router-view>
  </a-config-provider> 
</template>

<script lang="ts" setup>
import { computed, onMounted } from 'vue'
import enUS from '@arco-design/web-vue/es/locale/lang/en-us'
import zhCN from '@arco-design/web-vue/es/locale/lang/zh-cn'
import useLocale from '@/hooks/locale'
import { useUserStore } from '@/store'
import { RoleType } from './store/modules/user/types'

onMounted(() => {
  const { setIsLogin, setRole } = useUserStore()

  if (sessionStorage.getItem('TOKEN')) {
    console.log('onMounted')
    setIsLogin(true)
    setRole(sessionStorage.getItem('ROLE') as RoleType)
  }
})

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
