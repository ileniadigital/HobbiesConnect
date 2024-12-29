<template>
    <div class="h3">
        Hi, {{ name }}
    </div>
    <!-- Add a filter -->
    <Filter @filter-age="filterFriendsByAge" />
    <!-- Friends List -->
    <div class="friend-card" v-for="friend in filteredFriends" :key="friend.name">
        <Friend :name="friend.name" :hobbies="friend.hobbies" :age="friend.age" />
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Filter from "../components/Filter.vue";
import Friend from "../components/Friend.vue";

export default defineComponent({
    components: {
        Filter,
        Friend,

    },
    data() {
        return {
            name: "Ilenia", // Change this to dynamic data
            friends: [
                { name: "Alice", age: 25, hobbies: ["reading", "hiking"] },
                { name: "Bob", age: 30, hobbies: ["swimming", "biking"] },
                { name: "Charlie", age: 35, hobbies: ["cooking", "painting"] },
            ],
            ageFrom: 0,
            ageTo: Infinity,
        };
    },
    computed: {
        filteredFriends() {
            if (this.ageFrom === null || this.ageTo === null) {
                return this.friends;
            }
            return this.friends.filter(friend => friend.age >= this.ageFrom && friend.age <= this.ageTo);
        }
    },
    methods: {
        filterFriendsByAge(ageFrom: number, ageTo: number) {
            this.ageFrom = ageFrom;
            this.ageTo = ageTo;
        }
    }
})
</script>

<style scoped>
.friend-card {
    margin: 1.5rem 0 1.5rem 0;
}
</style>