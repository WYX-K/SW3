<template>
  <div class="container">
    <div class="left-side">
      <div class="panel">
        <keep-alive> 
          <component :is="curComponent" @onClick="onGradeClick"></component>
        </keep-alive>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { shallowRef } from 'vue'
import Content1 from './components/content.vue'
import Content2 from './components/gradeInfo.vue'

const curComponent = shallowRef(Content1)

const onGradeClick = (isClick: boolean) => {
  if (isClick) {
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    curComponent.value = Content2 
    sessionStorage.setItem('CC', 'C2')
  }
}
if (sessionStorage.getItem('CC') === 'C2') {
  // eslint-disable-next-line @typescript-eslint/ban-ts-comment
  // @ts-ignore
  curComponent.value = Content2 
} else {
  sessionStorage.setItem('CC', 'C1')
}
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