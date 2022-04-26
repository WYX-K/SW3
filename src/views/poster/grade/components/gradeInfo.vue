<template>
  <div>
  </div>
</template>

<script setup lang="ts">
import mitt from 'mitt'

const emitter = mitt()   
emitter.on('getRecord', (record) => {
  console.log(record)
})
</script>

<style lang="scss" scoped>

</style>