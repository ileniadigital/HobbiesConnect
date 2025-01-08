<template>
    <div class="h3">
        {{ title }}
    </div>
    <!-- Add a filter -->
    <Filter @filter-age="filterFriendsByAge" />
    <!-- Friends List -->
    <div class="friend-card" v-for="friend in paginatedFriends" :key="friend.name">
        <Friend :name="friend.name" :hobbies="friend.hobbies" :age="friend.age" />
    </div>
    <!-- Pagination -->
    <Pagination :currentPage="currentPage" :totalPages="totalPages" @page-changed="changePage" />
</template>

<script lang="ts">
import { defineComponent, ref, computed } from "vue";
import { useMainStore } from "../data/data";
import Filter from "../components/Filter.vue";
import Friend from "../components/Friend.vue";
import Pagination from "../components/Pagination.vue";

export default defineComponent({
    components: {
        Filter,
        Friend,
        Pagination,

    },
    setup() {
        const mainStore = useMainStore();
        const currentPage = ref(1);
        const itemsPerPage = ref(10);
        const ageFrom = ref(0);
        const ageTo = ref(Infinity);

        // CHANGE THIS TO GET IT FROM MAIN STORE
        const friends = ref([
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
        ]);
        const filteredFriends = computed(() => {
            return friends.value.filter(friend => friend.age >= ageFrom.value && friend.age <= ageTo.value);
        });

        const paginatedFriends = computed(() => {
            const start = (currentPage.value - 1) * itemsPerPage.value;
            const end = start + itemsPerPage.value;
            return filteredFriends.value.slice(start, end);
        });

        const totalPages = computed(() => {
            return Math.ceil(filteredFriends.value.length / itemsPerPage.value);
        });

        const changePage = (page: number) => {
            if (page > 0 && page <= totalPages.value) {
                currentPage.value = page;
            }
        };

        const filterFriendsByAge = (ageFromValue: number, ageToValue: number) => {
            ageFrom.value = ageFromValue;
            ageTo.value = ageToValue;
        };

        return {
            title: "Find Friends",
            // name: mainStore.user.first_name,
            currentPage,
            itemsPerPage,
            ageFrom,
            ageTo,
            friends,
            paginatedFriends,
            totalPages,
            changePage,
            filterFriendsByAge
        };
    }
});
</script>

<style scoped>
.friend-card {
    margin: 1.5rem 0 1.5rem 0;
}
</style>