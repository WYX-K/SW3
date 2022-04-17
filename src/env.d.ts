/* eslint-disable @typescript-eslint/ban-types */
/// <reference types="vite/client" />

declare module '*.vue' {
  import type { DefineComponent } from 'vue'

  const component: DefineComponent<{}, {}, any>
  export default component
}
interface ImportMetaEnv {
  readonly VITE_API_BASE_URL: string;
}

declare module 'mockjs'
declare module 'vue-i18n/index'
declare module 'nprogress'
declare module 'consola/src/browser'
