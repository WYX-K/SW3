<template>
  <a-col class="banner">
    <a-typography-title :heading="5" style="margin-top: 0">
      {{ t('home.welcome') }} {{ userInfo.name }}
    </a-typography-title>
    <a-divider class="panel-border" />
    <a-row justify="space-around">
      <a-col :span="8">
        <Carousel></Carousel>
      </a-col>
    </a-row>
  </a-col>
</template>

<script lang="ts" setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n/index'
import { useUserStore } from '@/store'
import Carousel from './carousel.vue'

const { t } = useI18n()
const userStore = useUserStore()
const userInfo = computed(() => ({
  name: userStore.name,
}))
</script>

<style scoped lang="less">
  .banner {
    width: 100%;
    padding: 20px 20px 0 20px;
    background-color: var(--color-bg-2);
    border-radius: 4px 4px 0 0;
  }
</style>