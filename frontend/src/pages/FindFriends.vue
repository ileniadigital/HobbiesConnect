<template>
    <div>
        <div class="h3">{{ title }}</div>
        <!-- Add a filter -->
        <Filter @filter="fetchSimilarUsers" />
        <!-- Friends List -->
        <div v-if="paginatedFriends.length > 0">
            <div class="friend-card" v-for="friend in paginatedFriends" :key="friend.id">
                <Friend :userId="mainStore.userId ?? 0" :friendId="friend.id"
                    :name="friend.first_name + ' ' + friend.last_name" :age="friend.age ?? 0" :hobbies="friend.hobbies"
                    @add-friend="handleAddFriend" />
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
import Filter from "../components/FindFriends/Filter.vue";
import Friend from "../components/FindFriends/Friend.vue";
import Pagination from "../components/FindFriends/Pagination.vue";
import { User } from "../utils/interfaces";

export default defineComponent({
    components: {
        Filter,
        Friend,
        Pagination,
    },
    setup() {
        const mainStore = useMainStore();
        const paginatedFriends = ref<User[]>([]);
        const errorMessage = ref<string>('');
        const currentPage = ref<number>(1);
        const itemsPerPage = ref<number>(10);
        const ageFrom = ref<number>(0);
        const ageTo = ref<number>(999);

        // Fetch similar users based on age filter
        const fetchSimilarUsers = async (filter: { ageFrom: number, ageTo: number }): Promise<void> => {
            await mainStore.fetchSimilarUsers(filter);
            paginateFriends();
        };

        const handleAddFriend = async ({ userId, friendId }: { userId: number, friendId: number }): Promise<void> => {
            await mainStore.handleAddFriend(userId, friendId);
        };

        const paginateFriends = (): void => {
            const start = (currentPage.value - 1) * itemsPerPage.value;
            const end = start + itemsPerPage.value;
            paginatedFriends.value = mainStore.similarUsers.slice(start, end);
        };

        const changePage = (page: number): void => {
            if (page > 0 && page <= totalPages.value) {
                currentPage.value = page;
                paginateFriends();
            }
        };

        const totalPages = computed<number>(() => {
            return Math.ceil(mainStore.similarUsers.length / itemsPerPage.value);
        });

        onMounted(async () => {
            await mainStore.fetchData();
            await fetchSimilarUsers({ ageFrom: ageFrom.value, ageTo: ageTo.value });
        });

        watch(mainStore.similarUsers, (): void => {
            paginateFriends();
        });

        return {
            title: "Find Friends",
            errorMessage,
            currentPage,
            itemsPerPage,
            ageFrom,
            ageTo,
            paginatedFriends,
            totalPages,
            changePage,
            fetchSimilarUsers,
            handleAddFriend,
            mainStore,
        };
    },
});
</script>

<style scoped>
.friend-card {
    margin: 1.5rem 0 1.5rem 0;
}
</style>