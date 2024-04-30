<script setup>
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { toast } from 'bulma-toast'
const router = useRouter()
const store = useStore()
const postId = Number(router.currentRoute.value.params.postId)
const post = store.getters['post/getPostById'](postId)

const userInfo = store.getters['userInfo/getUserInfo']
const comments = post.comments
const commentText = ref('')
const isAuth = ref(post.author.id === Number(localStorage.getItem('userId')))

async function submitComment() {
  try {
    const credentials = { post: postId, content: commentText.value }
    const response = await axios.post('comment/', credentials, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    })
    const newComment = response.data

    comments.push(newComment)
    if (response.status === 201) {
      toast({
        message: '评论成功',
        type: 'is-success',
        position: 'top-center',
        duration: 2000,
      })
    }
    setTimeout(() => {
      router.push(`/post/${postId}`)
    }, 1000) // 延迟 1 秒后执行路由跳转
  } catch (error) {
    console.error(error)
    // 处理登录失败...
  }
  setTimeout(() => {
    router.push('/')
  }, 1000) // 延迟 1 秒后执行路由跳转
}

async function deletePost() {
  const res = await axios.delete(`post/${postId}/`, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('token')}`,
    },
  })
  if (res.status === 204) {
    toast({
      message: '删除成功',
      type: 'is-success',
      position: 'top-center',
      duration: 2000,
    })
    setTimeout(() => {
      router.push('/')
    }, 1000) // 延迟 1 秒后执行路由跳转
  }
}
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
        <div class="level">
          <div class="level-left">
            <div class="content">
              {{ post.content }}
            </div>
          </div>
          <div v-if="isAuth" class="level-right">
            <button class="button is-danger" @click="deletePost">删除</button>
          </div>
        </div>
      </div>

      <hr />
      <div class="card-content">
        <div class="level">
          <div class="level-left">
            <div class="level-item">
              <figure class="image is-48x48">
                <img class="is-rounded" :src="userInfo.avatar" alt="Placeholder image" />
              </figure>
            </div>
          </div>
          <form @submit.prevent="submitComment" class="is-flex">
            <div class="level-item li-spacing">
              <div class="field">
                <div class="control">
                  <input
                    class="input is-primary is-medium"
                    type="text"
                    v-model="commentText"
                    placeholder="在这里写评论..."
                    style="margin-left: 1rem; margin-right: 1rem"
                  />
                </div>
              </div>
            </div>

            <div class="level-item li-spacing">
              <div class="field">
                <div class="control">
                  <button type="submit" class="button is-primary is-medium">评论</button>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
      <div class="card-content">
        <div class="columns is-multiline">
          <div class="column is-full" v-for="comment in comments" :key="comment.id">
            <div class="media">
              <div class="media-left">
                <figure class="image is-48x48">
                  <img class="is-rounded" :src="comment.user.avatar" alt="Placeholder image" />
                </figure>
              </div>
              <div class="media-content">
                {{ comment.content }}
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
.section-spacing {
  margin-left: 24rem;
  margin-right: 24rem;
  margin-top: 1rem;
  margin-bottom: 1rem;
}
.li-spacing {
  margin-left: 5rem;
  margin-right: 5rem;
}
.cc-center {
  justify-content: center;
}
.p-text {
  text-align: center;
}
</style>

