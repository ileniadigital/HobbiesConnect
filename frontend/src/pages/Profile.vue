<template>
  <div>
    <div class="h1">{{ title }}</div>
    <hr>
    <div class="h3">Hi, {{ name }}</div>

    <!-- Profile Form -->
    <div class="row">
      <!-- <div class="col-md-12"> -->
        <form @submit.prevent="updateUserProfile"> <!--   ADD BACK ONCE CHANGED TO AJAX-->
          <div class="form-row">
            <div class="form-group col-md-4">
              <label for="dob">Date of Birth:</label>
              <input type="date" v-model="dateofbirth" id="dob" />
            </div>
            <div class="form-group col-md-4">
              <label for="name">Name</label>
              <input type="text" v-model="name" id="name" />
            </div>
            <div class="form-group col-md-4">
              <label for="email">Email</label>
              <input type="email" v-model="email" id="email" />
            </div>
            <button type="submit" class="btn btn-primary">Update Profile</button>
          </div>
        </form>
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

export default defineComponent({
  components: {
    HobbyList,
    UpdatePassword,
  },
  data() {
    return {
      title: "Profile",
      name: "",
      email: "",
      dateofbirth: "",
      userId: 1, // temporary 
    };
  },
  methods: {
    fetchUserProfile() {
      const xhreq = new XMLHttpRequest();
      xhreq.open("GET", `/api/users/${this.userId}/`, true);
      xhreq.onload = () => {
        if (xhreq.status === 200) {
          const user = JSON.parse(xhreq.responseText);
          this.name = user.first_name + " " + user.last_name;
          this.email = user.email;
          this.dateofbirth = user.dob;
        } else {
          console.error("Error fetching user profile:", xhreq.statusText);
        }
      };
      xhreq.onerror = () => {
        console.error("Network error while fetching user profile.");
      };
      xhreq.send();
    },
    updateUserProfile() {
      const xhreq = new XMLHttpRequest();
      xhreq.open("PUT", `/api/users/${this.userId}/`, true);
      xhreq.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
      xhreq.onload = () => {
        if (xhreq.status === 200) {
          alert("Profile updated successfully!");
        } else {
          console.error("Error updating profile:", xhreq.statusText);
          alert("Failed to update profile.");
        }
      };
      xhreq.onerror = () => {
        console.error("Network error while updating profile.");
        alert("Failed to update profile.");
      };
      const [firstName, ...lastNameParts] = this.name.split(" ");
      const lastName = lastNameParts.join(" ");
      const data = JSON.stringify({
        first_name: firstName,
        last_name: lastName,
        email: this.email,
        dob: this.dateofbirth,
      });
      xhreq.send(data);
    },
  },
  mounted() {
    this.fetchUserProfile();
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
