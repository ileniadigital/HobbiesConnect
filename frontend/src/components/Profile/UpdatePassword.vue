<template>
    <div>
        <!-- Password Update Form -->
        <div class="row">
            <form @submit.prevent="updatePassword" class="col-md-12">
                <div class="form-row">
                    <div class="form-group col-md-8 d-flex align-items-center">
                        <label for="current_password" class="col-form-label col-md-4">Current Password</label>
                        <div class="col-md-8">
                            <input type="password" v-model="currentPassword" id="current_password"
                                class="form-control" />
                        </div>
                    </div>
                    <div class="form-group col-md-8 d-flex align-items-center">
                        <label for="new_password" class="col-form-label col-md-4">New Password</label>
                        <div class="col-md-8">
                            <input type="password" v-model="newPassword" id="new_password" class="form-control" />
                        </div>
                    </div>
                    <div class="form-group col-md-12 mt-4">
                        <button type="submit" class="btn btn-primary">Update Password</button>
                    </div>
                </div>
            </form>
            <div v-if="errorMessage" class="alert alert-danger mt-3">{{ errorMessage }}</div>
            <div v-if="confirmationMessage" class="alert alert-success mt-3">{{ confirmationMessage }}</div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useMainStore } from "../../data/data";
import { useAuthStore } from "../../utils/auth";
import { getCsrfToken } from "../../utils/csrf";

export default defineComponent({
    setup() {
        const mainStore = useMainStore();
        const authStore = useAuthStore();
        const currentPassword = ref<string>("");
        const newPassword = ref<string>("");
        const errorMessage = ref<string>("");
        const confirmationMessage = ref<string>("");

        const updatePassword = async (): Promise<void> => {
            try {
                const response = await fetch(`/user/update_password/${mainStore.userId}/`, {
                    credentials: 'include',
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCsrfToken() || '',
                    },
                    body: JSON.stringify({
                        current_password: currentPassword.value,
                        new_password: newPassword.value
                    })
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.error || 'Failed to update password');
                } else {
                    confirmationMessage.value = "Password updated successfully";
                }

                // const data = await response.json();
                // console.log("Password updated:", data);
                errorMessage.value = "";

                // Clear the form
                currentPassword.value = "";
                newPassword.value = "";

                await authStore.checkAuthentication();
            } catch (error: any) {
                console.error('There was a problem with the fetch operation:', error);
                errorMessage.value = error.message;
                confirmationMessage.value = "";
            }
        };

        return {
            currentPassword,
            newPassword,
            updatePassword,
            errorMessage,
            confirmationMessage
        };
    },
});
</script>

<style scoped>
.form-group {
    margin-bottom: 1rem;
}

.btn-primary,
.btn-primary:hover,
.btn-primary:hover:active {
    background-color: #FCE26D;
    border: none;
    color: black;
}

.btn-primary:hover {
    font-weight: bold;
}
</style>