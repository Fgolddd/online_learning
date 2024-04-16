import './assets/main.css'
import '@icon-park/vue-next/styles/index.css'
import 'bulma-toast/dist/bulma-toast.cjs'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import axios from 'axios'
axios.defaults.baseURL = 'http://127.0.0.1:8000'
const app = createApp(App)

app.use(router, axios).use(store)


app.mount('#app')
