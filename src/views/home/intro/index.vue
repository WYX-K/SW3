<template>
  <div class="container">
    <div class="left-side">
      <div class="panel">
        <Content></Content>
      </div>
    </div>
    <div class="right-side">
      <a-grid :cols="24" :row-gap="16">
        <a-grid-item :span="24">
          <div class="moduler-wrap">
            <QuickOperation />
          </div>
        </a-grid-item>
        <a-grid-item :span="24">
          <div class="moduler-wrap">
            <Announcement />
          </div>
        </a-grid-item>
      </a-grid>
    </div>
  </div>
</template>

<script lang="ts" setup>
import Content from './components/content.vue'
import Announcement from './components/announcement.vue'
import QuickOperation from './components/quick-operation.vue'
</script>

<style lang="less" scoped>
  .container {
    background-color: var(--color-fill-2);
    padding: 16px 20px;
    padding-bottom: 0;
    display: flex;
  }

  .left-side {
    flex: 1;
    overflow: auto;
  }
   .right-side {
    width: 280px;
    margin-left: 16px;
  }

  .panel {
    background-color: var(--color-bg-2);
    border-radius: 4px;
    overflow: auto;
    min-height: 83vh;
  }
  :deep(.panel-border) {
    margin-bottom: 2%;
    border-bottom: 1px solid rgb(var(--gray-2));
  }

  .moduler-wrap {
    border-radius: 4px;
    background-color: var(--color-bg-2);
  }

  :deep(.wrapper) {
    margin-bottom: 8px;
    text-align: center;
    cursor: pointer;

    &:last-child {
      .text {
        margin-bottom: 0;
      }
    }
    &:hover {
      .icon {
        color: rgb(var(--arcoblue-6));
        background-color: #e8f3ff;
      }
      .text {
        color: rgb(var(--arcoblue-6));
      }
    }
  }

  :deep(.icon) {
      display: inline-block;
      width: 32px;
      height: 32px;
      margin-bottom: 4px;
      color: rgb(var(--dark-gray-1));
      line-height: 32px;
      font-size: 16px;
      text-align: center;
      background-color: rgb(var(--gray-1));
      border-radius: 4px;
    }
</style>
