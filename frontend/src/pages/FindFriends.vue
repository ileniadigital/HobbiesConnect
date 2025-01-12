<template>
    <div>
        <div class="h3">{{ title }}</div>
        <!-- Add a filter -->
        <Filter @filter="fetchSimilarUsers"/>
        <!-- Friends List -->
        <div v-if="paginatedFriends.length > 0">
            <div class="friend-card" v-for="friend in paginatedFriends" :key="friend.id">
                <Friend :name="friend.first_name + ' ' + friend.last_name" :age="friend.age ?? 0"
                    :hobbies="friend.hobbies" />
            </div>
        </div>
        <div v-else class="alert alert-info mt-3">
            No similar friends available
        </div>
        <!-- Pagination -->
        <Pagination :currentPage="currentPage" :totalPages="totalPages" @page-changed="changePage" />
    </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, onMounted, watch } from "vue";
import { useMainStore } from "../data/data";
import Filter from "../components/Filter.vue";
import Friend from "../components/Friend.vue";
import Pagination from "../components/Pagination.vue";
import { User } from "../utils/interfaces";

export default defineComponent({
    components: {
        Filter,
        Friend,
        Pagination,
    },
    setup() {
        const mainStore = useMainStore();
        const similarUsers = ref<User[]>([]);
        const filteredFriends = ref<User[]>([]);
        const paginatedFriends = ref<User[]>([]);
        const errorMessage = ref<string>('');
        const currentPage = ref<number>(1);
        const itemsPerPage = ref<number>(10);
        const ageFrom = ref<number>(0);
        const ageTo = ref<number>(999);

        const fetchSimilarUsers = async (filter: { ageFrom: number, ageTo: number }) => {
            try {
                const response = await fetch(`http://127.0.0.1:8000/api/similar-users/${mainStore.userId}?age_from=${filter.ageFrom}&age_to=${filter.ageTo}`);
                if (!response.ok) {
                    throw new Error('Failed to fetch similar users');
                }
                const data = await response.json();
                similarUsers.value = data.users;
                console.log('Similar users:', similarUsers.value);
            } catch (error) {
                console.error('Error fetching similar users:', error);
                errorMessage.value = 'Error fetching similar users';
            }
        };

        const paginateFriends = () => {
            const start = (currentPage.value - 1) * itemsPerPage.value;
            const end = start + itemsPerPage.value;
            paginatedFriends.value = filteredFriends.value.slice(start, end);
        };

        const changePage = (page: number) => {
            if (page > 0 && page <= totalPages.value) {
                currentPage.value = page;
                paginateFriends();
            }
        };

        const totalPages = computed(() => {
            return Math.ceil(filteredFriends.value.length / itemsPerPage.value);
        });

        onMounted(() => {
            fetchSimilarUsers({ ageFrom: ageFrom.value, ageTo: ageTo.value });
        });

        watch(similarUsers, () => {
            paginateFriends();
        });

        return {
            title: "Find Friends",
            similarUsers,
            errorMessage,
            currentPage,
            itemsPerPage,
            ageFrom,
            ageTo,
            filteredFriends,
            paginatedFriends,
            totalPages,
            changePage,
            fetchSimilarUsers,
        };
    },
});
</script>

<style scoped>
.friend-card {
    margin: 1.5rem 0 1.5rem 0;
}
</style>