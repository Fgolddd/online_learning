<script setup>
import { onBeforeMount, ref } from 'vue'
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import { useStore } from 'vuex'

const store = useStore()

const order = ref({})

onBeforeMount(() => {
  store.dispatch('order/createOrder')
  order.value = store.getters['order/getOrder']
})
</script>
<template>
  <Header></Header>
  <section class="section-spacing">
    <div class="card"></div>
  </section>
  <Footer></Footer>
</template>
<style scoped>
.section-spacing {
  margin-left: 20rem; /* 示例：左侧留出2rem（可根据需要调整） */
  margin-right: 20rem; /* 示例：右侧留出2rem（可根据需要调整） */
  margin-top: 2rem;
  margin-bottom: 2rem;
}
</style>