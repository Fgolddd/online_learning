import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('../views/Home.vue')
    },
    {
      path: '/course',
      name: 'Course',
      component: () => import('../views/Course.vue')
    },
    {
      path: '/course/:courseId',
      name: 'CourseDetail',
      component: () => import('../views/CourseDetail.vue')
    },
    {
      path: '/video',
      name: 'VideoRoom',
      component: () => import('../views/VideoRoom.vue')
    },
    {
      path: '/Cart/:userId',
      name: 'Cart',
      component: () => import('../views/Cart.vue')
    }
  ]
})

export default router
