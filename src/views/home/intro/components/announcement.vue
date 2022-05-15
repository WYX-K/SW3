<template>
  <a-card
    class="general-card"
    :title="t('poster.home.announcement')"
    :header-style="{ paddingBottom: '0' }"
    :body-style="{ padding: '15px 20px 13px 20px' }"
  >
    <a-tag color="blue" size="small">
      Conference Info:
    </a-tag>
    <span class="item-content">
      {{ conInfo.list.date }}
      {{ conInfo.list.time }}
    </span>
    <div v-for="(item, idx) in list" :key="idx" class="item">
      <a-tag v-if="item.isShown" :color="item.type" size="small">{{ item.label }}</a-tag>
      <span v-if="item.isShown" class="item-content">
        {{ item.content }}
      </span>
    </div>
  </a-card>
</template>

<script lang="ts" setup>
import { onMounted, reactive } from 'vue'
import { useI18n } from 'vue-i18n/index'
import { getLuckyDraw } from '@/api/luckydraw'
import { getConInfo } from '@/api/conInfo'

const { t } = useI18n()
const list = reactive([
  {
    type: 'orangered',
    label: 'Lucky Draw',
    content: 'Lucky has been born',
    isShown: false
  }
])
const conInfo = reactive({
  list: {
    time: '',
    date: '',
    content: ''
  }
})
onMounted(async () => {
  let res = await getLuckyDraw()
  if (res.status === 200) {
    list[0].isShown = true
  }
  res = await getConInfo()
  conInfo.list = res.data.data
  console.log(conInfo.list)
})
</script>

<style scoped lang="less">
  .item {
    display: flex;
    align-items: center;
    width: 100%;
    height: 24px;
    margin-bottom: 4px;
    .item-content {
      flex: 1;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      margin-left: 4px;
      color: var(--color-text-2);
      text-decoration: none;
      font-size: 13px;
      cursor: pointer;
    }
  }
</style>
