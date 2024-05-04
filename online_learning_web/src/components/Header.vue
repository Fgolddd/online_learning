<script setup>
import { Home, Bookshelf, Search, User, ShoppingCart, Notes } from '@icon-park/vue-next'
import { useRouter } from 'vue-router'

import { ref, onMounted } from 'vue'
import { useStore } from 'vuex'

const store = useStore()
const router = useRouter()
const isLogin = ref(false)

const userName = localStorage.getItem('userName')
const userId = Number(localStorage.getItem('userId'))

function toUserInfo(userId) {
  router.push(`/user/info/${userId}`)
}
function toUserCart() {
  router.push('/cart')
}

const handleLogout = async () => {
  await store.dispatch('login/logout')
  setTimeout(() => {
    router.push('/login')
  }, 1000) // 延迟 1 秒后执行路由跳转
}

const toIndex = () => {
  router.push('/')
}
function toPost() {
  router.push('/post/edit')
}
const toCourse = () => {
  router.push('/course')
}
const toLogin = () => {
  router.push('/login')
}
const toRegister = () => {
  router.push('/register')
}
onMounted(() => {
  if (localStorage.getItem('userName') || store.getters['login/getIsAuthenticated']) {
    isLogin.value = true
  } else {
    isLogin.value = false
  }
})
</script>

<template>
  <header>
    <nav class="navbar is-spaced" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item" href="/">
          <img src="../assets/photo/logo.png" width="112" height="72" />
        </a>

        <a
          role="button"
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbarBasicExample"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
          <a class="navbar-item" @click="toIndex">
            <home theme="multi-color" size="24" :fill="['#333', '#50e3c2', '#FFF', '#cf139e']" />
            <span>首页</span>
          </a>

          <a class="navbar-item" @click="toCourse">
            <bookshelf
              theme="multi-color"
              size="24"
              :fill="['#333', '#50e3c2', '#FFF', '#cf139e']"
            />

            <span>课程</span>
          </a>

          <div class="navbar-item">
            <p class="control has-icons-left">
              <input class="input" type="text" placeholder="搜索课程" />
              <a class="icon is-left">
                <search
                  theme="multi-color"
                  size="24"
                  :fill="['#333', '#50e3c2', '#FFF', '#cf139e']"
                />
              </a>
            </p>
          </div>
        </div>

        <div class="navbar-end">
          <a class="navbar-item" v-if="isLogin" @click="toPost">
            <notes theme="two-tone" size="24" :fill="['#333', '#50e3c2']" />
            <span>发帖</span>
          </a>
          <a class="navbar-item" v-if="isLogin" @click="toUserCart">
            <shopping-cart theme="multi-color" size="24" :fill="['#333', '#50e3c2']" />

            <span>购物车</span>
          </a>

          <a class="navbar-item" v-if="isLogin">
            <div class="dropdown is-hoverable is-right">
              <div class="dropdown-trigger">
                <user theme="multi-color" size="24" :fill="['#333', '#50e3c2']" />
                <span>{{ userName }}</span>
              </div>
              <div class="dropdown-menu" id="dropdown-menu" role="menu">
                <div class="dropdown-content">
                  <a class="dropdown-item" @click="toUserInfo(userId)">个人中心</a>
                  <a class="dropdown-item" @click="handleUserCourse">我的课程</a>
                  <hr class="dropdown-divider" />
                  <a class="dropdown-item" @click="handleLogout">退出登录</a>
                </div>
              </div>
            </div>
          </a>
          <a class="navbar-item" @click="toLogin">
            <button v-if="!isLogin" class="button is-primary">登录</button>
          </a>
          <a class="navbar-item" @click="toRegister">
            <button v-if="!isLogin" class="button is-primary is-light">注册</button>
          </a>
        </div>
      </div>
    </nav>
  </header>
</template>

<style scoped>
</style>
