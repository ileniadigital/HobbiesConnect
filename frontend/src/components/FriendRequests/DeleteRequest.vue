<template>
    <div v-if="visible" class="modal fade show" tabindex="-1" style="display: block;" aria-modal="true" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="deleteRequestModalLabel">Confirm Action</h5>
                    <button type="button" class="btn-close" @click="close" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <p v-if="status === 'ACCEPTED'">Are you sure you want to delete this friend?</p>
                    <p v-else-if="status === 'PENDING'">Are you sure you want to remove this request?</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" @click="close">Cancel</button>
                    <button type="button" class="btn btn-danger" @click="deleteRequest">Delete</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
    props: {
        visible: {
            type: Boolean,
            required: true
        },
        userId: {
            type: Number,
            required: true
        },
        friendId: {
            type: Number,
            required: true
        },
        status: {
            type: String,
            required: true
        }
    },
    emits: ["close", "request-deleted"],
    methods: {
        close(): void {
            this.$emit("close");
        },
        deleteRequest(): void {
            this.$emit("request-deleted", { userId: this.userId, friendId: this.friendId });
        }
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

.btn-danger {
    background-color: #ca3f3f;
    color: white;
}

.btn-secondary {
    background-color: #6c757d;
    color: white;
}
</style>