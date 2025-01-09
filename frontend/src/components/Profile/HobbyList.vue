<template>
    <div class="head">
        <h2>Hobbies</h2>
        <button class="btn btn-primary" @click="showAddHobbyModal">Add Hobby</button>
    </div>
    <!-- Hobbies list -->
    <ul class="list-group">
        <li class="list-group-item" v-for="uHobby in userHobbies" :key="uHobby.hobby_id">
            <div class="d-flex justify-content-between">
                {{ uHobby.hobby }}
                <button class="btn btn-danger btn-sm" @click="showDeleteHobbyModal(uHobby.hobby_id)">Delete</button>
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
import { defineComponent, ref, onMounted } from "vue";
import { useMainStore } from "../../data/data";
import AddHobby from "./AddHobby.vue";
import DeleteHobby from "./DeleteHobby.vue";

interface UserHobby {
    hobby_id: number;
    hobby: string;
    description: string;
}

interface Hobby {
    id: number;
    name: string;
    description: string;
}

export default defineComponent({
    components: {
        AddHobby,
        DeleteHobby,
    },
    setup() {
        const mainStore = useMainStore();
        const userHobbies = ref<UserHobby[]>([]);
        const hobbies = ref<Hobby[]>([]);
        const isAddHobbyModalVisible = ref(false);
        const isDeleteHobbyModalVisible = ref(false);
        const selectedHobbyId = ref<number | null>(null);
        const userId = ref(mainStore.userId);

        // Fetch user hobbies
        const fetchUserHobbies = async () => {
            await mainStore.fetchData();
            userHobbies.value = mainStore.userHobbies as UserHobby[];
            hobbies.value = mainStore.hobbies as Hobby[];
            console.log('Hobbies in list:', hobbies.value);
        };
        onMounted(fetchUserHobbies);

        // Filter hobbies to existing ones from master list the user does not have
        const filteredHobbies = () => {
            const userHobbyIds = userHobbies.value.map(uHobby => uHobby.hobby_id);
            return hobbies.value.filter(hobby => !userHobbyIds.includes(hobby.id));
        };

        // Show Add Hobby Modal
        const showAddHobbyModal = () => {
            isAddHobbyModalVisible.value = true;
            console.log('Add Hobby Modal is visible:', isAddHobbyModalVisible.value);
        };

        // Show Delete Hobby Modal
        const showDeleteHobbyModal = (hobbyId: number) => {
            selectedHobbyId.value = hobbyId;
            isDeleteHobbyModalVisible.value = true;
            console.log('Delete Hobby Modal is visible:', isDeleteHobbyModalVisible.value);
        };

        return {
            userHobbies,
            hobbies,
            isAddHobbyModalVisible,
            isDeleteHobbyModalVisible,
            selectedHobbyId,
            showAddHobbyModal,
            showDeleteHobbyModal,
            fetchUserHobbies,
            userId,
            filteredHobbies,
        };
    }
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