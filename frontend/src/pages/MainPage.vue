<template>
  <div>
    <div class="h1">
      {{ title }}
    </div>
  </div>
</template>

<script lang="ts">
  import { defineComponent } from "vue";
  import Header from "@/components/Header.vue";

  export default defineComponent({
      components: {
          Header
      },
      data() {
          return {
              title: "Main Page",
          }
      }
  })
</script>

<style scoped>
</style>
