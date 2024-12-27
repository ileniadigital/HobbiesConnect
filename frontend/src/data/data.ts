// filepath: /c:/Users/ileni/Desktop/HobbiesConnect/frontend/src/stores/main.ts
import { defineStore } from 'pinia';
import axios from 'axios';

export const useMainStore = defineStore('main', {
    state: () => ({
        user: null,
        friends: [],
        hobbies: [],
    }),
    actions: {
        async fetchData() {
            try {
                const userResponse = await axios.get('/api/user');
                this.user = userResponse.data;

                const friendsResponse = await axios.get('/api/friends');
                this.friends = friendsResponse.data;

                const hobbiesResponse = await axios.get('/api/hobbies');
                this.hobbies = hobbiesResponse.data;
            } catch (error) {
                console.error("Can't fetch initial data", error);
            }
        }
    }
});