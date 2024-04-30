<script setup>
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import Video from '@/components/Video.vue'

import { useStore } from 'vuex'
const store = useStore()

const video = store.getters['userInfo/getVideoInfoById']
</script>
<template>
  <Header></Header>
  <section class="section-spacing">
    <div class="card">
      <div class="card-content">
        <p class="title is-4">{{ video.title }}</p>
      </div>
      <div class="card-image">
        <Video :source="video.link"></Video>
      </div>
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