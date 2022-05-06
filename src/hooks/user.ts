import { Router } from 'vue-router'
import { Message } from '@arco-design/web-vue'
import consola from 'consola'
import { useUserStore } from '@/store'

export default function useUser() {
  const userStore = useUserStore()
  
  const logout = async (router: Router, t: any) => {
    userStore.logout()
    Message.success(t('login.form.logout.success'))
    router.push({
      name: 'login'
    })
  }

  const login = async (data: FormData, router: Router, t: any) => {
    try {
      const res = await userStore.login(data)
      if (res.status === 200) {
        consola.success(res)
        router.push({
          name: 'intro',
        })
        Message.success(t('login.form.login.success'))
      } else if (res.status === 201) {
        Message.success(t('login.form.login.checkEmail'))
      } else {
        Message.success(t('login.form.login.fail'))
      }
    } catch (err) {
      consola.error(err)
    }
  }

  return {
    login,
    logout
  }
}
