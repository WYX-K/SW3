<template>
  <router-view></router-view>
</template>

<script lang="ts" setup>
import useIsLoginStore from '@/store/index'

const isLoginStore = useIsLoginStore()
console.log(isLoginStore.islogin)
</script>

<style>

</style>
