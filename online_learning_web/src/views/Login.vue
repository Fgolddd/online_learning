<script setup>
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
const router = useRouter()

const username = ref('')
const password = ref('')
const store = useStore()

async function handleSubmit() {
  try {
    const form = { username: username.value, password: password.value }
    await store.dispatch('user/login', form)
    setTimeout(() => {
      router.push('/')
    }, 1000) // 延迟 1 秒后执行路由跳转
  } catch (error) {
    console.error(error)
    // 处理登录失败...
  }
}
</script>
<template>
  <Header></Header>
  <section class="section-spacing">
    <div class="card">
      <div class="card-image">
        <figure class="image is-3by1">
          <img src="../assets/photo/logo.png" alt="Placeholder image" />
        </figure>
      </div>
      <div class="media">
        <div class="media-content">
          <p class="title is-3 p-text">登录</p>
        </div>
      </div>
      <div class="card-content">
        <form @submit.prevent="handleSubmit">
          <div class="field">
            <p class="title is-5 p-text">用户名</p>
            <div class="control">
              <input
                v-model="username"
                class="input is-primary is-medium is-rounded"
                type="text"
                style="text-align: center"
                placeholder="请输入用户名"
                required
              />
            </div>
          </div>
          <div class="field">
            <p class="title is-5 p-text">密码</p>
            <div class="control">
              <input
                v-model="password"
                class="input is-primary is-medium is-rounded"
                type="password"
                style="text-align: center"
                placeholder="请输入密码"
                required
              />
            </div>
          </div>

          <div class="control" style="text-align: center">
            <button type="submit" class="button is-primary is-rounded">登录</button>
          </div>
        </form>
      </div>
      <div class="card-content is-flex cc-center">
        <p>没有账号？</p>
        <a>注册</a>
      </div>
    </div>
  </section>
  <Footer></Footer>
</template>
<style scoped>
.section-spacing {
  margin-left: 30rem;
  margin-right: 30rem;
  margin-top: 1rem;
  margin-bottom: 1rem;
}
.cc-center {
  justify-content: center;
}
.p-text {
  text-align: center;
}
</style>

