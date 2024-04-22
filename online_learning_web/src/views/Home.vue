<script setup>
import { Comment, ThumbsUp } from '@icon-park/vue-next'

import { ref, computed, onBeforeMount } from 'vue'
import { useStore } from 'vuex'

const isLogin = ref(Boolean(localStorage.getItem('token')))
const store = useStore()

const posts = computed(() =>
  store.getters['post/getPosts'].map((post) => ({ ...post, isActivate: false })),
)
const userInfo = store.getters['userInfo/getUserInfo']

onBeforeMount(() => {
  store.dispatch('post/fetchPosts')
  if (localStorage.getItem('token')) {
    store.dispatch('userInfo/fetchUserInfo', localStorage.getItem('userId'))
  }
})
</script>

<template>
  <section class="section section-spacing">
    <div class="column" v-if="isLogin || store.getters['login/getIsAuthenticated']">
      <div class="card">
        <header class="card-header">
          <p class="card-header-title">发个动态吧！</p>
        </header>
        <div class="card-content has-flex">
          <figure class="image is-48x48 mr-2">
            <img class="is-rounded" :src="userInfo.avatar" />
          </figure>
          <input
            class="input is-primary is-rounded"
            type="tel"
            placeholder="有什么新鲜事想告诉大家！"
            @click="inputClick"
          />
        </div>
      </div>
    </div>
    <div class="columns is-centered">
      <div class="column">
        <article v-for="post in posts" :key="post.id" class="column">
          <div class="card">
            <div class="level">
              <div class="level-left">
                <div class="level-item">
                  <figure class="image is-48x48">
                    <img class="is-rounded" :src="post.author.avatar" />
                  </figure>
                </div>
                <div class="level-item">
                  <p class="is-48x48">
                    <strong>{{ post.author.username }}</strong>
                  </p>
                </div>
              </div>

              <div class="level-right">
                <div class="level-item">
                  <time>发布于 {{ post.created_at }}</time>
                </div>
              </div>
            </div>

            <div class="card-content">
              <div class="content">
                {{ post.content }}
              </div>
            </div>

            <div class="columns is-multiline is-gapless">
              <div class="column is-half">
                <button
                  @click="handleCommentActive(post)"
                  class="dropdown button is-fullwidth"
                  onclick="this.classList.toggle('is-active')"
                  aria-haspopup="true"
                  aria-controls="dropdown-menu"
                >
                  <comment
                    theme="multi-color"
                    size="24"
                    :fill="['#333', '#50e3c2', '#FFF', '#cf139e']"
                  />

                  <div class="dropdown-menu" id="dropdown-menu" role="menu">
                    <div class="dropdown-content">
                      <a href="#" class="dropdown-item"> Dropdown item </a>
                      <a class="dropdown-item"> Other dropdown item </a>
                    </div>
                  </div>
                </button>
              </div>

              <div class="column is-half">
                <button @click="toggleDropdown" class="button is-fullwidth">
                  <thumbs-up
                    theme="multi-color"
                    size="24"
                    :fill="['#333', '#50e3c2', '#FFF', '#cf139e']"
                  />
                </button>
              </div>
            </div>
          </div>
        </article>
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
  margin-left: 20rem; /* 示例：左侧留出2rem（可根据需要调整） */
  margin-right: 20rem; /* 示例：右侧留出2rem（可根据需要调整） */
  margin-top: 2rem;
  margin-bottom: 2rem;
}
.has-flex {
  display: flex;
  align-items: center; /* 可选，垂直居中对齐 */
}
.mr-2 {
  margin-right: 0.5rem;
}
</style>

