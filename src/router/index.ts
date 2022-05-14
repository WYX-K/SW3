import { createRouter, createWebHistory } from 'vue-router'
import NProgress from 'nprogress'
import appRoutes from './routes'
import 'nprogress/nprogress.css'
import createRouteGuard from './guard'
import DefaultLayout from '@/layout/default-layout.vue'

NProgress.configure({ showSpinner: false })

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/login/index.vue'),
      meta: {
        requiresAuth: false,
      },
    },
    {
      name: 'root',
      path: '/',
      component: DefaultLayout,
      children: appRoutes,
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'notFound',
      component: () => import('@/views/not-found/index.vue'),
    },
  ],
  scrollBehavior() {
    return { top: 0 }
  },
})

createRouteGuard(router)
export default router