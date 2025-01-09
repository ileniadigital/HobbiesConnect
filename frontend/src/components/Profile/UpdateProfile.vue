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
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import { useMainStore } from "../../data/data";

export default defineComponent({
  components: {
  },
  setup() {
    const mainStore = useMainStore();
    const title = ref("Profile");
    const first_name = ref("");
    const last_name = ref("");
    const email = ref("");
    const dob = ref("");
    const userId = ref(1); // temporary

    onMounted(async () => {
      await mainStore.fetchData();
      if (mainStore.user) {
        first_name.value = mainStore.user.first_name || "No name";
        last_name.value = mainStore.user.last_name || "No name";
        email.value = mainStore.user.email || "No email";
        dob.value = mainStore.user.dob || "No date of birth";
        userId.value = mainStore.user.id || 1;
      }
    });

    return {
      title,
      first_name,
      last_name,
      email,
      dob,
      userId,
      mainStore,
    };
  },
  methods: {
    async updateUserProfile() {
      try {
        const apiURL = `http://127.0.0.1:8000/api/user/update/${this.userId}/`;
        console.log("Updating profile with URL:", apiURL);
        const updated = JSON.stringify({
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email,
          dob: this.dob,
        });
        console.log("Sending updated data:", updated);
        const response = await fetch(apiURL, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json;charset=UTF-8",
          },
          body: updated,
        });
        if (!response.ok) {
          throw new Error(`Error updating profile: ${response.statusText}`);
        }
      } catch (error) {
        console.error("Error updating profile:", error);
      }
    },
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