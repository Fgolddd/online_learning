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
            <label class="label">手机号码</label>
            <div class="control">
              <input
                class="input"
                type="phone"
                v-model="phone"
                placeholder="请输入手机号码"
                required
              />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-primary is-fullwidth" type="submit">注册</button>
            </div>
          </div>
          <hr />
        </form>
      </div>
    </div>
  </section>
</template>

<style scoped>
</style>