import { defineStore } from 'pinia'
import { UserState } from './types'
import { removeRouteListener } from '@/utils/route-listener'

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
    switchRoles() {
      return new Promise((resolve) => {
        this.role = this.role === 'user' ? 'admin' : 'user'
        resolve(this.role)
      })
    },

    getLoginStatus() {
      return this.isLogin
    },

    login() {
      this.isLogin = true
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
      removeRouteListener()
    }
  },
})

export default useUserStore
