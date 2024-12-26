<template>
    <nav class="navbar navbar-expand-lg custom-navbar">
    <div class="container-fluid">
        <router-link class="navbar-brand" to="/">HobbiesConnect</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
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
                <router-link class="nav-link" to="/other">Find Friends</router-link>
            </li>
            <!-- Friends Request -->
            <li class="nav-item">
                <router-link class="nav-link" to="/other">Friend Requests</router-link>
            </li>
        </ul>
        <button class="btn" @click="logout">Logout</button>
        </div>
    </div>
    </nav>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';

    export default defineComponent({
        name: 'Header',
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
    background-color:#FCE26D;
    color: #000000;
}

.btn:hover {
    font-weight: bold;
}
</style>