<template>
    <div class="head">
        <h2>Hobbies</h2>
        <button class="btn btn-primary" @click="showAddHobbyModal">Add Hobby</button>
    </div>
    <!-- Hobbies list -->
    <ul class="list-group">
        <li class="list-group-item" v-for="uHobby in userHobbies" :key="uHobby.hobby_id">
            {{ uHobby.hobby }}
        </li>
        <li v-if="userHobbies.length === 0" class="list-group-item">No hobbies found.</li>
    </ul>
    <!-- Add Hobby Modal -->
    <AddHobby :visible="isAddHobbyModalVisible" :userId="userId" @close="isAddHobbyModalVisible = false"
        @hobby-added="fetchUserHobbies" :hobbies="hobbies" />
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import { useMainStore } from "../data/data";
import AddHobby from "./AddHobby.vue";

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
    },
    setup() {
        const mainStore = useMainStore();
        const userHobbies = ref<UserHobby[]>([]);
        const hobbies = ref<Hobby[]>([]);
        const isAddHobbyModalVisible = ref(false);
        const userId = ref(mainStore.userId);

        // Fetch user hobbies
        const fetchUserHobbies = async () => {
            await mainStore.fetchData();
            userHobbies.value = mainStore.userHobbies as UserHobby[];
            hobbies.value = mainStore.hobbies as Hobby[];
            console.log('Hobbies in list:', hobbies.value);

        };
        onMounted(fetchUserHobbies);

        // Show Add Hobby Modal
        const showAddHobbyModal = () => {
            isAddHobbyModalVisible.value = true;
            console.log('Add Hobby Modal is visible:', isAddHobbyModalVisible.value);
        };

        return {
            userHobbies,
            hobbies,
            isAddHobbyModalVisible,
            showAddHobbyModal,
            fetchUserHobbies,
            userId
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
    width: 17rem;
}
</style>