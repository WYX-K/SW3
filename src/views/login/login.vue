<template>
  <Button type="primary">Hello World</Button>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { Button } from '@arco-design/web-vue'

export default defineComponent({
  name: 'Login',
  components: {
    Button
  },
  setup() {
    return {}
  }
})
</script>

<style scoped>

</style>