<script setup>
import { onBeforeMount, reactive, ref } from 'vue'
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import api from '@/api'
import { computed } from 'vue'

const order = reactive({})
const totalPrice = ref(0)

const baseURL = 'http://127.0.0.1:8000'
onBeforeMount(async () => {
  const res = await api.order.createOrder()
  if (res.status === 201) {
    order.value = res.data
  }

  totalPrice.value = computed(() => {
    let total = 0
    order.value.order_goods_set.forEach((item) => {
      total += Number(item.price)
    })
    return total.toFixed(2)
  })
})
</script>
<template>
  <Header></Header>
  <section class="section-spacing">
    <div class="card">
      <div class="card-header">
        <p class="card-header-title">订单编号：{{ order.value?.order_code }}</p>
        <p class="card-header-title">创建时间：{{ order.value?.created_at }}</p>
      </div>
      <div class="card-content">
        <div class="columns is-multiline">
          <div class="column is-full" v-for="item in order.value?.order_goods_set" :key="item.id">
            <div class="box">
              <div class="media">
                <div class="media-left">
                  <figure class="image is-64x64">
                    <img :src="baseURL + item.course.course_cover" alt="Image" />
                  </figure>
                </div>
                <div class="media-left">
                  {{ item.course.name }}
                </div>
                <div class="media-left">￥{{ item.course.price }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="card-content">
        <div class="level">
          <div class="level-left">
            <div class="level-item">
              <p class="title">总价：￥ {{ totalPrice.value }}</p>
            </div>
          </div>
          <div class="level-left">
            <div class="level-item">
              <button class="button is-primary">微信支付</button>
            </div>
            <div class="level-item">
              <button class="button is-info">支付宝支付</button>
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
  margin-left: 20rem; /* 示例：左侧留出2rem（可根据需要调整） */
  margin-right: 20rem; /* 示例：右侧留出2rem（可根据需要调整） */
  margin-top: 2rem;
  margin-bottom: 2rem;
}
</style>