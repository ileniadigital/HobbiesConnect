<template>
  <div>
    <div class="h1">
      {{ title }}
    </div>
    <hr />

    <div class="row">
      <!-- Pending Requests -->
      <div class="col-md-6">
        <h2>Pending Requests</h2>
        <div v-for="request in pendingRequests" :key="request.id">
          <Request :name="request.friend" :status="request.status" :createdAt="request.created_at" />
        </div>
      </div>
      <!-- My friends -->
      <div class="col-md-6">
        <h2>My Friends</h2>
        <div v-for="friend in acceptedRequests" :key="friend.id">
          <Request :name="friend.friend" :status="friend.status" :createdAt="friend.created_at" />
        </div>
      </div>
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
    const pendingRequests = ref([]);
    const acceptedRequests = ref([]);

    async function fetchFriends() {
      await mainStore.fetchData();
      friends.value = mainStore.friends;
      console.log("Friends:", friends.value);
      // Sort friendships into accepted and pending
      pendingRequests.value = friends.value.filter((f) => f.status === "PENDING");
      console.log("Pending:", pendingRequests.value);
      acceptedRequests.value = friends.value.filter((f) => f.status === "ACCEPTED");
      console.log("Accepted:", acceptedRequests.value);
    }
    onMounted(fetchFriends);

    return {
      title: "Friend Requests",
      pendingRequests,
      acceptedRequests,
    };
  }
});
</script>

<style scoped>
.row {
  margin-top: 2rem;
}
</style>