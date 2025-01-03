<template>
    <div class="card" style="width: 18rem;">
        <div class="card-body">
            <h5 class="card-title">{{ name }}</h5>
            <h6 class="card-subtitle mb-2 text-body-secondary">Status: {{ status }}</h6>
            <p class="card-text">Friend since: {{ new Date(createdAt).toLocaleDateString() }}</p>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";

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
.card {
    margin-bottom: 1rem;
}
</style>