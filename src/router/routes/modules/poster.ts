export default {
  path: 'poster',
  name: 'poster',
  component: () => import('@/views/poster/index.vue'),
  meta: {
    locale: 'menu.poster',
    requiresAuth: true,
    icon: 'icon-home',
    order: 0,
  },
  children: [
    {
      path: 'show',
      name: 'show',
      component: () => import('@/views/poster/show/index.vue'),
      meta: {
        locale: 'menu.poster.show',
        requiresAuth: true,
        roles: ['user'],
      },
    },
  ],
}