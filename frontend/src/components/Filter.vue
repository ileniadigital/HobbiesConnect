<template>
    <div class="filter-card d-flex flex-row gap-3 p-2 align-items-center">
        <h5 class="card-title">Filter New Friends</h5>
        <!-- Input age ranges -->
        <div class="form-group d-flex flex-row align-items-center gap-2">
            <label for="ageFrom">From:</label>
            <input type="text" id="ageFrom" class="form-control" v-model="ageFrom" placeholder="Age from">
            <label for="ageTo">To:</label>
            <input type="text" id="ageTo" class="form-control" v-model="ageTo" placeholder="Age to">
        </div>
        <!-- Filter confirm button-->
        <button class="btn btn-primary" @click="filter">Filter</button>
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
    data() {
        return {
            ageFrom: '',
            ageTo: ''
        };
    },
    methods: {
        filter() {
            console.log('Age from:', this.ageFrom);
            console.log('Age to:', this.ageTo);
        }
    }
})
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