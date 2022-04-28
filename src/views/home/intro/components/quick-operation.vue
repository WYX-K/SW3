<template>
  <a-card
    class="general-card"
    :title="t('home.quick.operation')"
    :header-style="{ paddingBottom: '0' }"
    :body-style="{ padding: '24px 20px 0 20px' }"
  >
    <a-row :gutter="8">
      <a-col
        v-for="link in links"
        :key="link"
        :span="8"
        class="wrapper"
      >
        <div class="icon">
          <component :is="link.icon" />
        </div>
        <a-typography-paragraph class="text">
          {{ link.text }}
        </a-typography-paragraph>
      </a-col>
    </a-row>
    <a-divider class="split-line" style="margin: 0" />
  </a-card>
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n/index'

const { t } = useI18n()
const links = [
  { text: 'Zoom', icon: 'icon-lark-color' },
  { text: '腾讯会议', icon: 'icon-qq' },
]
</script>

<style scoped lang="less"></style>
