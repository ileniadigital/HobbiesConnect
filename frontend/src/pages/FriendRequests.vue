<template>
  <div>
    <div class="h3">
      {{ title }}
    </div>
    <hr />

    <div class="row">
      <!-- Pending Requests -->
      <div class="col-md-6">
        <h2>Pending Requests</h2>
        <ul class="list-unstyled">
          <li v-for="request in pendingRequests" :key="request.id" class="mb-3">
            <Request :name="request.user" :status="request.status" :createdAt="request.created_at"
              @accept-request="acceptRequest(request.id)"
              @delete-request="openDeleteModal(request.id, request.status)" />
          </li>
        </ul>
      </div>
      <!-- My friends -->
      <div class="col-md-6">
        <h2>My Friends</h2>
        <ul class="list-unstyled">
          <li v-for="friend in acceptedRequests" :key="friend.id" class="mb-3">
            <Request :name="friend.user === user_first_name ? friend.friend : friend.user" :status="friend.status" :createdAt="friend.created_at"
              @delete-request="openDeleteModal(friend.id, friend.status)" />
          </li>
        </ul>
      </div>
    </div>

    <!-- Delete Request Modal -->
    <DeleteRequest :visible="isDeleteModalVisible" :userId="userId" :friendId="selectedFriendId"
      :status="selectedStatus" @close="isDeleteModalVisible = false" @request-deleted="handleDeleteRequest" />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import { useMainStore } from "../data/data";
import Request from "../components/FriendRequests/Request.vue";
import DeleteRequest from "../components/FriendRequests/DeleteRequest.vue";
import { Friendship } from "../utils/interfaces";

export default defineComponent({
  components: {
    Request,
    DeleteRequest,
  },
  setup() {
    const mainStore = useMainStore();
    const pendingRequests = ref<Friendship[]>([]);
    const acceptedRequests = ref<Friendship[]>([]);
    const isDeleteModalVisible = ref<boolean>(false);
    const selectedFriendId = ref<number>(-1);
    const selectedStatus = ref<string>("none");
    const user_first_name = ref(mainStore.user?.first_name ?? "");
    const userId = ref(mainStore.userId ?? 0);

    // Fetch friends
    const fetchFriends = async (): Promise<void> => {
      await mainStore.fetchData();
      pendingRequests.value = mainStore.pending_friend_requests;
      acceptedRequests.value = mainStore.friends;
    };

    // Accept request
    const acceptRequest = async (friendId: number): Promise<void> => {
      await mainStore.acceptFriendRequest(friendId);
      fetchFriends();
    };

    // Open delete modal
    const openDeleteModal = (friendId: number, status: string): void => {
      selectedFriendId.value = friendId;
      selectedStatus.value = status;
      isDeleteModalVisible.value = true;
    };

    // Handle delete request
    const handleDeleteRequest = async ({ friendId }: { friendId: number }): Promise<void> => {
      await mainStore.deleteFriendship(friendId);
      isDeleteModalVisible.value = false;
      fetchFriends();
    };

    onMounted(fetchFriends);

    return {
      title: "Friend Requests",
      pendingRequests,
      acceptedRequests,
      isDeleteModalVisible,
      selectedFriendId,
      selectedStatus,
      userId,
      user_first_name,
      acceptRequest,
      openDeleteModal,
      fetchFriends,
      handleDeleteRequest,
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