<template>
    <div class="head">
        <h2>Hobbies</h2>
        <button class="btn btn-primary" @click="addHobby">Add Hobby</button>
    </div>
    <!-- Hobbies list -->
    <ul class="list-group">
        <li class="list-group-item" v-for="uHobby in userHobbies" :key="uHobby.hobby_id">
            {{ uHobby.hobby }}
        </li>
        <li v-if="userHobbies.length === 0" class="list-group-item">No hobbies found.</li>
    </ul>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import { useMainStore } from "../data/data";

interface Hobby {
    hobby_id: number;
    hobby: string;
    description: string;
}

export default defineComponent({
    setup() {
        const mainStore = useMainStore();
        const userHobbies = ref<Hobby[]>([]);

        onMounted(async () => {
            await mainStore.fetchData();
            userHobbies.value = mainStore.userHobbies as Hobby[];
        });

        return {
            userHobbies,
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

.btn {
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