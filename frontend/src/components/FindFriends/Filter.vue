<template>
    <div class="filter-card d-flex flex-row gap-3 p-2 align-items-center">
        <h5 class="card-title">Filter New Friends</h5>
        <!-- Input age ranges -->
        <div class="form-group d-flex flex-row align-items-center gap-2">
            <label for="ageFrom">From:</label>
            <input type="number" id="ageFrom" class="form-control" v-model="ageFrom" placeholder="Age from">
            <label for="ageTo">To:</label>
            <input type="number" id="ageTo" class="form-control" v-model="ageTo" placeholder="Age to">
        </div>
        <!-- Filter confirm button-->
        <button class="btn btn-primary" @click="filter">Filter</button>
    </div>
    <div v-if="errorMessage" class="alert alert-danger mt-2">{{ errorMessage }}</div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
    emits: ['filter'],
    setup(_, { emit }) {
        const ageFrom = ref<number>(0);
        const ageTo = ref<number>(999);
        const errorMessage = ref<string>('');

        const filter = (): void => {
            // error messages
            if (isNaN(ageFrom.value) || isNaN(ageTo.value)) {
                errorMessage.value = 'Please fill in both age fields with valid numbers.';
                return;
            }
            if (isNaN(Number(ageFrom.value)) || isNaN(Number(ageTo.value))) {
                errorMessage.value = 'Please enter valid numbers.';
                return;
            }
            if (Number(ageFrom.value) > Number(ageTo.value)) {
                errorMessage.value = 'Age from must be less than age to.';
                return;
            }
            errorMessage.value = ''; // Clear any previous error message
            console.log('Age from:', ageFrom.value);
            console.log('Age to:', ageTo.value);
            emit('filter', { ageFrom: ageFrom.value, ageTo: ageTo.value });
        };

        return {
            ageFrom,
            ageTo,
            errorMessage,
            filter,
        };
    },
});
</script>

<style scoped>
.filter-card {
    background-color: #fce26d;
    border-radius: 0.25rem;
}

.card-title {
    margin-left: 0.5rem;
}

.form-control {
    width: 7rem;
    margin: 0.5rem 0;
    padding: 0.5rem;
    border: 0.0625rem solid #ccc;
    border-radius: 0.25rem;
}

.btn-primary,
.btn-primary:hover {
    background-color: #8DE2CD;
    color: black;
    border: none;
    border-radius: 0.5rem;
    padding: 0.5rem 1rem;
    cursor: pointer;
}

.btn-primary:hover {
    font-weight: bold;
}
</style>