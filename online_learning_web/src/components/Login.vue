<script setup>
import { ref, defineProps, defineEmits } from 'vue'
import Register from '@/components/Register.vue'
import { useStore } from 'vuex'

const username = ref('')
const password = ref('')
const store = useStore()
const registerModalOpen = ref(false)
const props = defineProps({
  loginModalOpen: {
    type: Boolean,
    default: false,
    required: true,
  },
})

const emit = defineEmits(['closeLoginModal'])

function openRegisterModal() {
  registerModalOpen.value = true
}
function closeRegisterModal() {
  registerModalOpen.value = false
}
function handleLoginClose() {
  emit('closeLoginModal')
}

async function handleSubmit() {
  try {
    // 在这里实现登录逻辑，如发送登录请求到后端
    // 示例：假设 `login` 是一个异步登录函数
    const credentials = { username: username.value, password: password.value }
    await store.dispatch('login/login', credentials)
    console.log(store.getters['login/getUserName'])
    handleLoginClose()
    // 登录成功后的操作...
  } catch (error) {
    store.commit('login/setLoginError', error)
    console.error(error)
    // 处理登录失败...
  }
}
</script>
<template>
  <div v-if="props.loginModalOpen" class="modal is-active">
    <div class="modal-background" @click="handleLoginClose"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">登录/注册</p>
        <button class="delete" aria-label="close" @click="handleLoginClose"></button>
      </header>

      <section class="modal-card-body">
        <form @submit.prevent="handleSubmit">
          <div class="field">
            <label class="label">用户名</label>
            <div class="control">
              <input
                v-model="username"
                class="input"
                type="text"
                placeholder="请输入用户名"
                required
              />
            </div>
          </div>
          <div class="field">
            <label class="label">密码</label>
            <div class="control">
              <input
                v-model="password"
                class="input"
                type="password"
                placeholder="请输入密码"
                required
              />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button type="submit" class="button is-primary is-fullwidth">登录</button>
            </div>
          </div>
          <hr />
          <div class="is-flex is-justify-content-center">
            <p>没有账号?</p>
            <div>
              <a @click="openRegisterModal"> 注册 </a>
              <Register
                :registerModalOpen="registerModalOpen"
                @closeRegisterModal="closeRegisterModal"
              ></Register>
            </div>
          </div>
        </form>
      </section>
    </div>
  </div>
</template>

