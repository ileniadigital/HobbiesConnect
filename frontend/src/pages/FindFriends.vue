<template>
    <div class="h3">
        Hi, {{ name }}
    </div>
    <!-- Add a filter -->
    <Filter />
    <!-- Friends List -->
    <div class="friend-card" v-for="friend in friends" :key="friend.name">
        <Friend :name="friend.name" :hobbies="friend.hobbies" />
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Filter from "../components/Filter.vue";
import Friend from "../components/Friend.vue";

export default defineComponent({
    components: {
        Filter,
        Friend
    },
    data() {
        return {
            name: "Ilenia", // Change this to dynamic data
            friends: [
                { name: "Alice", age: 25, hobbies: ["reading", "hiking"] },
                { name: "Bob", age: 30, hobbies: ["swimming", "biking"] },
                { name: "Charlie", age: 35, hobbies: ["cooking", "painting"] },
            ]
        };
    }
})
</script>

<style scoped>
.friend-card {
    margin: 1.5rem 0 1.5rem 0;
}
</style>