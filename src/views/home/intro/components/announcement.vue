<template>
  <a-card
    class="general-card"
    :title="t('poster.home.announcement')"
    :header-style="{ paddingBottom: '0' }"
    :body-style="{ padding: '15px 20px 13px 20px' }"
  >
    <div v-if="isData">
      <div v-for="(item, idx) in list" :key="idx" class="item">
        <a-tag v-if="item.isShown" :color="item.type" size="small">{{ item.label }}</a-tag>
        <span v-if="item.isShown" class="item-content">
          {{ item.content }}
        </span>
      </div>
    </div>
    <div v-else>
      <a-empty />
    </div>
  </a-card>
</template>

<script lang="ts" setup>
import { computed, onMounted, reactive } from 'vue'
import { useI18n } from 'vue-i18n/index'
import { getLuckyDraw } from '@/api/luckydraw'

const { t } = useI18n()
const list = reactive([
  {
    type: 'orangered',
    label: 'Lucky Draw',
    content: 'Lucky has been born',
    isShown: false
  }
])

const isData = computed(() => list.some(item => item.isShown))
onMounted(async () => {
  const res = await getLuckyDraw()
  if (res.status === 200) {
    list[0].isShown = true
  }
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
