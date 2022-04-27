<template>
  <a-col class="banner">
    <a-typography-title :heading="5" style="margin-top: 0">
      {{ t('luckydraw.choose.welcome') }}
    </a-typography-title>
    <a-divider class="panel-border" />
    <a-button 
      type="primary"
      style="margin-bottom: 20px;"
      @click="onLuckydraw"
    >
      {{ t('luckydraw.choose.btn') }}
    </a-button>
    <a-table :pagination="pagination" :columns="columns" :data="data" />
  </a-col>
</template>

<script lang="ts" setup>
import { reactive, computed } from 'vue'
import { useI18n } from 'vue-i18n/index'

const { t } = useI18n()

const columns = [
  {
    title: computed(() => t('choose.table.username')),
    dataIndex: 'username',
  },
  {
    title: computed(() => t('choose.table.name')),
    dataIndex: 'name',
  },
]
const data = reactive([])

const pagination = reactive({
  pageSize: 10,
  current: 1,
  total: data.length,
  hideOnSinglePage: true
})

const onLuckydraw = () => {
  console.log('onLuckydraw')
}
</script>

<style lang='less' scoped>
    .banner {
    width: 100%;
    padding: 20px 20px 0 20px;
    background-color: var(--color-bg-2);
    border-radius: 4px 4px 0 0;
  }

</style>