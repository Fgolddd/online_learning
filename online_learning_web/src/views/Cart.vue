<script setup>
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import { computed, onMounted } from 'vue'
import { useStore } from 'vuex'
const store = useStore()
const cart = store.getters['cart/getCart']
const totalPrice = computed(() => {
  let total = 0
  cart.forEach((item) => {
    total += Number(item.course.price)
  })
  return total.toFixed(2)
})

onMounted(() => {
  store.dispatch('cart/fetchCart')
})
</script>
<template>
  <Header></Header>
  <section class="section-spacing">
    <div class="columns is-centered is-multiline">
      <div class="column is-12" v-for="(item, index) in cart" :key="index">
        <div class="level">
          <div class="level-left">
            <div class="level-item">
              <figure class="image is-48x48">
                <img :src="item.course.course_cover" />
              </figure>
            </div>
            <div class="level-item">
              <div class="content">
                <p class="title is-5">{{ item.course.name }}</p>
              </div>
            </div>
            <div class="level-item">
              <div class="content">
                <p class="title is-5">￥{{ item.course.price }}</p>
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
    </div>
  </section>
  <Footer></Footer>
</template>
<style scoped>
.section-spacing {
  margin-left: 20rem; /* 示例：左侧留出2rem（可根据需要调整） */
  margin-right: 20rem; /* 示例：右侧留出2rem（可根据需要调整） */
  margin-top: 2rem;
  margin-bottom: 2rem;
}
</style>