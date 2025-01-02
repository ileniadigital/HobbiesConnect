<template>
  <div>
    <div class="h1">
      {{ title }}
    </div>
    <hr>
    <div class="h3">
      Hi, {{ name }}
    </div>
  </div>
  <div class="row">
    <div class="col-md-12">
      <form>
        <div class="form-row vertical">
          <div class="form-field">
            <label for="dob">Date of Birth:</label>
            <input type="date" v-model="dateofbirth" id="dob">
          </div>
          <div class="form-field">
            <label for="name">Name</label>
            <input type="text" v-model="name" id="name">
          </div>
          <div class="form-field">
            <label for="email">Email</label>
            <input type="email" v-model="email" id="email">
          </div>
          <button type="submit" class="btn btn-primary" v-on:click="">Update Profile</button>
        </div>

      </form>
    </div>
    <div>
      <button type="button" class="btn btn-primary">Update Password</button>
    </div>
  </div>
  <!-- <div class="container">
    <div class="row">
      <div class="col-md-12">
        <div class="hobbies">
          <form>
            <div class="form-row">
              <div class="form-field">
                <legend>Hobbies</legend>
                <input list="hobbies">
                <button type="submit" class="btn btn-primary">Add</button>
                <datalist id="hobbies">
                  <option v-for="hobby in hobbies" :key="hobby.name">
                    {{ hobby.name }}
                  </option>
                </datalist>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div> -->
  <HobbyList />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import HobbyList from "../components/HobbyList.vue";

export default defineComponent({
  components: {
    HobbyList,
  },
  data() {
    return {
      title: "Profile",
      username: "Amy123",
      hobbies: [
        { name: "Reading" },
        { name: "Swimming" },
        { name: "Coding" }
      ],
    }
  }
})
</script>

<style scoped></style>
