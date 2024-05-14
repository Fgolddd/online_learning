<script setup>
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../api/index'
import { toast } from 'bulma-toast'
const router = useRouter()

const username = ref('')
const phone = ref('')
const password = ref('')

async function handleSubmit() {
  const form = { username: username.value, phone: phone.value, password: password.value }
  const res = await api.user.register(form)
  if (res.status === 201) {
    toast({
      message: '注册成功',
      type: 'is-primary',
      position: 'top-center',
      duration: 2000,
    })
    setTimeout(() => {
      router.push('/login')
    }, 1000) // 延迟 1 秒后执行路由跳转
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
          <p class="title is-3 p-text">注册</p>
        </div>
      </div>
      <div class="card-content">
        <form @submit.prevent="handleSubmit">
          <div class="field">
            <p class="title is-5 p-text">用户名</p>
            <div class="control">
              <input
                v-model="username"
                class="input is-info is-medium is-rounded"
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
                class="input is-info is-medium is-rounded"
                type="password"
                style="text-align: center"
                placeholder="请输入密码"
                required
              />
            </div>
          </div>
          <div class="field">
            <p class="title is-5 p-text">手机号</p>
            <div class="control">
              <input
                v-model="phone"
                class="input is-info is-medium is-rounded"
                type="text"
                style="text-align: center"
                placeholder="请输入手机号"
                required
              />
            </div>
          </div>
          <div class="control" style="text-align: center">
            <button type="submit" class="button is-info is-rounded">注册</button>
          </div>
        </form>
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

