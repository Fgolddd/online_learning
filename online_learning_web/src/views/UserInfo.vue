<script setup>
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import { useStore } from 'vuex'

const store = useStore()
const userInfo = store.getters['user/getUserInfo']
</script>
<template>
  <Header></Header>
  <section class="section-spacing">
    <div class="card">
      <div class="card-image">
        <figure class="image is-1by1">
          <img class="" :src="userInfo.avatar" alt="Placeholder image" />
        </figure>
      </div>
      <div class="card-content">
        <div class="media">
          <div class="media-content">
            <div class="level">
              <div class="level-left">
                <div class="level-item">
                  <p class="title is-3 p-text">用户名：{{ userInfo.username }}</p>
                </div>
              </div>
              <div class="level-right">
                <div class="level-item">
                  <button class="button">修改</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="card-content">
        <div class="media">
          <div class="media-content">
            <div class="level">
              <div class="level-left">
                <div class="level-item">
                  <p class="title is-3 p-text">手机号：{{ userInfo.phone }}</p>
                </div>
              </div>
              <div class="level-right">
                <div class="level-item">
                  <button class="button">修改</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="card-content">
        <div class="media">
          <div class="media-content">
            <div class="level">
              <div class="level-left">
                <div class="level-item">
                  <p class="title is-3 p-text">密码：要改密码吗 -----></p>
                </div>
              </div>
              <div class="level-right">
                <div class="level-item">
                  <button class="button is-danger">修改</button>
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
.section-spacing {
  margin-left: 30rem;
  margin-right: 30rem;
  margin-top: 1rem;
  margin-bottom: 1rem;
}
.is-centered {
  justify-content: center;
}
.cc-center {
  justify-content: center;
}
.p-text {
  text-align: center;
}
/* 在您的 CSS 文件中添加以下样式 */
.is-centered {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

