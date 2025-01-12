<!-- <template>
    <button class="btn btn-primary" @click="addFriend">Add Friend</button>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
    name: "AddFriend",
    methods: {
        addFriend() {
            alert('Friend added!');
        }
    }
})
</script>

<style scoped>
.btn-primary,
.btn-primary:hover {
    background-color: #fce26d;
    color: black;
    border: none;
    border-radius: 0.5rem;
    padding: 0.5rem 1rem;
    cursor: pointer;
}

.btn-primary:hover {
    font-weight: bold;
}
</style> -->

<template>
    <button class="btn btn-primary" @click="addFriend">Add Friend</button>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
    name: "AddFriend",
    props: {
        userId: {
            type: Number,
            required: true
        },
        friendId: {
            type: Number,
            required: true
        }
    },
    methods: {
        addFriend() {
            console.log('Add friend:', this.userId, this.friendId);
            this.$emit('add-friend', { userId: this.userId, friendId: this.friendId });
        }
    }
});
</script>

<style scoped>
.btn-primary,
.btn-primary:hover {
    background-color: #fce26d;
    color: black;
    border: none;
    border-radius: 0.5rem;
    padding: 0.5rem 1rem;
    cursor: pointer;
}

.btn-primary:hover {
    font-weight: bold;
}
</style>