<script setup>
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import { useStore } from 'vuex'

import { onMounted, ref } from 'vue'

const store = useStore()
const courseList = ref(null)
courseList.value = store.getters['userInfo/getMyCourse']
console.log(courseList.value)

onMounted(async () => {
  await store.dispatch('userInfo/fetchMyCourse')
})
</script>
<template>
  <Header></Header>
  <section class="section-spacing">
    <div class="columns is-multiline">
      <div class="column is-one-third" v-for="(item, index) in courseList" :key="index"></div>
    </div>
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