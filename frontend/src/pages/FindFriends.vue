<template>
    <div class="h3">
        Hi, {{ name }}
    </div>
    <!-- Add a filter -->
    <Filter />
    <!-- Friends List -->
    <div v-for="friend in friends" :key="friend.name">
        <div>{{ friend.name }} is {{ friend.age }} years old</div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Filter from "../components/Filter.vue";

export default defineComponent({
    components: {
        Filter
    },
    data() {
        return {
            name: "Ilenia", // Change this to dynamic data
            friends: [
                { name: "Alice", age: 25 },
                { name: "Bob", age: 30 },
                { name: "Charlie", age: 35 },
            ]
        };
    }
})
</script>

<style scoped></style>