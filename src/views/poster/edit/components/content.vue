<template>
  <a-col class="banner">
    
  </a-col>
</template>

<script lang="ts" setup>
import { ref, reactive, h } from 'vue'
import { IconSearch } from '@arco-design/web-vue/es/icon'
import { Modal } from '@arco-design/web-vue'
import { useI18n } from 'vue-i18n/index'

const { t } = useI18n()

</script>

<style scoped lang="less">
  .banner {
    width: 100%;
    padding: 20px 20px 0 20px;
    background-color: var(--color-bg-2);
    border-radius: 4px 4px 0 0;
  }

</style>
