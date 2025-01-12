<template>
    <nav aria-label="Page navigation example">
        <ul class="pagination">
            <li class="page-item" :class="{ disabled: currentPage === 1 }">
                <a class="page-link" href="#" @click.prevent="changePage(currentPage - 1)">Previous</a>
            </li>
            <li class="page-item" v-for="page in totalPages" :key="page" :class="{ active: currentPage === page }">
                <a class="page-link" href="#" @click.prevent="changePage(page)">{{ page }}</a>
            </li>
            <li class="page-item" :class="{ disabled: currentPage === totalPages }">
                <a class="page-link" href="#" @click.prevent="changePage(currentPage + 1)">Next</a>
            </li>
        </ul>
    </nav>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
    props: {
        currentPage: {
            type: Number,
            required: true
        },
        totalPages: {
            type: Number,
            required: true
        }
    },
    emits: ["page-changed"],
    methods: {
        changePage(page: number) {
            if (page > 0 && page <= this.totalPages) {
                this.$emit("page-changed", page);
            }
        }
    }
});
</script>

<style scoped>
.pagination .page-item .page-link {
    border: 0.0625rem solid #8DE2CD;
    color: black;
}

.pagination .page-item.active .page-link {
    background-color: #FCE26D;
    border-color: #8DE2CD;
    color: black;
    font-weight: bold;
}

.pagination .page-item.disabled .page-link {
    border-color: #8DE2CD;
}
</style>