<script setup>
import { ShoppingCartAdd, Buy } from '@icon-park/vue-next'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
const store = useStore()
const courseId = Number(useRouter().currentRoute.value.params.courseId)

const course = store.getters['course/getCourseById'](courseId)

const chapters = course.chapters
</script>
<template>
  <section class="section-spacing">
    <div class="columns">
      <div class="column is-half">
        <div class="card card-spacing">
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
              <div class="media-right">
                <button
                  class="button is-primary is-outlined is-rounded"
                  style="margin-right: 1rem"
                  title="添加购物车"
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
              <div v-html="course.description"></div>
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
                v-for="(chapter, chapterIndex) in chapters"
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
                      <a
                        v-for="(section, sectionIndex) in chapter.info"
                        :key="sectionIndex"
                        class="dropdown-item"
                      >
                        <router-link :to="{ name: 'VideoRoom', params: { url: section.url } }">
                          {{ section.remark }}
                        </router-link>
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
