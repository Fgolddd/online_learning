<script setup>
import { Home, Bookshelf, Search, User, ShoppingCart } from '@icon-park/vue-next'
import { useRouter } from 'vue-router'
import Login from '@/components/Login.vue'
import { ref } from 'vue'
import { useStore } from 'vuex'
const store = useStore()
const router = useRouter()

const loginModalOpen = ref(false)

function openLoginModal() {
  loginModalOpen.value = true
}
function closeLoginModal() {
  loginModalOpen.value = false
}

const index = () => {
  router.push('/')
}
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
          <a class="navbar-item" v-if="store.getters['login/getIsAuthenticated']" @click="cart">
            <shopping-cart
              theme="multi-color"
              size="24"
              :fill="['#333', '#50e3c2', '#FFF', '#cf139e']"
            />

            <span>购物车</span>
          </a>
          <a class="navbar-item">
            <user
              v-if="store.getters['login/getIsAuthenticated']"
              theme="multi-color"
              size="24"
              :fill="['#333', '#50e3c2', '#FFF', '#cf139e']"
            />
            <span v-if="store.getters['login/getIsAuthenticated']">{{
              store.getters['login/getUserName']
            }}</span>
          </a>
          <a class="navbar-item" @click="openLoginModal">
            <button v-if="!store.getters['login/getIsAuthenticated']" class="button is-primary">
              登录
            </button>
          </a>
          <a class="navbar-item">
            <button
              v-if="!store.getters['login/getIsAuthenticated']"
              class="button is-primary is-light"
            >
              注册
            </button>
          </a>
        </div>
      </div>
    </nav>
    <Login :loginModalOpen="loginModalOpen" @closeLoginModal="closeLoginModal" />
  </header>
</template>

<style scoped>
</style>
