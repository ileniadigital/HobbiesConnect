<template>
    <div>
        <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#deleteHobbyModal">
            Delete Hobby
        </button>

        <div class="modal fade" id="deleteHobbyModal" tabindex="-1" aria-labelledby="deleteHobbyModalLabel"
            aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="deleteHobbyModalLabel">Confirm Delete</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        Are you sure you want to delete this hobby?
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                        <button type="button" class="btn btn-danger" @click="confirmDelete">Delete</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
    methods: {
        confirmDelete() {
            console.log("Delete hobby");
        }
    }
});
</script>