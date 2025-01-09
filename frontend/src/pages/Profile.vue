<template>
  <div>
    <div class="h3">{{ title }}</div>
    <hr>
    <!-- <div class="h3">Hi, {{ name }}</div> -->

    <!-- Profile Form -->
    <div class="row">
      <!-- <div class="col-md-12"> -->
        <UpdateProfile />
      <!-- </div> -->
    </div>
    <!-- Update Password -->
    <div class="updatepassword">
      <UpdatePassword />
    </div>

    <!-- List of Hobbies -->
    <div class="hobbylist">
      <HobbyList />
    </div>
  </div>
</template>


<script lang="ts">
import { defineComponent } from "vue";
import HobbyList from "../components/Profile/HobbyList.vue";
import UpdatePassword from "../components/Profile/UpdatePassword.vue";
import UpdateProfile from "../components/Profile/UpdateProfile.vue";

export default defineComponent({
  components: {
    HobbyList,
    UpdatePassword,
    UpdateProfile,
  },
  data() {
    return {
      title: "Profile",
    };
  },
});
// methods: {
//   async fetchUserProfile() {
//     try {
//       const response = await axios.get(`/api/users/${this.userId}/`);
//       const user = response.data;
//       this.name = user.first_name + " " + user.last_name;
//       this.email = user.email;
//       this.dateofbirth = user.dob;
//     } catch (error) {
//       console.error("Error fetching user profile:", error);
//     }
//   },
//   async updateUserProfile() {
//     try {
//       const [firstName, ...lastNameParts] = this.name.split(" ");
//       const lastName = lastNameParts.join(" ");
//       const data = {
//         first_name: firstName,
//         last_name: lastName,
//         email: this.email,
//         dob: this.dateofbirth,
//       };
//       await axios.put(`/api/users/${this.userId}/`, data);
//       alert("Profile updated successfully!");
//     } catch (error) {
//       console.error("Error updating profile:", error);
//       alert("Failed to update profile.");
//     }
//   },
// },
// mounted() {
//   this.fetchUserProfile();
// },
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
