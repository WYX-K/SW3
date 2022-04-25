export default {
  path: 'poster',
  name: 'poster',
  component: () => import('@/views/poster/index.vue'),
  meta: {
    locale: 'menu.poster',
    requiresAuth: true,
    icon: 'icon-camera',
    order: 0,
  },
  children: [
    {
      path: 'show&vote',
      name: 'show&vote',
      component: () => import('@/views/poster/show&vote/index.vue'),
      meta: {
        locale: 'menu.poster.show',
        requiresAuth: true,
        roles: ['uicer'],
      },
    },
    {
      path: 'upload',
      name: 'upload',
      component: () => import('@/views/poster/upload/index.vue'),
      meta: {
        locale: 'menu.poster.upload',
        requiresAuth: true,
        roles: ['admin','con_coor'],
      },
    },
    {
      path: 'edit',
      name: 'edit',
      component: () => import('@/views/poster/edit/index.vue'),
      meta: {
        locale: 'menu.poster.edit',
        requiresAuth: true,
        roles: ['admin','con_coor'],
      },
    }
  ],
}