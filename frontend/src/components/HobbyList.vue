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
    <AddHobby :visible="isAddHobbyModalVisible" @close="isAddHobbyModalVisible = false"
        @hobby-added="fetchUserHobbies" />
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import { useMainStore } from "../data/data";
import AddHobby from "./AddHobby.vue";

interface Hobby {
    hobby_id: number;
    hobby: string;
    description: string;
}

export default defineComponent({
    components: {
        AddHobby,
    },
    setup() {
        const mainStore = useMainStore();
        const userHobbies = ref<Hobby[]>([]);
        const isAddHobbyModalVisible = ref(false);

        // Fetch user hobbies
        const fetchUserHobbies = async () => {
            await mainStore.fetchData();
            userHobbies.value = mainStore.userHobbies as Hobby[];
        }
        onMounted(fetchUserHobbies);

        // Show Add Hobby Modal
        const showAddHobbyModal = () => {
            isAddHobbyModalVisible.value = true;
            console.log('Add Hobby Modal is visible:', isAddHobbyModalVisible.value);
        }
        return {
            userHobbies,
            isAddHobbyModalVisible,
            showAddHobbyModal,
            fetchUserHobbies
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