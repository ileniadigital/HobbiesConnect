<template>
    <div>
        <!-- Password Update Form -->
        <div class="row">
            <form @submit.prevent="updatePassword" class="col-md-12">
                <div class="form-row">
                    <div class="form-group col-md-5 d-flex align-items-center">
                        <label for="current_password" class="col-form-label col-md-4">Current Password</label>
                        <div class="col-md-5">
                            <input type="password" v-model="currentPassword" id="current_password"
                                class="form-control" />
                        </div>
                    </div>
                    <div class="form-group col-md-5 d-flex align-items-center">
                        <label for="new_password" class="col-form-label col-md-4">New Password</label>
                        <div class="col-md-5">
                            <input type="password" v-model="newPassword" id="new_password" class="form-control" />
                        </div>
                    </div>
                    <div class="form-group col-md-12">
                        <button type="submit" class="btn btn-primary">Update Password</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useMainStore } from "../../data/data";

export default defineComponent({
    setup() {
        const mainStore = useMainStore();
        const currentPassword = ref("");
        const newPassword = ref("");

        const updatePassword = async () => {
            try {
                const response = await fetch(`http://127.0.0.1:8000/user/update_password/${mainStore.userId}/`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        current_password: currentPassword.value,
                        new_password: newPassword.value
                    })
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.error || 'Failed to update password');
                }

                const data = await response.json();
                console.log("Password updated:", data);
                alert("Password updated successfully");
            } catch (error) {
                console.error('There was a problem with the fetch operation:', error);
            }
        };

        return {
            currentPassword,
            newPassword,
            updatePassword,
        };
    },
});
</script>

<style scoped>
.form-group {
    margin-bottom: 1rem;
}

.btn-primary {
    background-color: #FCE26D;
    border: none;
    color: black;
}

.btn-primary:hover {
    font-weight: bold;
}
</style>