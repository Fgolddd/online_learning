<script setup>
import { ref } from 'vue'

const articles = ref([
  // 假设这是从 API 获取的文章数据
  {
    id: 1,
    title: '标题一',
    summary: '这是文章一的摘要...',
    commentsCount: 7,
    likesCount: 98,
  },
  {
    id: 2,
    title: '标题二',
    summary: '这是文章二的摘要...',
    commentsCount: 23,
    likesCount: 65,
  },
  // 更多文章...
])
</script>

<template>
  <section class="section">
    <div class="columns is-mobile is-centered">
      <div class="column is-half">
        <div class="card">
          <header class="card-header">
            <p class="card-header-title">发个动态吧！</p>
          </header>
          <div class="card-content">
            <div class="content is-flex">
              <figure class="image is-24x24">
                <img class="is-rounded" src="" />
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
      </div>
    </div>

    <div class="columns is-multiline is-centered">
      <div class="column is-half">
        <article v-for="article in articles" :key="article.id" class="column">
          <div class="card">
            <header class="card-header">
              <p class="card-header-title">
                {{ article.title }}
              </p>
              <a href="#" class="card-header-icon" aria-label="more options">
                <span class="icon">
                  <i class="fas fa-angle-down" aria-hidden="true"></i>
                </span>
              </a>
            </header>
            <div class="card-content">
              <div class="content">
                {{ article.summary }}
              </div>
            </div>
            <footer class="card-footer">
              <a href="#" class="card-footer-item">评论({{ article.commentsCount }})</a>
              <a href="#" class="card-footer-item">点赞({{ article.likesCount }})</a>
            </footer>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

