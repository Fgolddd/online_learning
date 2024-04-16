<script setup>
defineProps({
  article: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <article class="message">
    <div class="message-header">
      <p>{{ article.title }}</p>
      <span class="tag is-primary">{{ article.author }}</span>
    </div>
    <div class="message-body">
      {{ article.content }}
    </div>
  </article>
</template>


