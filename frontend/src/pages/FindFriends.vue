<template>
    <div class="h3">
      {{ title }}
    </div>
  </template>
  
  <script lang="ts">
      import { defineComponent } from "vue";
  
      export default defineComponent({
          data() {
              return {
                  title: "Find Friends",
              }
          }
      })
  </script>
  
  <style scoped>
  </style>
  