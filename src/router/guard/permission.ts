import type { Router } from 'vue-router'
import NProgress from 'nprogress' // progress bar

import usePermission from '@/hooks/permission'
import { useUserStore } from '@/store'
import appRoutes from '../routes'

export default function setupPermissionGuard(router: Router) {
  router.beforeEach(async (to, _from, next) => {
    NProgress.start()
    const userStore = useUserStore()
    async function crossroads() {
      const Permission = usePermission()
      if (Permission.accessRouter(to)) next()
      else {
        const destination = Permission.findFirstPermissionRoute(
          appRoutes,
          userStore.role
        ) || {
          name: 'notFound',
        }
        next(destination)
      }
      NProgress.done()
    }
    if (userStore.getLoginStatus()) {
      if (userStore.role) {
        crossroads()
      } else {
        try {
          crossroads()
        } catch (error) {
          next({
            name: 'login'
          })
          NProgress.done()
        }
      }
    } else {
      if (to.name === 'login') {
        next()
        NProgress.done()
        return
      }
      next({
        name: 'login'
      })
      NProgress.done()
    }
  })
}
