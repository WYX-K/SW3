import { defineStore } from 'pinia'
import { RoleType, UserState } from './types'
import { setToken, clearSession } from '@/utils/auth'
import { removeRouteListener } from '@/utils/route-listener'
import { getLoginData } from '@/api/login'

const useUserStore = defineStore('user', {
  state: (): UserState => ({
    name: undefined,
    username: undefined,
    role: 'uicer',
    isLogin: false,
    major: '',
  }),

  getters: {
    userInfo(state: UserState): UserState {
      return { ...state }
    }
  },

  actions: {
    setIsLogin(islogin: boolean) {
      this.isLogin = islogin
    },

    setName(name: string) {
      this.name = name
    },

    setUsername(username: string) {
      this.username = username
    },

    setRole(role: RoleType) {
      this.role = role
    },

    setMajor(major: string) {
      this.major = major
    },
    
    async login(prama: FormData) {
      const res = await getLoginData(prama)
      if (res.status === 200) {
        this.role = res.data.role
        this.name = res.data.name
        this.username = res.data.username
        sessionStorage.setItem('ROLE', res.data.role)
        sessionStorage.setItem('USERNAME', res.data.username)
        sessionStorage.setItem('NAME', res.data.name)
        sessionStorage.setItem('MAJOR', res.data.major)
        setToken('USER')
        this.isLogin = true
      }
      return res
    },

    // Reset user's information
    resetInfo() {
      this.$reset()
    },

    logout() {
      this.isLogin = false
      this.resetInfo()
      clearSession()
      removeRouteListener()
    }
  },
})

export default useUserStore
