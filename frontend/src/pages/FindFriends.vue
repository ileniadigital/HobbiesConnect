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
        const similarUsers = ref<User[]>([]);
        const paginatedFriends = ref<User[]>([]);
        const errorMessage = ref<string>('');
        const currentPage = ref<number>(1);
        const itemsPerPage = ref<number>(10);
        const ageFrom = ref<number>(0);
        const ageTo = ref<number>(999);

        // Fetch similar users based on age filter
        const fetchSimilarUsers = async (filter: { ageFrom: number, ageTo: number }): Promise<void> => {
            try {
                const response = await fetch(`http://localhost:8000/api/similar-users/${mainStore.userId}?age_from=${filter.ageFrom}&age_to=${filter.ageTo}`);
                if (!response.ok) {
                    throw new Error('Failed to fetch similar users');
                }
                const data = await response.json();
                similarUsers.value = data.users;
                paginateFriends();
                console.log('Similar users:', similarUsers.value);
            } catch (error) {
                console.error('Error fetching similar users:', error);
                errorMessage.value = 'Error fetching similar users';
            }
        };

        const handleAddFriend = async ({ userId, friendId }: { userId: number, friendId: number }): Promise<void> => {
            try {
                const response = await fetch('http://localhost:8000/api/friendship/create/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ user_id: userId, friend_id: friendId })
                });
                const data = await response.json();
                if (!response.ok) {
                    throw new Error(data.message || 'Failed to add friend');
                }
                console.log('Friend added:', data);
                // alert('Friend request sent successfully!');
            } catch (error) {
                console.error('Error adding friend:', (error as any).message);
                // const errorMessage = (error as Error).message;
                // alert(`Error adding friend: ${errorMessage}`);
            }
        };

        const paginateFriends = (): void => {
            const start = (currentPage.value - 1) * itemsPerPage.value;
            const end = start + itemsPerPage.value;
            paginatedFriends.value = similarUsers.value.slice(start, end);
        };

        const changePage = (page: number): void => {
            if (page > 0 && page <= totalPages.value) {
                currentPage.value = page;
                paginateFriends();
            }
        };

        const totalPages = computed<number>(() => {
            return Math.ceil(similarUsers.value.length / itemsPerPage.value);
        });

        onMounted(async () => {
            await mainStore.fetchData();
            await fetchSimilarUsers({ ageFrom: ageFrom.value, ageTo: ageTo.value });
        });

        watch(similarUsers, (): void => {
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