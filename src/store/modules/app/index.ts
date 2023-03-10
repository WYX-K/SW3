/* eslint-disable @typescript-eslint/ban-ts-comment */
import { defineStore } from 'pinia'
import defaultSettings from '@/config/settings.json'
import { AppState } from './types'

const useAppStore = defineStore('app', {
  state: (): AppState => ({ ...defaultSettings }),

  actions: {
    // Update app settings
    updateSettings(partial: Partial<AppState>) {
      // @ts-ignore-next-line
      this.$patch(partial)
    },
    
    // Change theme color
    toggleTheme(dark: boolean) {
      if (dark) {
        this.theme = 'dark'
        document.body.setAttribute('arco-theme', 'dark')
      } else {
        this.theme = 'light'
        document.body.removeAttribute('arco-theme')
      }
    },

    toggleMenu(value: boolean) {
      this.hideMenu = value
    },
  },
})

export default useAppStore
