<script setup>
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import { onBeforeMount, reactive, ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import api from '../api/index'
import { toast } from 'bulma-toast'

const router = useRouter()
const store = useStore()
const postId = Number(router.currentRoute.value.params.postId)
// const post = store.getters['post/getPostById'](postId)
const post = reactive({})
const userInfo = store.getters['user/getUserInfo']
const comments = reactive([])
const commentText = ref('')

async function submitComment() {
  try {
    const form = { post: postId, content: commentText.value }
    const res = await api.post.addComment(form)

    const newComment = res.data
    comments.value.push(newComment)
    if (res.status === 201) {
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
}

function addPrefixToImages(content, mediaUrl) {
  return content.replace(/!\[\]\((.*)\)/g, '![](' + mediaUrl + '/$1)')
}
const baseURL = 'http://127.0.0.1:8000'

async function deletePost() {
  const res = await api.post.deletePost(postId)
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

onBeforeMount(async () => {
  const res = await api.post.getPost(postId)
  post.value = res.data
  comments.value = res.data.comments
})
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
                <img class="is-rounded" :src="post.value?.author.avatar" alt="Placeholder image" />
              </figure>
            </div>
            <div class="level-item">
              <p>
                <strong>{{ post.value?.author.username }}</strong>
              </p>
            </div>
          </div>
          <div class="level-right">
            <div class="level-item">
              <time>发布于 {{ post.value?.created_at }}</time>
            </div>
          </div>
        </div>
      </div>
      <div class="card-content">
        <div class="level">
          <div class="level-left">
            <div class="content">
              <v-md-preview :text="addPrefixToImages(post.value?.content, baseURL)"></v-md-preview>
            </div>
          </div>
          <div class="level-right">
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
          <div class="column is-full" v-for="comment in comments.value" :key="comment.id">
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
            <hr />
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

