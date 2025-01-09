<template>
  <div>
    <!-- Profile Form -->
    <div class="row">
      <!-- <div class="col-md-12"> -->
        <form @submit.prevent="updateUserProfile"> <!--   ADD BACK ONCE CHANGED TO AJAX-->
          <div class="form-row">
            <div class="form-group col-md-4">
              <label for="dob">Date of Birth</label>
              <input type="date" v-model="dob" id="dob" />
            </div>
            <div class="form-group col-md-4">
              <label for="first_name">First Name</label>
              <input type="text" v-model="first_name" id="first_name" />
            </div>
            <div class="form-group col-md-4">
              <label for="last_name">Last Name</label>
              <input type="text" v-model="last_name" id="last_name" />
            </div>
            <div class="form-group col-md-4">
              <label for="email">Email</label>
              <input type="email" v-model="email" id="email" />
            </div>
            <button type="submit" class="btn btn-primary" @click="updateUserProfile">Update Profile</button>
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
        alert("Profile updated successfully!");
      } catch (error) {
        console.error("Error updating profile:", error);
      }
    },
  },
});

</script>


<style scoped>
.hobbylist {
  margin: 2rem 0 2rem 0;
}

.btn,
.btn:hover {
  padding: 0.5rem 1rem;
  background-color: #FCE26D;
  border: none;
  color: black;
}

.btn:hover {
  font-weight: bold;
}
</style>
