<script setup>
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import api from '@/api'
import { ref } from 'vue'
import { toast } from 'bulma-toast'
import { useRouter } from 'vue-router'
const router = useRouter()
const mdContent = ref('')
const publishContent = async () => {
  try {
    const res = await api.post.createPost({
      content: mdContent.value,
    })
    if (res.status === 201) {
      toast({
        message: '发布成功',
        type: 'is-primary',
        position: 'top-center',
        duration: 2000,
      })
      setTimeout(() => {
        router.push('/')
      }, 1000)
    } else {
      toast({
        message: '发布失败',
        type: 'is-danger',
        position: 'top-center',
        duration: 2000,
      })
      setTimeout(() => {
        router.push('/')
      }, 1000)
    }
  } catch (error) {
    console.error('Error submitting Markdown:', error)
  }
}
</script>
<template>
  <Header></Header>
  <section class="section-spacing">
    <div class="card">
      <div class="card-header">
        <p class="card-header-title">发个动态吧！</p>
      </div>
      <div class="card-content">
        <v-md-editor v-model="mdContent" height="400px"></v-md-editor>
      </div>
      <div class="card-content">
        <div class="level">
          <div class="level-left"></div>

          <div class="level-right">
            <div class="level-item">
              <button class="button is-primary" @click="publishContent">发布</button>
            </div>
          </div>
        </div>
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