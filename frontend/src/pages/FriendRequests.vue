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
import { defineComponent } from "vue";

export default defineComponent({
  components: {
  },
  data() {
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
})
</script>

<style scoped></style>