<template>
  <div>
    <div class="h3">
      {{ title }}
    </div>
    <hr />
    <!-- <div class="h3">Hi, {{ name }}</div> -->

    <div class="row">
      <!-- Pending Requests -->
      <div class="col-md-6">
        <h2>Pending Requests</h2>
        <ul class="list-unstyled">
          <li v-for="request in pendingRequests" :key="request.id">
            <Request :name="request.friend" :status="request.status" :createdAt="request.created_at"
              @delete-request="openDeleteModal(request.id, request.status)" />
          </li>
        </ul>
      </div>
      <!-- My friends -->
      <div class="col-md-6">
        <h2>My Friends</h2>
        <ul class="list-unstyled">
          <li v-for="friend in acceptedRequests" :key="friend.id">
            <Request :name="friend.friend" :status="friend.status" :createdAt="friend.created_at"
              @delete-request="openDeleteModal(friend.id, friend.status)" />
          </li>
        </ul>
      </div>
    </div>

    <!-- Delete Request Modal -->
    <DeleteRequest :visible="isDeleteModalVisible" :userId="userId" :friendId="selectedFriendId"
      :status="selectedStatus" @close="isDeleteModalVisible = false" @request-deleted="fetchFriends" />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import { useMainStore } from "../data/data";
import Request from "../components/FriendRequests/Request.vue";
import DeleteRequest from "../components/FriendRequests/DeleteRequest.vue";

interface Friend {
  id: number;
  friend: string;
  status: string;
  created_at: string;
  accepted: boolean;
}

export default defineComponent({
  components: {
    Request,
    DeleteRequest,
  },
  setup() {
    const mainStore = useMainStore();
    const friends = ref<Friend[]>([]);
    const pendingRequests = ref<Friend[]>([]);
    const acceptedRequests = ref<Friend[]>([]);
    const isDeleteModalVisible = ref(false);
    const selectedFriendId = ref<number>(-1);
    const selectedStatus = ref<string>("none");
    const userId = ref(mainStore.userId);

    const fetchFriends = async () => {
      await mainStore.fetchData();
      friends.value = mainStore.friends;
      pendingRequests.value = friends.value.filter(friend => !friend.accepted);
      acceptedRequests.value = friends.value.filter(friend => friend.accepted);
    };

    const openDeleteModal = (friendId: number, status: string) => {
      selectedFriendId.value = friendId;
      selectedStatus.value = status;
      isDeleteModalVisible.value = true;
    };

    onMounted(fetchFriends);

    return {
      title: "Friend Requests",
      name: mainStore.user.first_name,
      pendingRequests,
      acceptedRequests,
      isDeleteModalVisible,
      selectedFriendId,
      selectedStatus,
      userId,
      openDeleteModal,
      fetchFriends,
    };
  }
});
</script>

<style scoped>
.row {
  margin-top: 2rem;
}

.list-unstyled {
  padding: 0;
}
</style>