<script setup>
import router from '@/router'
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import { computed, onBeforeMount, reactive, ref } from 'vue'
import { toast } from 'bulma-toast'
import api from '@/api'

const cart = reactive([])

const totalPrice = ref(0)
function deleteItem(id) {
  api.cart.deleteItem(id)
  cart.value.filter((item) => item.id !== id)
  toast({
    message: '移除成功',
    type: 'is-success',
    position: 'top-center',
    duration: 2000,
  })
}

const toOrder = () => {
  router.push('/order')
}

onBeforeMount(async () => {
  const res = await api.cart.getCartList()
  if (res.status === 200) {
    cart.value = res.data
  }

  totalPrice.value = computed(() => {
    let total = 0
    cart.value.forEach((item) => {
      total += Number(item.course.price)
    })
    return total.toFixed(2)
  })
})
</script>
<template>
  <Header></Header>
  <section class="section-spacing">
    <div class="columns is-centered is-multiline">
      <div class="column is-12" v-for="(item, index) in cart.value" :key="index">
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
          <p class="title is-5">总计：￥{{ totalPrice.value }}</p>
        </div>
        <div class="level-right">
          <button class="button is-primary" @click="toOrder">支付</button>
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