<script setup>
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import { ShoppingCartAdd, Buy } from '@icon-park/vue-next'
import { useRouter } from 'vue-router'

import { toast } from 'bulma-toast'
import { onBeforeMount, reactive } from 'vue'
import api from '../api/index'

const router = useRouter()
const courseId = Number(useRouter().currentRoute.value.params.courseId)

const course = reactive({})
const chapters = reactive([])

function addPrefixToImages(content, mediaUrl) {
  return content.replace(/!\[\]\((.*)\)/g, '![](' + mediaUrl + '/$1)')
}

const baseURL = 'http://127.0.0.1:8000'

async function addCourseToCart() {
  try {
    const res = await api.cart.addItem(courseId)

    if (res.status === 201) {
      toast({
        message: '添加成功',
        type: 'is-success',
        position: 'top-center',
        duration: 2000,
      })
    }
  } catch (error) {
    console.error(error)
  }
}

async function toVideoRoom(section) {
  if (localStorage.getItem('token')) {
    router.push(`/video/${section.id}`)
  } else {
    toast({
      message: '请先登录',
      type: 'is-danger',
      position: 'top-center',
      duration: 2000,
    })
    setTimeout(() => {
      router.push('/login')
    }, 1000)
  }
}

onBeforeMount(async () => {
  const res = await api.course.getCourse(courseId)
  course.value = res.data
  chapters.value = res.data.chapters
})
</script>
<template>
  <Header></Header>
  <section class="section-spacing">
    <div class="columns">
      <div class="column is-half">
        <div class="card card-spacing">
          <div class="card-image">
            <figure class="image is-4by3">
              <img :src="course.value?.course_cover" alt="Placeholder image" />
            </figure>
          </div>
          <div class="card-content">
            <div class="media">
              <div class="media-left">
                <figure class="image is-48x48">
                  <img :src="course.value?.course_cover" alt="Placeholder image" />
                </figure>
              </div>
              <div class="media-content">
                <p class="title is-4">{{ course.value?.name }}</p>
              </div>
              <div class="media-right">
                <button
                  class="button is-primary is-outlined is-rounded"
                  style="margin-right: 1rem"
                  title="添加购物车"
                  @click="addCourseToCart"
                >
                  <shopping-cart-add
                    theme="multi-color"
                    size="24"
                    :fill="['#333', '#50e3c2', '#FFF', '#cf139e']"
                  />
                </button>
                <button class="button is-primary is-outlined is-rounded" title="购买">
                  <buy
                    theme="multi-color"
                    size="24"
                    :fill="['#333', '#50e3c2', '#FFF', '#cf139e']"
                  />
                </button>
              </div>
            </div>
            <div class="card-footer">
              <v-md-preview
                :text="addPrefixToImages(course.value?.description, baseURL)"
              ></v-md-preview>

              <br />
            </div>
          </div>
        </div>
      </div>
      <div class="column is-half">
        <div class="card card-spacing">
          <div class="card-content">
            <div class="columns is-multiline">
              <div
                class="column is-12"
                v-for="(chapter, chapterIndex) in chapters.value"
                :key="chapterIndex"
              >
                <div class="dropdown db-width">
                  <button
                    class="button db-width"
                    aria-haspopup="true"
                    aria-controls="dropdown-menu-{{ chapterIndex }}"
                    onclick="this.parentNode.classList.toggle('is-active')"
                  >
                    {{ chapter.title }}
                  </button>

                  <div
                    :id="'dropdown-menu-' + chapterIndex"
                    class="dropdown-menu dm-width"
                    role="menu"
                  >
                    <div class="dropdown-content">
                      <a v-for="(section, sectionIndex) in chapter.video" :key="sectionIndex">
                        <span @click="toVideoRoom(section)">
                          <a class="dropdown-item">{{ section.title }}</a>
                        </span>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <Footer></Footer>
</template>

<style scoped>
.card-spacing {
  margin-left: 5rem; /* 示例：左侧留出2rem（可根据需要调整） */
  margin-right: 5rem; /* 示例：右侧留出2rem（可根据需要调整） */
  margin-top: 2rem;
  margin-bottom: 2rem;
}
.db-width {
  width: 530px;
}
.dm-width {
  width: 530px;
}
/* .drop-button {
  width: 500px;
} */
</style>
