<script setup>
</script>
<template>
  <section class="section is-medium">
    <div class="columns is-centered is-large">
      <div class="column is-one-third">
        <form class="box" @submit.prevent="submitForm">
          <div class="field">
            <label class="label">用户名</label>
            <div class="control">
              <input
                class="input"
                type="text"
                v-model="username"
                placeholder="请输入用户名"
                required
              />
            </div>
          </div>
          <div class="field">
            <label class="label">密码</label>
            <div class="control">
              <input
                class="input"
                type="password"
                v-model="password"
                placeholder="请输入密码"
                required
              />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-primary is-fullwidth" type="submit">登录</button>
            </div>
          </div>
          <hr />
          <div class="is-flex is-justify-content-center">
            <p class="mr-2">没有账号？</p>
            <div>
              <router-link to="/register">
                <a>注册</a>
              </router-link>
            </div>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>

<style scoped>
</style>