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
    }
  ],
}