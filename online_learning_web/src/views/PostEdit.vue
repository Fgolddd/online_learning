<script setup>
import Footer from '../components/Footer.vue'
import Header from '../components/Header.vue'
import { onBeforeUnmount, ref, shallowRef, onMounted } from 'vue'
import { Editor, Toolbar } from '@wangeditor/editor-for-vue'
import { toast } from 'bulma-toast'
import axios from 'axios'
// 编辑器实例，必须用 shallowRef
const editorRef = shallowRef()
const mode = ref('simple')
// 内容 HTML
const valueHtml = ref('')

// 模拟 ajax 异步获取内容
onMounted(() => {
  setTimeout(() => {
    valueHtml.value = ''
  }, 1500)
})

const toolbarConfig = {}
const editorConfig = { placeholder: '请输入内容...' }

// 组件销毁时，也及时销毁编辑器
onBeforeUnmount(() => {
  const editor = editorRef.value
  if (editor == null) return
  editor.destroy()
})

const handleCreated = (editor) => {
  editorRef.value = editor // 记录 editor 实例，重要！
}

async function publishContent() {
  try {
    // 确保编辑器实例已创建
    if (!editorRef.value) return

    // 获取编辑器的HTML内容
    const htmlContent = editorRef.value.getHtml()
    const tempElement = document.createElement('div')
    tempElement.innerHTML = htmlContent
    const content = tempElement.textContent

    // 发送POST请求到后端，这里使用fetch API作为示例
    const response = await axios.post(
      'post/',
      {
        content: content,
      },
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      },
    )
    if (response.status === 201) {
      toast({
        message: '发布成功',
        type: 'is-success',
        position: 'top-center',
        duration: 2000,
      })
    } else {
      console.error('内容发布失败')
      // 处理错误情况
    }
  } catch (error) {
    console.error('请求错误:', error)
    // 错误处理
  }
}
</script>
<template>
  <Header></Header>
  <section class="section-spacing">
    <div class="card">
      <div class="card-header">
        <p class="card-header-title">发个动态吧！</p>
      </div>
      <div class="card-content">
        <div style="border: 1px solid #ccc">
          <Toolbar
            style="border-bottom: 1px solid #ccc"
            :editor="editorRef"
            :defaultConfig="toolbarConfig"
            :mode="mode"
          />
          <Editor
            style="height: 300px; overflow-y: hidden"
            v-model="valueHtml"
            :defaultConfig="editorConfig"
            :mode="mode"
            @onCreated="handleCreated"
          />
        </div>
      </div>
      <div class="card-content">
        <div class="level">
          <div class="level-left"></div>

          <div class="level-right">
            <div class="level-item">
              <button class="button is-primary" @click="publishContent">发布</button>
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