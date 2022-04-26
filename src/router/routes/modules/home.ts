export default {
  path: 'home',
  name: 'home',
  component: () => import('@/views/home/index.vue'),
  meta: {
    locale: 'menu.home',
    requiresAuth: true,
    icon: 'icon-home',
    order: 0,
  },
  children: [
    {
      path: 'intro',
      name: 'intro',
      component: () => import('@/views/home/intro/index.vue'),
      meta: {
        locale: 'menu.home.intro',
        requiresAuth: true,
        roles: ['*']
      },
    },
  ],
}