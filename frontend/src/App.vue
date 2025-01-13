<template>
    <Header></Header>
    <main class="container pt-4">
        <!-- <div>
            <router-link
                class=""
                :to="{name: 'Main Page'}"
            >
                Home
            </router-link>
            |
            <router-link
                class=""
                :to="{name: 'Other Page'}"
            >
                Profile
            </router-link>
        </div> -->
        <RouterView class="flex-shrink-0" />
    </main>
    <Footer></Footer>
</template>

<script lang="ts">
import { defineComponent, onMounted } from "vue";
import { RouterView, useRouter } from "vue-router";
import { useMainStore } from "./data/data";
import { useAuthStore } from "./utils/auth";

import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";

export default defineComponent({
    components: { RouterView, Header, Footer },
    setup() {
        const mainStore = useMainStore();
        const authStore = useAuthStore();
        const router = useRouter();

        onMounted(async () => {
            const isAuthenticated = await authStore.isAuthenticated;
            console.log(isAuthenticated);
            if (!isAuthenticated) {
                window.alert("You are not authenticated. Please log in.");
                window.location.href = ('http://127.0.0.1:8000/login');
            } else {
                mainStore.fetchData();
            }
        });

        // onMounted(async () => {
        //     // Delay authentication check slightly to ensure cookies are set
        //     setTimeout(async () => {
        //         await authStore.checkAuthentication();
        //         const isAuthenticated = authStore.get_authenticated;
        //         console.log(isAuthenticated);
        //         if (!isAuthenticated) {
        //             window.location.href = ('http://127.0.0.1:8000/login');
        //         }
        //     }, 100);
        // });

        return {
            user: mainStore.user,
            hobbies: mainStore.hobbies,
            userHobbies: mainStore.userHobbies,
            friends: mainStore.friends,
        };
    }
});

</script>
<style scoped></style>