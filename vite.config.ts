/* eslint-disable arrow-body-style */
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'
import { createStyleImportPlugin } from 'vite-plugin-style-import'

export default defineConfig({
  plugins: [
    vue(),
    createStyleImportPlugin({
      libs: [
        {
          libraryName: '@arco-design/web-vue',
          esModule: true,
          resolveStyle: (name) => {
            // css
            return `@arco-design/web-vue/es/${ name }/style/css.js`
          }
        }
      ]
    })
  ],
  server: {
    // 反向代理
    proxy: {
      '/api': {
        target: 'https://cms-1591686-1309449446.ap-shanghai.run.tcloudbase.com', // 代理的地址
        changeOrigin: true,
        rewrite: path => path.replace(/^\/api/, '')
      }
    }
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, '.', 'src'),
    },
  }
})