<template>
    <div v-if="visible" class="modal fade show" tabindex="-1" style="display: block;" aria-modal="true" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Add Hobby</h5>
                    <button type="button" class="btn-close" @click="close" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form @submit.prevent="addHobby">
                        <div class="mb-3">
                            <label for="hobby" class="form-label">Hobby:</label>
                            <input type="text" id="hobby" v-model="hobby" class="form-control" required />
                        </div>
                        <div class="mb-3">
                            <label for="description" class="form-label">Description:</label>
                            <input type="text" id="description" v-model="description" class="form-control" required />
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" @click="close">Close</button>
                            <button type="submit" class="btn btn-primary">Add Hobby</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
    props: {
        visible: {
            type: Boolean,
            required: true
        }
    },
    emits: ["close", "hobby-added"],
    setup(props, { emit }) {
        const hobby = ref("");
        const description = ref("");

        const close = () => {
            emit("close");
        };

        const addHobby = () => {
            // Simulate adding a hobby
            console.log("Hobby added:", hobby.value, description.value);
            emit("hobby-added");
            close();
        };

        return {
            hobby,
            description,
            close,
            addHobby
        };
    }
});
</script>

<style scoped>
.modal-content {
    padding: 1.25rem;
}

.btn-primary,
.btn-primary:hover,
.btn-primary:active {
    background-color: #FCE26D;
    border: none;
    color: black;

}

.btn-primary:hover,
.btn-primary:active {
    font-weight: bold;
}
</style>
