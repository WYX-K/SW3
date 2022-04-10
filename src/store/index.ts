import { defineStore } from 'pinia'

const useIsLoginStore = defineStore({
  id: 'login',
  state: () => ({
    islogin: false
  }),
  getters: {},
  actions: {}
})

export default useIsLoginStore