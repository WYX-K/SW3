import { defineStore } from 'pinia'
import { UserState } from './types'
import { setToken, clearToken } from '@/utils/auth'
import { removeRouteListener } from '@/utils/route-listener'
import { getLoginData } from '@/api/login'

const useUserStore = defineStore('user', {
  state: (): UserState => ({
    name: undefined,
    role: '',
    isLogin: false
  }),

  getters: {
    userInfo(state: UserState): UserState {
      return { ...state }
    }
  },

  actions: {

    getRole() {
      return this.role
    },

    getLoginStatus() {
      return this.isLogin
    },

    async login(data: FormData) {
      const res = await getLoginData(data)
      setToken('USER')
      this.isLogin = true
      return res
    },
    
    // Set user's information
    setInfo(partial: Partial<UserState>) {
      this.$patch(partial)
    },

    // Reset user's information
    resetInfo() {
      this.$reset()
    },

    logout() {
      this.isLogin = false
      this.resetInfo()
      clearToken()
      removeRouteListener()
    }
  },
})

export default useUserStore
