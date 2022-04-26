export default {
  path: 'luckydraw',
  name: 'luckydraw',
  component: () => import('@/views/luckydraw/index.vue'),
  meta: {
    locale: 'menu.luckydraw',
    requiresAuth: true,
    icon: 'icon-thumb-up',
    order: 0,
  },
  children: [
    {
      path: 'choose',
      name: 'choose',
      component: () => import('@/views/luckydraw/choose/index.vue'),
      meta: {
        locale: 'menu.luckydraw.choose',
        requiresAuth: true,
        roles: ['dean']
      },
    },
  ],
}