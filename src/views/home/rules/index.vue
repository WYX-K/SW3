<template>
  <div class="container">
    <div class="left-side">
      <div class="panel">
        <Content></Content>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import Content from './components/content.vue'
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
</style>