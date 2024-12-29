import { defineStore } from 'pinia';
import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:8000';
export const useMainStore = defineStore('main', {
    state: () => ({
        user: null,
        friends: [],
        hobbies: [],
    }),
    actions: {
        async fetchData() {
            try {
                const userId = 1;
                const userResponse = await axios.get(`/api/user/${userId}/`); // Ensure the URL starts with '/'
                this.user = userResponse.data;
                console.log("User data", this.user);

                const hobbiesResponse = await axios.get('/api/hobbies/'); // Ensure the URL starts with '/'
                this.hobbies = hobbiesResponse.data;
                console.log("Hobbies data", this.hobbies);

                // const friendsResponse = await axios.get('/api/friends/');
                // this.friends = friendsResponse.data;
            } catch (error) {
                console.error("Can't fetch initial data", error);
            }
        }
    }
});