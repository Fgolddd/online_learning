<script setup>
import { Home, Bookshelf, Search } from '@icon-park/vue-next'
import { useRouter } from 'vue-router'

const router = useRouter()
const login = () => {
  router.push('/login')
}

const index = () => {
  router.push('/')
}
const course = () => {
  router.push('/course')
}
</script>

<template>
  <header>
    <nav class="navbar is-spaced" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item" href="https://bulma.io">
          <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28" />
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
          <div class="navbar-item" @click="login">
            <a> 登录/注册</a>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<style scoped>
</style>
