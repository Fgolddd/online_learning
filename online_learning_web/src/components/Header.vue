<script setup>
import { Home, Bookshelf, Search, User, ShoppingCart } from '@icon-park/vue-next'
import { useRouter } from 'vue-router'
import Login from '@/components/Login.vue'
import { ref, watchEffect } from 'vue'
import { useStore } from 'vuex'
import Register from './Register.vue'
const store = useStore()
const router = useRouter()
const isLogin = ref(false)

const handleLogout = async () => {
  await store.dispatch('login/logout')
}
watchEffect(() => {
  ;(isLogin.value =
    Boolean(localStorage.getItem('token')) || store.getters['login/getIsAuthenticated']),
    (newValue) => {
      isLogin.value = Boolean(newValue)
      console.log(isLogin.value)
    },
    { immediate: true, deep: true }
})
const loginModalOpen = ref(false)
const registerModalOpen = ref(false)
function openLoginModal() {
  loginModalOpen.value = true
}
function closeLoginModal() {
  loginModalOpen.value = false
}
function openRegisterModal() {
  registerModalOpen.value = true
}
function closeRegisterModal() {
  registerModalOpen.value = false
}
const userName = localStorage.getItem('userName')
const index = () => {
  router.push('/')
}
const course = () => {
  router.push('/course')
}
const userId = localStorage.getItem('userId')
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
          <a class="navbar-item" @click="index">
            <home theme="multi-color" size="24" :fill="['#333', '#50e3c2', '#FFF', '#cf139e']" />
            <span>首页</span>
          </a>

          <a class="navbar-item" @click="course">
            <bookshelf
              theme="multi-color"
              size="24"
              :fill="['#333', '#50e3c2', '#FFF', '#cf139e']"
            />

            <span>课程</span>
          </a>

          <div class="navbar-item">
            <p class="control has-icons-left">
              <input class="input" type="text" placeholder="Find a course" />
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
          <router-link :to="{ name: 'Cart', params: { userId: userId } }">
            <a class="navbar-item" v-if="isLogin">
              <shopping-cart
                theme="multi-color"
                size="24"
                :fill="['#333', '#50e3c2', '#FFF', '#cf139e']"
              />

              <span>购物车</span>
            </a>
          </router-link>

          <a class="navbar-item" v-if="isLogin">
            <div class="dropdown is-hoverable is-right">
              <div class="dropdown-trigger">
                <user
                  theme="multi-color"
                  size="24"
                  :fill="['#333', '#50e3c2', '#FFF', '#cf139e']"
                />
                <span>{{ userName }}</span>
              </div>
              <div class="dropdown-menu" id="dropdown-menu" role="menu">
                <div class="dropdown-content">
                  <a href="#" class="dropdown-item">个人中心</a>
                  <a href="#" class="dropdown-item">我的课程</a>
                  <hr class="dropdown-divider" />
                  <a class="dropdown-item" @click="handleLogout">退出登录</a>
                </div>
              </div>
            </div>
          </a>
          <a class="navbar-item" @click="openLoginModal">
            <button v-if="!isLogin" class="button is-primary">登录</button>
          </a>
          <a class="navbar-item" @click="openRegisterModal">
            <button v-if="!isLogin" class="button is-primary is-light">注册</button>
          </a>
        </div>
      </div>
    </nav>
    <Login :loginModalOpen="loginModalOpen" @closeLoginModal="closeLoginModal" />
    <Register :registerModalOpen="registerModalOpen" @closeRegisterModal="closeRegisterModal" />
  </header>
</template>

<style scoped>
</style>
