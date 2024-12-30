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
import { defineComponent } from "vue";
import { RouterView } from "vue-router";
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";

export default defineComponent({
    components: { RouterView, Header, Footer },
});

</script>
<style scoped></style>
