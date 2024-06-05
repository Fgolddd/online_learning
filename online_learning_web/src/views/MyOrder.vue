<script setup>
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import { toast } from 'bulma-toast'
import { onBeforeMount, reactive } from 'vue'
import api from '@/api'

const baseURL = 'http://127.0.0.1:8000'
const orderList = reactive([])

async function removeOrder(orderId) {
  await api.order.removeOrder(orderId).then((res) => {
    if (res.status === 204) {
      toast({
        message: '删除成功',
        type: 'is-success',
        position: 'top-center',
        duration: 1000,
      })
    }
  })

  orderList.value = orderList.value.filter((item) => item.id !== orderId)
}

onBeforeMount(async () => {
  const res = await api.order.getOrderList()
  console.log(res.data)
  if (res.status === 200) {
    orderList.value = res.data
  }
})
</script>
<template>
  <Header></Header>
  <section class="section-spacing">
    <div class="columns is-multiline is-centered">
      <div class="column is-full" v-for="order in orderList.value" :key="order.id">
        <div class="card">
          <div class="card-header">
            <div class="card-header-title">订单编号：{{ order.order_code }}</div>
            <div class="card-header-title">创建时间：{{ order.created_at }}</div>
          </div>
          <div class="card-content">
            <div class="columns is-multiline">
              <div class="column is-full" v-for="item in order.order_goods_set" :key="item.id">
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
                  <strong>订单金额￥{{ order.amount }}</strong>
                </div>
                <div class="level-item" v-if="order.status === '待支付'">
                  <p class="tag is-warning is-medium">{{ order.status }}</p>
                </div>
                <div class="level-item" v-if="order.status === '已支付'">
                  <p class="tag is-info is-medium">{{ order.status }}</p>
                </div>
              </div>
              <div class="level-left">
                <div class="level-item">
                  <button class="button is-danger" @click="removeOrder(order.id)">删除</button>
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
  margin-left: 20rem; /* 示例：左侧留出2rem（可根据需要调整） */
  margin-right: 20rem; /* 示例：右侧留出2rem（可根据需要调整） */
  margin-top: 2rem;
  margin-bottom: 2rem;
}
</style>