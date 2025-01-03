<template>
    <div class="card" style="width: 18rem;">
        <div class="card-body d-flex justify-content-between align-items-center">
            <div>
                <h5 class="card-title">{{ name }}</h5>
                <h6 class="card-subtitle mb-2 text-body-secondary">Status: {{ status }}</h6>
                <p class="card-text">Friend since: {{ new Date(createdAt).toLocaleDateString() }}</p>
            </div>
            <button class="btn btn-danger btn-sm" @click="$emit('delete-request')">Delete</button>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
    name: "Request",
    props: {
        name: {
            type: String,
            required: true
        },
        status: {
            type: String,
            required: true
        },
        createdAt: {
            type: String,
            required: true
        }
    }
});
</script>

<style scoped>
.card-body {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.btn-danger,
.btn-danger:hover {
    margin-left: 1rem;
}

.btn-danger:hover,
.btn-danger:active {
    font-weight: bold;
}
</style>