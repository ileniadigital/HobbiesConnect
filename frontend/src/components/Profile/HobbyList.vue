<template>
    <div class="head">
        <h2>Hobbies</h2>
        <button class="btn btn-primary" @click="showAddHobbyModal">Add Hobby</button>
    </div>
    <!-- Hobbies list -->
    <ul class="list-group">
        <li class="list-group-item" v-for="uHobby in userHobbies" :key="uHobby.hobby.id">
            <div class="d-flex justify-content-between">
                {{ uHobby.hobby.name }}
                <button class="btn btn-danger btn-sm"
                    @click="showDeleteHobbyModal(userId, uHobby.hobby.id)">Delete</button>
            </div>
        </li>
        <li v-if="userHobbies.length === 0" class="list-group-item">No hobbies found.</li>
    </ul>
    <!-- Add Hobby Modal -->
    <AddHobby :visible="isAddHobbyModalVisible" :userId="userId" @close="isAddHobbyModalVisible = false"
        @hobby-added="fetchUserHobbies" :hobbies="filteredHobbies()" />
    <!-- Delete Hobby Modal -->
    <DeleteHobby :visible="isDeleteHobbyModalVisible" :userId="userId" :hobbyId="selectedHobbyId ?? 0"
        @close="isDeleteHobbyModalVisible = false" @hobby-deleted="fetchUserHobbies" />
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, watch } from "vue";
import { useMainStore } from "../../data/data";
import AddHobby from "./AddHobby.vue";
import DeleteHobby from "./DeleteHobby.vue";
import { UserHobby, Hobbies } from "../../utils/interfaces";

export default defineComponent({
    components: {
        AddHobby,
        DeleteHobby,
    },
    setup() {
        const mainStore = useMainStore();
        const userHobbies = ref<UserHobby[]>([]);
        const isAddHobbyModalVisible = ref<boolean>(false);
        const isDeleteHobbyModalVisible = ref<boolean>(false);
        const selectedHobbyId = ref<number | null>(null);
        const userId = ref<number>(mainStore.get_user_id ?? 0);

        const fetchUserHobbies = async () => {
            await mainStore.fetchData();
            userHobbies.value = mainStore.userHobbies;
        };

        watch(
            () => mainStore.get_user_id,
            async (newUserId: number | null) => {
                if (newUserId) {
                    userId.value = newUserId;
                    await fetchUserHobbies();
                }
            },
            { immediate: true }
        );

        onMounted(async () => {
            await mainStore.fetchData();
        });

        // Filter hobbies to existing ones from master list the user does not have
        const filteredHobbies = (): Hobbies[] => {
            const userHobbyIds = userHobbies.value.map(uHobby => uHobby.hobby.id);
            return mainStore.hobbies.filter(hobby => !userHobbyIds.includes(hobby.id));
        };

        const showAddHobbyModal = () => {
            isAddHobbyModalVisible.value = true;
        };

        const showDeleteHobbyModal = (userHobbyId: number, hobbyId: number) => {
            userId.value = userHobbyId;
            selectedHobbyId.value = hobbyId;
            isDeleteHobbyModalVisible.value = true;
            // this.userId = mainStore.get_user_id;
            console.log("Selected hobby id:", selectedHobbyId.value);
            console.log("User id in hobby list:", userId.value);
        };

        onMounted(fetchUserHobbies);

        return {
            userHobbies,
            isAddHobbyModalVisible,
            isDeleteHobbyModalVisible,
            selectedHobbyId,
            userId,
            fetchUserHobbies,
            showAddHobbyModal,
            showDeleteHobbyModal,
            filteredHobbies,
        };
    },
});
</script>

<style scoped>
.head {
    display: flex;
    align-items: center;
    gap: 3rem;
    margin-bottom: 1rem;
}

.btn,
.btn:active,
.btn:hover {
    padding: 0.5rem 1rem;
    background-color: #FCE26D;
    border: none;
    color: black;
}

.btn:hover {
    font-weight: bold;
}

.list-group {
    width: 20rem;
}

.btn-danger,
.btn-danger:hover {
    background-color: red;
    color: white;
}

.btn-danger:hover {
    font-weight: bold;
}
</style>