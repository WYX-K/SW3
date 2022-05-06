/* eslint-disable arrow-body-style */
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'
import { createStyleImportPlugin } from 'vite-plugin-style-import'
import vueJsx from '@vitejs/plugin-vue-jsx'
import { viteMockServe } from 'vite-plugin-mock'

export default defineConfig({
  plugins: [
    vue(),
    vueJsx(),
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
    }),
    viteMockServe({ supportTs: false })
  ],
  server: {
    // 反向代理
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000/', // 代理的地址
        changeOrigin: true,
      },
      '/api/mock': {
        target: 'http://localhost:8080/', // 对mock进行代理，为了区别非mock的代理
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  },
  css: {
    preprocessorOptions: {
      less: {
        modifyVars: {
          hack: `true; @import (reference) "${ resolve(
            'src/assets/style/breakpoint.less'
          ) }";`,
        },
        javascriptEnabled: true,
      },
    },
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, '.', 'src'),
      vue: 'vue/dist/vue.esm-bundler.js'
    },
  }
})