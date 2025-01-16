<template>
    <div v-if="visible" class="modal fade show" tabindex="-1" style="display: block;" aria-modal="true" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Add Hobby</h5>
                    <button type="button" class="btn-close" @click="close" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <!-- Add hobby from existing ones -->
                    <div>
                        <h6>Add hobby from existing ones</h6>
                        <div class="mb-3">
                            <label for="hobbySelect" class="form-label">Select a hobby:</label>
                            <select id="hobbySelect" class="form-select" v-model="selectedHobbyId">
                                <option value="">Select a hobby</option>
                                <option v-for="hobby in hobbies" :key="hobby.id" :value="hobby.id">
                                    {{ hobby.name }}
                                </option>
                            </select>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" @click="close">Close</button>
                            <button type="button" class="btn btn-primary" id="addHobby-button"
                                @click="addExistingHobby">Add Hobby</button>
                        </div>
                    </div>
                    <!-- Create a new hobby -->
                    <div>
                        <h6>Create a new hobby</h6>
                        <form @submit.prevent="addHobby">
                            <div class="mb-3">
                                <label for="hobby" class="form-label">Hobby:</label>
                                <input type="text" id="hobby" v-model="hobby" class="form-control" required />
                            </div>
                            <div class="mb-3">
                                <label for="description" class="form-label">Description:</label>
                                <input type="text" id="description" v-model="description" class="form-control"
                                    required />
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" @click="close">Close</button>
                                <button type="submit" class="btn btn-primary" id="createHobby-button">Create
                                    Hobby</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref, watch, PropType } from "vue";
import { getCsrfToken } from "../../utils/csrf";

interface Hobby {
    id: number;
    name: string;
    description: string;
}

export default defineComponent({
    props: {
        visible: {
            type: Boolean,
            required: true
        },
        userId: {
            type: Number,
            required: true
        },
        hobbies: {
            type: Array as PropType<Hobby[]>,
            required: true,
            default: () => []
        }
    },
    emits: ["close", "hobby-added"],
    setup(props, { emit }) {
        const hobby = ref<string>("");
        const description = ref<string>("");
        const selectedHobbyId = ref<number | null>(null);
        // console.log("Hobbies in AddHobby:", props.hobbies);

        watch(
            () => props.visible,
            (newVal) => {
                if (!newVal) {
                    // Clear input fields when the modal is closed
                    hobby.value = "";
                    description.value = "";
                    selectedHobbyId.value = null;
                }
            }
        );

        const close = (): void => {
            emit("close");
        };

        const addHobby = async (): Promise<void> => {
            try {
                const response = await fetch('/api/hobbies/add_user_hobby/', {
                    credentials: 'include',
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCsrfToken() || '',
                    },
                    body: JSON.stringify({
                        user_id: props.userId,
                        name: hobby.value,
                        description: description.value
                    })
                });
                if (!response.ok) {
                    throw new Error('Something went wrong');
                }
                // const data = await response.json();
                // console.log("Hobby added:", data);
                emit("hobby-added");
                close();
            } catch (error) {
                console.error('There was a problem with the fetch operation:', error);
            }
        };

        const addExistingHobby = async (): Promise<void> => {
            if (selectedHobbyId.value === null) {
                return;
            }
            // console.log("User ID:", props.userId);
            // console.log("Selected Hobby ID:", selectedHobbyId.value);
            try {
                const response = await fetch('/api/user_hobbies/add/', {
                    credentials: 'include',
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCsrfToken() || '',
                    },
                    body: JSON.stringify({
                        user_id: props.userId,
                        hobby_id: selectedHobbyId.value
                    })
                });
                if (!response.ok) {
                    throw new Error('Something went wrong');
                }
                // const data = await response.json();
                // console.log("Existing hobby added:", data);
                emit("hobby-added");
                close();
            } catch (error) {
                console.error('There was a problem with the fetch operation:', error);
            }
        };

        return {
            hobby,
            description,
            selectedHobbyId,
            close,
            addHobby,
            addExistingHobby
        };
    }
});
</script>

<style scoped>
.modal-content {
    padding: 1.25rem;
}

.btn-primary,
.btn-primary:hover,
.btn-primary:active {
    background-color: #FCE26D;
    border: none;
    color: black;
}

.btn-primary:hover,
.btn-primary:active {
    font-weight: bold;
}
</style>