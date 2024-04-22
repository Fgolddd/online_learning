<script setup>
import { computed } from 'vue'
import { useStore } from 'vuex'
const store = useStore()
const collections = store.getters['userInfo/getUserInfo'].collections
const totalPrice = computed(() => {
  let total = 0
  collections.forEach((item) => {
    total += Number(item.price)
  })
  return total.toFixed(2)
})
</script>
<template>
  <section class="section-spacing">
    <div class="columns is-centered is-multiline">
      <div class="column is-12" v-for="(item, index) in collections" :key="index">
        <div class="level">
          <div class="level-left">
            <div class="level-item">
              <figure class="image is-48x48">
                <img :src="item.course_cover" />
              </figure>
            </div>
            <div class="level-item">
              <div class="content">
                <p class="title is-5">{{ item.name }}</p>
              </div>
            </div>
            <div class="level-item">
              <div class="content">
                <p class="title is-5">￥{{ item.price }}</p>
              </div>
            </div>
          </div>
          <div class="level-right">
            <button class="button is-danger" @click="deleteItem(item.id)">移出购物车</button>
          </div>
        </div>
        <hr />
      </div>
    </div>
    <div class="column">
      <div class="level">
        <div class="level-left">
          <p class="title is-5">总计：￥{{ totalPrice }}</p>
        </div>
        <div class="level-right">
          <button class="button is-primary" @click="pay">去支付</button>
        </div>
      </div>
      "
    </div>
  </section>
</template>
<style scoped>
.section-spacing {
  margin-left: 20rem; /* 示例：左侧留出2rem（可根据需要调整） */
  margin-right: 20rem; /* 示例：右侧留出2rem（可根据需要调整） */
  margin-top: 2rem;
  margin-bottom: 2rem;
}
</style>