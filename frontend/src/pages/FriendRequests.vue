<template>
  <div>
    <div class="h1">
      {{ title }}
    </div>
    <!-- Pending Requests -->
    <div>
      <h2>Pending Requests</h2>
    </div>
    <!-- My friends -->
    <div>
      <h2>My Friends</h2>
      <ul>
        <li v-for="friend in friends" :key="friend.id">
          <Request :name="friend.friend" :status="friend.status" :createdAt="friend.created_at" />
        </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import { useMainStore } from "../data/data";
import Request from "../components/FriendRequests/Request.vue";

export default defineComponent({
  components: {
    Request,
  },
  setup() {
    const mainStore = useMainStore();
    const friends = ref([]);

    async function fetchFriends() {
      await mainStore.fetchData();
      friends.value = mainStore.friends;
      console.log("Friends in list:", friends.value);
    }
    onMounted(fetchFriends);

    return {
      title: "Friend Requests",
      friends,
    };
  }
});
</script>

<style scoped></style>