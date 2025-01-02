<template>
    <h2>Hobbies</h2>
    <ul class="list-group">
        <li class="list-group-item">An item</li>
        <li class="list-group-item">A second item</li>
        <li class="list-group-item">A third item</li>
        <li class="list-group-item">A fourth item</li>
        <li class="list-group-item">And a fifth one</li>
    </ul>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
    data() {
        return {
            hobbies: [
                { name: "Reading" },
                { name: "Swimming" },
                { name: "Coding" }
            ],
        }
    }
})
</script>

<style scoped></style>