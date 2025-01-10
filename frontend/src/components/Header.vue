<template>
    <nav class="navbar navbar-expand-lg custom-navbar">
        <div class="container-fluid">
            <router-link class="navbar-brand" to="/">HobbiesConnect</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
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
                <a v-else class="btn" href="http://127.0.0.1:8000/login">Login</a>

            </div>
        </div>
    </nav>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'Header',
  data() {
    return {
      isAuthenticated: false,
      userEmail: null
    };
},
created() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/authenticated', true);
    xhr.onload = () => {
        if (xhr.status >= 200 && xhr.status < 300) {
            if (xhr.getResponseHeader('Content-Type')?.includes('application/json')) {
                const response = JSON.parse(xhr.responseText);
                this.isAuthenticated = response.isAuthenticated;
                this.userEmail = response.email;
            } else {
                this.isAuthenticated = false;
                this.userEmail = null;
            }
        } else {
            this.isAuthenticated = false;
            this.userEmail = null;
        }
    };
    xhr.onerror = () => {
        this.isAuthenticated = false;
        this.userEmail = null;
    };
    xhr.send();
},
methods: {
    logout() {
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/api/logout', true);
        xhr.onload = () => {
            if (xhr.status >= 200 && xhr.status < 300) {
                this.isAuthenticated = false;
                window.location.href = 'http://127.0.0.1:8000/login';  // Redirect to Django login page
            }
        };
        xhr.send();
    }
}
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