<template>
  <a-col class="banner">
    <a-typography-title :heading="5" style="margin-top: 0">
      {{ t('luckydraw.choose.welcome') }}
    </a-typography-title>
    <a-divider class="panel-border" />
    <a-button 
      v-if="isLuckydraw"
      type="primary"
      style="margin-bottom: 20px;"
      @click="onLuckydraw"
    >
      {{ t('luckydraw.choose.btn') }}
    </a-button>
    <a-table :pagination="pagination" :columns="columns" :data="data.list" />
  </a-col>
</template>

<script lang="ts" setup>
import { reactive, computed, onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n/index'
import consola from 'consola'
import { Message } from '@arco-design/web-vue'
import { postLuckyDraw, getLuckyDraw } from '@/api/luckydraw'

const { t } = useI18n()

const columns = [
  {
    title: computed(() => t('choose.table.luckydraw')),
    dataIndex: 'luckydraw',
  },
  {
    title: computed(() => t('choose.table.name')),
    dataIndex: 'name',
  },
  {
    title: computed(() => t('choose.table.username')),
    dataIndex: 'username',
  }
]
const data = reactive({
  list: [],
})

const pagination = reactive({
  pageSize: 10,
  current: 1,
  total: 3,
  hideOnSinglePage: true
})

const onLuckydraw = async () => {
  try {
    await postLuckyDraw()
    Message.success(t('luckydraw.choose.success'))
    getLuckyDrawList()
  } catch (e) {
    consola.error(e)
  }
}
const getLuckyDrawList = async () => {
  const res = await getLuckyDraw()
  if (res.status === 200) {
    data.list = res.data
    isLuckydraw.value = false
  } else {
    isLuckydraw.value = true
  }
}
const isLuckydraw = ref(false)
onMounted(async () => {
  await getLuckyDrawList()
})
</script>

<style lang='less' scoped>
    .banner {
    width: 100%;
    padding: 20px 20px 0 20px;
    background-color: var(--color-bg-2);
    border-radius: 4px 4px 0 0;
  }

</style>