<!-- RegisterModal.vue -->
<script setup>
import { ref, defineProps, defineEmits } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
const router = useRouter()
const store = useStore()
const username = ref('')
const phone = ref('')
const password = ref('')

const props = defineProps({
  registerModalOpen: {
    type: Boolean,
    default: false,
    required: true,
  },
})
const emit = defineEmits(['closeRegisterModal'])

function handleRegisterClose() {
  emit('closeRegisterModal')
}

async function handleSubmit() {
  const form = { username: username.value, phone: phone.value, password: password.value }

  await store.commit('login/register', form)
  router.push('/')
}
</script>
<template>
  <div>
    <div v-if="props.registerModalOpen" class="modal is-active">
      <div class="modal-background" @click="handleRegisterClose"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">注册</p>
          <button class="delete" aria-label="close" @click="handleRegisterClose"></button>
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
              <label class="label">手机号</label>
              <div class="control">
                <input
                  v-model="phone"
                  class="input"
                  type="text"
                  placeholder="请输入手机号"
                  required
                />
              </div>
            </div>

            <div class="field">
              <div class="control">
                <button type="submit" class="button is-primary is-fullwidth">注册</button>
              </div>
            </div>
          </form>
        </section>
      </div>
    </div>
  </div>
</template>

