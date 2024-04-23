<script setup>
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
const router = useRouter()
const store = useStore()
const postId = Number(router.currentRoute.value.params.postId)
const post = store.getters['post/getPostById'](postId)
const userInfo = store.getters['userInfo/getUserInfo']

const commentText = ref('')
</script>
<template>
  <Header></Header>
  <section class="section-spacing">
    <div class="card">
      <div class="card-content">
        <div class="level">
          <div class="level-left">
            <div class="level-item">
              <figure class="image is-48x48">
                <img class="is-rounded" :src="post.author.avatar" alt="Placeholder image" />
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
      <hr />
      <div class="card-content">
        <div class="level">
          <div class="level-left">
            <div class="level-item">
              <figure class="image is-48x48">
                <img :src="userInfo.avatar" alt="Placeholder image" />
              </figure>
            </div>
          </div>

          <div class="level-item" @submit.prevent="submitComment">
            <input
              class="input is-primary is-medium"
              type="text"
              v-model="commentText"
              placeholder="在这里写评论..."
              style="margin-left: 1rem; margin-right: 1rem"
            />
          </div>
          <div class="level-right">
            <div class="level-item">
              <button type="submit" class="button is-primary is-medium">评论</button>
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
  margin-left: 24rem;
  margin-right: 24rem;
  margin-top: 1rem;
  margin-bottom: 1rem;
}
.cc-center {
  justify-content: center;
}
.p-text {
  text-align: center;
}
</style>

