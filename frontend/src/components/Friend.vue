<template>
    <div class="card" style="width: 18rem;">
        <div class="card-body">
            <h5 class="card-title">{{ name }} {{ age }}</h5>
            <h6 class="card-subtitle mb-2 text-body-secondary">{{ hobbies.join(', ') }}</h6>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";

export default defineComponent({
    name: "Friend",
    props: {
        name: {
            type: String,
            required: true
        },
        hobbies: {
            type: Array as PropType<string[]>,
            required: true
        },
        age: {
            type: Number,
            required: true
        }
    }
})
</script>