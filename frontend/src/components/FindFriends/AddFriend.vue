<template>
    <button :class="buttonClass" @click="addFriend">{{ buttonText }}</button>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from "vue";

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
    setup(props, { emit }) {
        const isRequestSent = ref(false);

        const addFriend = () => {
            console.log('Add friend:', props.userId, props.friendId);
            isRequestSent.value = true;
            emit('add-friend', { userId: props.userId, friendId: props.friendId });
        };

        const buttonClass = computed(() => {
            return isRequestSent.value ? 'btn btn-success' : 'btn btn-primary';
        });

        const buttonText = computed(() => {
            return isRequestSent.value ? 'Friend Request Sent' : 'Send Friend Request';
        });

        return {
            isRequestSent,
            addFriend,
            buttonClass,
            buttonText
        };
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

.btn-success,
.btn-success:hover {
    background-color: #8DE2CD;
    color: black;
    border: none;
    border-radius: 0.5rem;
}

.btn-primary:hover,
.btn-success:hover {
    font-weight: bold;
}
</style>