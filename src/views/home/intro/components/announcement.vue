<template>
  <a-card
    class="general-card"
    :title="t('poster.home.announcement')"
    :header-style="{ paddingBottom: '0' }"
    :body-style="{ padding: '15px 20px 13px 20px' }"
  >
    <div v-if="isData">
      <div v-for="(item, idx) in list" :key="idx" class="item">
        <a-tag :color="item.type" size="small">{{ item.label }}</a-tag>
        <span class="item-content">
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
import { computed } from 'vue'
import { useI18n } from 'vue-i18n/index'

const { t } = useI18n()
const list = [
  // {
  //   type: 'orangered',
  //   label: '活动',
  //   content: '内容最新优惠活动',
  // },
  // {
  //   type: 'cyan',
  //   label: '消息',
  //   content: '新增内容尚未通过审核，详情请点击查看。',
  // },
  // {
  //   type: 'blue',
  //   label: '通知',
  //   content: '当前产品试用期即将结束，如需续费请点击查看。',
  // },
  // {
  //   type: 'blue',
  //   label: '通知',
  //   content: '1月新系统升级计划通知',
  // },
  // {
  //   type: 'cyan',
  //   label: '消息',
  //   content: '新增内容已经通过审核，详情请点击查看。',
  // },
]

const isData = computed(() => list.length > 0)
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
