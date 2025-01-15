<template>
  <nav class="navbar navbar-expand-lg custom-navbar">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">HobbiesConnect</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <!-- Profile link -->
          <li class="nav-item">
            <router-link class="nav-link active" aria-current="page" to="/">Profile</router-link>
          </li>
          <!-- Find friends link -->
          <li class="nav-item">
            <router-link class="nav-link" to="/findfriends">Find Friends</router-link>
          </li>
          <!-- Friends Request -->
          <li class="nav-item">
            <router-link class="nav-link" to="/friendrequests">Friend Requests</router-link>
          </li>
        </ul>
        <!-- Login/logout button depending -->
        <button v-if="isAuthenticated" class="btn" @click="logout">Logout</button>
        <button v-else class="btn" @click="redirectToLogin">Login</button>
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useAuthStore } from '../utils/auth';
import { getCsrfToken } from '../utils/csrf';

export default defineComponent({
  name: 'Header',
  setup() {
    const authStore = useAuthStore();

    const redirectToLogin = (): void => {
      authStore.checkAuthentication();
    };
    const logout = async (): Promise<void> => {
      try {
        console.log('Logging out');
        const response = await fetch('/api/logout/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken() || '',
          },
          credentials: 'include',
        });
        if (response.ok) {
          redirectToLogin();
        } else {
          console.error('Logout failed');
        }
      } catch (error) {
        console.error('Error during logout:', error);
      }
    };


    const isAuthenticated = ref(false);

    authStore.checkAuthentication().then((result) => {
      isAuthenticated.value = result;
    });

    return {
      isAuthenticated,
      logout,
      redirectToLogin,
    };
  },
});
</script>

<style scoped>
.custom-navbar {
  background-color: #8DE2CD;
}

.navbar-brand {
  font-weight: bold;
}

.btn {
  background-color: #FCE26D;
  color: #000000;
}

.btn:hover {
  font-weight: bold;
}
</style>