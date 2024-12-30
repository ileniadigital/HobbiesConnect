<template>
    <footer class="footer">
        <div class="footer-left brand">
            HobbiesConnect
        </div>
        <div class="footer-center">
            &copy; 2024-25 Amy Anigboro, Mariam Thabti, Sai Sandeep Vemula, Ilenia Maietta
        </div>
    </footer>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
    name: 'Footer',
});
</script>

<style scoped>
.footer {
    display: flex;
    justify-content: space-between;
    padding: 1rem;
    background-color: #8DE2CD;
}

.footer-left {
    flex: 1;
    text-align: left;
}

.footer-center {
    flex: 1;
    text-align: center;
}

.brand {
    font-weight: bold;
    font-size: 1.25rem;
}
</style>