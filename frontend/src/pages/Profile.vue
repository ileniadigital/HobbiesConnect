<template>
  <div>
    <div class="h3" id="profile-page">{{ title }}</div>
    <hr>
    <!-- <div class="h3">Hi, {{ name }}</div> -->

    <!-- Profile Form -->
    <div class="row">
      <div class="col-md-6">
        <UpdateProfile />
      </div>
      <div class="col-md-6">
        <UpdatePassword />
      </div>
    </div>
    <hr>
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
</script>


<style scoped>
.updatepassword {
  margin: 2rem 0 2rem 0;
}

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
