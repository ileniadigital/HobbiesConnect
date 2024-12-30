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
                { name: "David", age: 40, hobbies: ["gardening", "fishing"] },
                { name: "Eve", age: 22, hobbies: ["dancing", "singing"] },
                { name: "Frank", age: 28, hobbies: ["running", "gaming"] },
                { name: "Grace", age: 32, hobbies: ["writing", "traveling"] },
                { name: "Hank", age: 27, hobbies: ["photography", "skiing"] },
                { name: "Ivy", age: 24, hobbies: ["knitting", "yoga"] },
                { name: "Jack", age: 29, hobbies: ["surfing", "climbing"] },
                { name: "Karen", age: 31, hobbies: ["drawing", "sculpting"] },
                { name: "Leo", age: 26, hobbies: ["fishing", "hiking"] },
                { name: "Mona", age: 33, hobbies: ["baking", "gardening"] },
                { name: "Nate", age: 34, hobbies: ["cycling", "swimming"] },
                { name: "Olivia", age: 23, hobbies: ["reading", "writing"] },
                { name: "Paul", age: 36, hobbies: ["gaming", "coding"] },
                { name: "Quinn", age: 37, hobbies: ["painting", "dancing"] },
                { name: "Rachel", age: 38, hobbies: ["singing", "acting"] },
                { name: "Steve", age: 39, hobbies: ["cooking", "biking"] },
                { name: "Tina", age: 40, hobbies: ["yoga", "meditation"] },
                { name: "Uma", age: 41, hobbies: ["hiking", "camping"] },
                { name: "Victor", age: 42, hobbies: ["running", "swimming"] },
                { name: "Wendy", age: 43, hobbies: ["gardening", "knitting"] },
                { name: "Xander", age: 44, hobbies: ["climbing", "surfing"] },
                { name: "Yara", age: 45, hobbies: ["painting", "drawing"] },
                { name: "Zane", age: 46, hobbies: ["gaming", "coding"] }
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