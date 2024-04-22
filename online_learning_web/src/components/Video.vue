<script setup>
import { onMounted, onBeforeUnmount, ref, defineProps } from 'vue'
import videojs from 'video.js'
import 'video.js/dist/video-js.css'

const props = defineProps({
  source: {
    type: String,
    required: true,
  },
})

const videoContainer = ref(null)
const videoElement = ref(null)

let player = null

const initializePlayer = () => {
  const options = {
    controls: true,
    autoplay: false,
    preload: 'auto',
    sources: [
      {
        src: props.source,
        type: 'video/mp4',
      },
    ],
  }

  player = videojs(videoElement.value, options, () => {
    console.log('Video player is ready!')
  })
}

const disposePlayer = () => {
  if (player) {
    player.dispose()
    player = null
  }
}

onMounted(initializePlayer)
onBeforeUnmount(disposePlayer)
</script>

<template>
  <div ref="videoContainer" class="video-container">
    <video ref="videoElement" class="video-js"></video>
  </div>
</template>

<style scoped>
.video-container {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
}

.video-js {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>