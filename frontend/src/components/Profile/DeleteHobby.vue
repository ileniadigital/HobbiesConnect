<template>
    <div v-if="visible" class="modal fade show" tabindex="-1" style="display: block;" aria-modal="true" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="deleteHobbyModalLabel">Confirm Delete</h5>
                    <button type="button" class="btn-close" @click="close" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    Are you sure you want to delete this hobby?
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" @click="close">Cancel</button>
                    <button type="button" class="btn btn-danger" id="deleteHobby-button"@click="confirmDelete">Delete</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { getCsrfToken } from '../../utils/csrf';
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
        hobbyId: {
            type: Number,
            required: true
        }
    },
    emits: ["close", "hobby-deleted"],
    methods: {
        close() {
            this.$emit("close");
        },
        async confirmDelete(): Promise<void> {
            // console.log("User id in delete:", this.userId);
            // console.log("Hobby id in delete:", this.hobbyId);
            try {
                const response = await fetch('/api/user_hobbies/delete/', {
                    credentials: 'include',
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCsrfToken() || '',
                    },
                    body: JSON.stringify({
                        user_id: this.userId,
                        hobby_id: this.hobbyId
                    })
                });
                if (!response.ok) {
                    throw new Error('Something went wrong');
                }
                // const data = await response.json();
                // console.log("Hobby deleted:", data);
                this.$emit('hobby-deleted');
                this.close();
            } catch (error) {
                console.error('There was a problem with the fetch operation:', error);
            }
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