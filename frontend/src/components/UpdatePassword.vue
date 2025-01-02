<template>
  <div class="main">
    <button class="btn btn-primary updatepassword" v-if="!showForm" @click="toggleForm">Update Password</button>
    
    <div v-else>
      <form @submit.prevent="updatePassword" class="d-flex flex-column">
        <div class="d-flex flex-column align-items-end">
          <div>
            <label for="currentPassword">Current Password:</label>
            <input type="password" id="currentPassword" v-model="currentPassword" required>
          </div>
          <div>
            <label for="newPassword">New Password:</label>
            <input type="password" id="newPassword" v-model="newPassword" required>
          </div>
          <div>
            <label for="confirmNewPassword">Confirm New Password:</label>
            <input type="password" id="confirmNewPassword" v-model="confirmNewPassword" required>
          </div>
        </div>
        <div class="formaction d-inline-flex gap-1 d-flex justify-content-center">
          <button class="btn confirm p-2" type="submit">Confirm</button>
          <button class="btn cancel p-2" type="button" @click="cancelUpdate">Cancel</button>
        </div>
      </form>
    </div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      showForm: false,
      currentPassword: '',
      newPassword: '',
      confirmNewPassword: '',
    };
  },
  methods: {
    toggleForm() {
      this.showForm = !this.showForm;
    },
    updatePassword() {
      // Poor validation but you get the idea 
      if (this.newPassword !== this.confirmNewPassword) {
        this.message = 'New passwords do not match';
        alert('New passwords do not match');
        return;
      }

      alert('Password updated successfully');
      this.resetForm();
    },
    cancelUpdate() {
      this.resetForm();
      this.showForm = false;
    },
    resetForm() {
      this.currentPassword = '';
      this.newPassword = '';
      this.confirmNewPassword = '';
      this.showForm = false;
    }
  }
};
</script>

<style scoped>
.btn,
.btn:active,
.btn:hover {
    padding: 0.5rem 1rem;
    background-color: #FCE26D;
    border: none;
    color: black;
}

.btn:hover {
    font-weight: bold;
}

.btn.cancel {
    background-color: #ca3f3f;
    color: white
}
.btn.confirm {
    background-color: #1e823a;
    color: white;
}

.formaction {
    margin-top: 1rem;
}

form>div {
    float: right;
}

form {
    margin-top: 1rem;
    border: 1px solid grey;
    border-radius: 0.5rem;
    border-color: grey;
    padding: 1rem;
    width: fit-content;
    height:fit-content;
}


</style>