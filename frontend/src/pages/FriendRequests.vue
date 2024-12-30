<template>
  <div>
    <div class="h1">
      {{ title }}
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  components: {
  },
  data() {
    return {
      title: "Friend Requests",
    }
  }
})
</script>

<style scoped></style>