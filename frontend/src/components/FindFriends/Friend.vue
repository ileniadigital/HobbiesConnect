<template>
    <div class="card" style="width: 18rem;">
        <div class="card-body">
            <h5 class="card-title">{{ name }} {{ age }}</h5>
            <h6 class="card-subtitle mb-2 text-body-secondary">{{ hobbies.map(hobby => hobby.name).join(', ') }}</h6>
        </div>
        <AddFriend />
    </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
import AddFriend from "./AddFriend.vue";
import { Hobbies } from "../../utils/interfaces";

export default defineComponent({
    name: "Friend",
    components: {
        AddFriend
    },
    props: {
        name: {
            type: String,
            required: true
        },
        hobbies: {
            type: Array as PropType<Hobbies[]>,
            required: true,
            default: () => []
        },
        age: {
            type: Number,
            required: true
        }
    }
})
</script>