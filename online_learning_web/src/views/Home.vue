<script setup>
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import { toast } from 'bulma-toast'
import { ref, computed, onBeforeMount } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

const isLogin = ref(false)
const store = useStore()
const router = useRouter()
const posts = computed(() =>
  store.getters['post/getPosts'].map((post) => ({ ...post, isActivate: false })),
)
// const userInfo = store.getters['userInfo/getUserInfo']
const userAvatar = 'http://127.0.0.1:8000/' + localStorage.getItem('userAvatar')

function inputClick() {
  router.push('/post/edit')
}

function toPostDetail(postId) {
  if (localStorage.getItem('token')) {
    router.push(`/post/${postId}`)
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

onBeforeMount(() => {
  store.dispatch('userInfo/fetchUserInfo', localStorage.getItem('userId'))
  store.dispatch('post/fetchPosts')
  if (localStorage.getItem('token')) {
    store.dispatch('userInfo/fetchUserInfo', localStorage.getItem('userId'))
  }
  if (localStorage.getItem('userName') || store.getters['login/getIsAuthenticated']) {
    isLogin.value = true
  } else {
    isLogin.value = false
  }
})
</script>

<template>
  <Header></Header>
  <section class="section section-spacing">
    <div class="column" v-if="isLogin">
      <div class="card">
        <header class="card-header">
          <p class="card-header-title">发个动态吧！</p>
        </header>
        <div class="card-content has-flex">
          <figure class="image is-48x48 mr-2">
            <img class="is-rounded" :src="userAvatar" />
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
          <div class="card" @click="toPostDetail(post.id)">
            <div class="card-content">
              <div class="level">
                <div class="level-left">
                  <div class="level-item">
                    <figure class="image is-48x48">
                      <img class="is-rounded" :src="post.author.avatar" />
                    </figure>
                  </div>
                  <div class="level-item">
                    <p>
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
            </div>

            <div class="card-content">
              <div class="content">
                {{ post.content }}
              </div>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>
  <Footer></Footer>
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

