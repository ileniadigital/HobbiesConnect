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

import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";

export default defineComponent({
    components: { RouterView, Header, Footer },
    setup() {
        const mainStore = useMainStore();
        const router = useRouter();

        onMounted(async () => {
            const isAuthenticated = await mainStore.checkAuthentication();
            if (!isAuthenticated) {
                window.location.href = ('http://127.0.0.1:8000/login');
            } else {
                mainStore.fetchData();
            }
        });
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
