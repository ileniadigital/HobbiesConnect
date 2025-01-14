<template>
  <div>
    <!-- Profile Form -->
    <div class="row">
      <form @submit.prevent="updateUserProfile" class="col-md-12">
        <div class="form-row">
          <div class="form-group col-md-6 d-flex align-items-center">
            <label for="dob" class="col-form-label col-md-6">Date of Birth</label>
            <div class="col-md-8">
              <input type="date" v-model="dob" id="dob" class="form-control" />
            </div>
          </div>
          <div class="form-group col-md-6 d-flex align-items-center">
            <label for="first_name" class="col-form-label col-md-6">First Name</label>
            <div class="col-md-8">
              <input type="text" v-model="first_name" id="first_name" class="form-control" />
            </div>
          </div>
          <div class="form-group col-md-6 d-flex align-items-center">
            <label for="last_name" class="col-form-label col-md-6">Last Name</label>
            <div class="col-md-8">
              <input type="text" v-model="last_name" id="last_name" class="form-control" />
            </div>
          </div>
          <div class="form-group col-md-6 d-flex align-items-center">
            <label for="email" class="col-form-label col-md-6">Email</label>
            <div class="col-md-8">
              <input type="email" v-model="email" id="email" class="form-control" />
            </div>
          </div>
          <div class="form-group col-md-12 mt-4">
            <button type="submit" class="btn btn-primary">Update Profile</button>
          </div>
        </div>
      </form>
      <div v-if="errorMessage" class="alert alert-danger mt-3">{{ errorMessage }}</div>
      <div v-if="confirmationMessage" class="alert alert-success mt-3">{{ confirmationMessage }}</div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import { useMainStore } from "../../data/data";
import { getCsrfToken } from "../../utils/csrf";

export default defineComponent({
  setup() {
    const mainStore = useMainStore();
    const title = ref<string>("Profile");
    const first_name = ref<string>("");
    const last_name = ref<string>("");
    const email = ref<string>("");
    const dob = ref<string>("");
    const userId = ref<number>(1); // temporary
    const errorMessage = ref<string>("");
    const confirmationMessage = ref<string>("");

    onMounted(async (): Promise<void> => {
      await mainStore.fetchData();
      if (mainStore.user) {
        first_name.value = mainStore.user.first_name || "No name";
        last_name.value = mainStore.user.last_name || "No name";
        email.value = mainStore.user.email || "No email";
        dob.value = mainStore.user.dob || "No date of birth";
        userId.value = mainStore.user.id || 1;
      }
    });

    const updateUserProfile = async (): Promise<void> => {
      try {
        const updated = JSON.stringify({
          first_name: first_name.value,
          last_name: last_name.value,
          email: email.value,
          dob: dob.value,
        });
        // console.log("Sending updated data:", updated);
        const response = await fetch(`http://localhost:8000/api/user/update/${mainStore.userId}/`, {
          credentials: "include",
          method: "PUT",
          headers: {
            "Content-Type": "application/json;charset=UTF-8",
            "X-CSRFToken": getCsrfToken() || "",
          },
          body: updated,
        });
        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.error || `Error updating profile: ${response.statusText}`);
        }
        confirmationMessage.value = "Profile updated successfully";
        errorMessage.value = ""; // Clear any previous error messages

      } catch (error) {
        console.error("Error updating profile:", error);
        if (error instanceof Error) {
          errorMessage.value = error.message;
          confirmationMessage.value = "";
        } else {
          errorMessage.value = String(error);
        }
      }
    };

    return {
      title,
      first_name,
      last_name,
      email,
      dob,
      userId,
      mainStore,
      errorMessage,
      confirmationMessage,
      updateUserProfile,
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