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
      path: '/login',
      name: 'Login',
      component: () => import('../views/Login.vue')
    },
    {
      path: '/register',
      name: 'Register',
      component: () => import('../views/Register.vue')
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
      path: '/video/:videoId',
      name: 'VideoRoom',
      component: () => import('../views/VideoRoom.vue')
    },
    {
      path: '/cart/:userId',
      name: 'Cart',
      component: () => import('../views/Cart.vue')
    },
    {
      path: '/user/info/:userId',
      name: 'UserInfo',
      component: () => import('../views/UserInfo.vue')
    },
    {
      path: '/post/:postId',
      name: 'PostDetail',
      component: () => import('../views/PostDetail.vue')
    },
  ]
})

export default router
