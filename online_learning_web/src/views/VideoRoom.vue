<script setup>
import { ref } from 'vue'
import Video from '@/components/Video.vue'
const url = ref('http://vjs.zencdn.net/v/oceans.mp4')
</script>
<template>
  <section class="section-spacing">
    <div class="card">
      <div class="card-content">
        <p class="title is-4">Video Room</p>
      </div>
      <div class="card-image">
        <Video :source="url"></Video>
      </div>
    </div>
  </section>
</template>
<style scoped>
.section-spacing {
  margin-left: 20rem; /* 示例：左侧留出2rem（可根据需要调整） */
  margin-right: 20rem; /* 示例：右侧留出2rem（可根据需要调整） */
  margin-top: 2rem;
  margin-bottom: 2rem;
}
</style>