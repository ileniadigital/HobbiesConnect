<template>
    <div class="card" style="width: 24rem;">
        <div class="card-body d-flex justify-content-between align-items-center">
            <div>
                <h5 class="card-title">{{ name }}</h5>
                <h6 class="card-subtitle mb-2 text-body-secondary">Status: {{ status }}</h6>
                <p class="card-text">Friend since: {{ new Date(createdAt).toLocaleDateString() }}</p>
            </div>
            <button v-if="status === 'PENDING'" class="btn btn-primary btn-sm"
                @click="$emit('accept-request')">Accept</button>
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

.btn-primary,
.btn-primary:hover,
.btn-primary:hover:active {
    background-color: #FCE26D;
    color: #000000;
    border: none;
}

.btn:hover {
    font-weight: bold;
}

.btn-primary:hover:active {
    background-color: #8DE2CD;
}
</style>