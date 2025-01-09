<template>
  <div>
    <!-- Profile Form -->
    <div class="row">
      <form @submit.prevent="updateUserProfile" class="col-md-12">
        <div class="form-row">
          <div class="form-group col-md-4 d-flex align-items-center">
            <label for="dob" class="col-form-label col-md-4">Date of Birth</label>
            <div class="col-md-8">
              <input type="date" v-model="dob" id="dob" class="form-control" />
            </div>
          </div>
          <div class="form-group col-md-4 d-flex align-items-center">
            <label for="first_name" class="col-form-label col-md-4">First Name</label>
            <div class="col-md-8">
              <input type="text" v-model="first_name" id="first_name" class="form-control" />
            </div>
          </div>
          <div class="form-group col-md-4 d-flex align-items-center">
            <label for="last_name" class="col-form-label col-md-4">Last Name</label>
            <div class="col-md-8">
              <input type="text" v-model="last_name" id="last_name" class="form-control" />
            </div>
          </div>
          <div class="form-group col-md-4 d-flex align-items-center">
            <label for="email" class="col-form-label col-md-4">Email</label>
            <div class="col-md-8">
              <input type="email" v-model="email" id="email" class="form-control" />
            </div>
          </div>
          <div class="form-group col-md-12">
            <button type="submit" class="btn btn-primary">Update Profile</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import { useMainStore } from "../../data/data";

export default defineComponent({
  setup() {
    const mainStore = useMainStore();
    const dob = ref("");
    const first_name = ref("");
    const last_name = ref("");
    const email = ref("");
    const userId = mainStore.userId;

    onMounted(async () => {
      await mainStore.fetchData();
      if (mainStore.user) {
        dob.value = mainStore.user?.dob || "";
        first_name.value = mainStore.user?.first_name || "";
        last_name.value = mainStore.user?.last_name || "";
        email.value = mainStore.user?.email || "";
      }
    });

    const updateUserProfile = async () => {
      // Your update logic here
    };

    return {
      dob,
      first_name,
      last_name,
      email,
      updateUserProfile,
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