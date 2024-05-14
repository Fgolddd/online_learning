import './assets/main.css'
import '@icon-park/vue-next/styles/index.css'
import '@wangeditor/editor/dist/css/style.css'

import VMdPreview from '@kangc/v-md-editor/lib/preview';
import VMdEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import vuepressTheme from '@kangc/v-md-editor/lib/theme/vuepress.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';
import hljs from 'highlight.js';
import Prism from 'prismjs';

VMdEditor.use(githubTheme, {
    Hljs: hljs,
});

VMdPreview.use(vuepressTheme, {
    Prism,
});

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'


axios.defaults.baseURL = 'http://127.0.0.1:8000/api'
const app = createApp(App)

app.use(router, axios).use(store).use(VMdEditor).use(VMdPreview)


app.mount('#app')
