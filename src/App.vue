<template>
  <login></login>
  {{ isLoginStore.islogin }}
</template>

<script lang="ts" setup>
import login from './views/login/login.vue'
import useIsLoginStore from './store/index'

const isLoginStore = useIsLoginStore()
</script>

<style>

</style>
