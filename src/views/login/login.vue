<template>
  <Button type="primary" @click="toHome">To Home</Button>
</template>

<script lang="ts">
import { defineComponent, onBeforeMount } from 'vue'
import { Button } from '@arco-design/web-vue'
import { useRouter } from 'vue-router'
// import { UserService } from '@/api/login'

export default defineComponent({
  name: 'Login',
  components: {
    Button
  },
  setup() {
    onBeforeMount(() => {
      login()
    })
    const login = async () => {
      const formData = new FormData()
      formData.append('username', 'simon')
      formData.append('pwd', 'simon')
      // const res = await UserService.login(formData)
      // console.log(res)
    }
    const router = useRouter()
    const toHome = (():void => {
      router.push({
        name: 'home'
      })
    })

    return {
      toHome
    }
  }
})
</script>

<style scoped>

</style>