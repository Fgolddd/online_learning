<script setup>
import { onBeforeMount } from 'vue'
import { useStore } from 'vuex'
const store = useStore()

onBeforeMount(() => {
  if (localStorage.getItem('token')) {
    store.dispatch('user/fetchUserInfo', localStorage.getItem('userId'))
  }
})
</script>

<template>
  <router-view />
</template>

<style scoped>
</style>
