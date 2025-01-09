<template>
    <div>
        <button class="btn btn-primary updatepassword" @click="openModal">Update Password</button>

        <!-- Modal -->
        <div v-if="visible" class="modal fade show" tabindex="-1" style="display: block;" aria-modal="true" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Update Password</h5>
                <button type="button" class="btn-close" @click="closeModal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form @submit.prevent="updatePassword" class="d-flex flex-column">
                <div class="d-flex flex-column align-items-end">
                    <div>
                    <label for="currentPassword">Current Password:</label>
                    <input type="password" id="currentPassword" v-model="currentPassword" required>
                    </div>
                    <div>
                    <label for="newPassword">New Password:</label>
                    <input type="password" id="newPassword" v-model="newPassword" required>
                    </div>
                    <div>
                    <label for="confirmNewPassword">Confirm New Password:</label>
                    <input type="password" id="confirmNewPassword" v-model="confirmNewPassword" required>
                    </div>
                </div>
                <div class="formaction d-inline-flex gap-1 d-flex justify-content-center">
                    <button class="btn confirm p-2" type="submit">Confirm</button>
                    <button class="btn cancel p-2" type="button" @click="closeModal">Cancel</button>
                </div>
                <div v-if="message" class="alert alert-danger mt-2">{{ message }}</div>
                </form>
            </div>
            </div>
        </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useMainStore } from "../../data/data";

export default defineComponent({
    setup() {
        const mainStore = useMainStore();
        const visible = ref(false);
        const currentPassword = ref("");
        const newPassword = ref("");
        const confirmNewPassword = ref("");
        const message = ref<string | null>(null);
        const userId = mainStore.userId;

        const openModal = () => {
            visible.value = true;
        };

        const closeModal = () => {
            visible.value = false;
            message.value = null;
            currentPassword.value = "";
            newPassword.value = "";
            confirmNewPassword.value = "";
        };

        const updatePassword = async () => {
            if (newPassword.value !== confirmNewPassword.value) {
                message.value = "New passwords do not match.";
                return;
            }
            console.log(`http://127.0.0.1:8000/api/user/update_password/${userId}/`);
            console.log("Current Password:", currentPassword.value);
            console.log("New Password:", newPassword.value);
            try {
                const response = await fetch(`http://127.0.0.1:8000/api/user/update_password/${userId}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    current_password: currentPassword.value,
                    new_password: newPassword.value,
                }),
                });
                if (!response.ok) {
                const errorData = await response.json();
                message.value = errorData.message || 'Failed to update password';
                return;
                }
                message.value = "Password updated successfully!";
                closeModal();
            } catch (error) {
                if (error instanceof Error) {
                console.error("Error updating profile:", error.message);
                message.value = error.message;
                } else {
                console.error("Error updating profile:", String(error));
                message.value = String(error);
                }
            }
        };

        return {
            visible,
            currentPassword,
            newPassword,
            confirmNewPassword,
            message,
            openModal,
            closeModal,
            updatePassword,
        };
    },
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

.formaction{
    margin-top: 1rem;
}

.confirm{
    background-color: #2c8713;
    color: black;
}

.cancel{
    background-color: #ff0000;
    color: black;
}
.confirm:hover, .cancel:hover{
    border-color: black;
    font-weight: bold;
}
</style>