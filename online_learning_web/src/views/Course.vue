<script setup>
import { computed, onBeforeMount } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

const store = useStore()
const router = useRouter()
const courses = computed(() => store.getters['course/getCourses'])
onBeforeMount(async () => {
  await store.dispatch('course/fetchCourses')
})

function handleCardClick(course) {
  router.push({
    name: 'CourseDetail',
    params: {
      courseId: course.id,
    },
  })
}
</script>
<template>
  <section>
    <p class="title is-3 has-text-centered">OLEARN 在线课程</p>
  </section>
  <section class="section-spacing">
    <div class="columns is-multiline">
      <div class="column is-one-quarter" v-for="course in courses" :key="course.id">
        <div class="card" @click="handleCardClick(course)">
          <div class="card-image">
            <figure class="image is-4by3">
              <img :src="course.course_cover" alt="Placeholder image" />
            </figure>
          </div>
          <div class="card-content">
            <div class="media">
              <div class="media-left">
                <figure class="image is-48x48">
                  <img :src="course.course_cover" alt="Placeholder image" />
                </figure>
              </div>
              <div class="media-content">
                <p class="title is-4">{{ course.name }}</p>
              </div>
            </div>
          </div>
          <div class="card-footer">
            <div class="card-footer-item">
              <p>{{ course.students }}人已学习</p>
            </div>
            <div class="card-footer-item">
              <p>￥{{ course.price }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<style scoped>
.card:hover {
  cursor: pointer;
  transform: scale(1.03); /* 示例：放大2% */
  transition: transform 0.2s ease-in-out; /* 添加平滑过渡效果 */
}
.section-spacing {
  margin-left: 5rem; /* 示例：左侧留出2rem（可根据需要调整） */
  margin-right: 5rem; /* 示例：右侧留出2rem（可根据需要调整） */
  margin-top: 2rem;
  margin-bottom: 2rem;
}
</style>