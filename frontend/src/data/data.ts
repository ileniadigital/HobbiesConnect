// filepath: /c:/Users/ileni/Desktop/HobbiesConnect/frontend/src/stores/main.ts
import { defineStore } from 'pinia';
import axios from 'axios';

export const useMainStore = defineStore('main', {
    state: () => ({
        user: 1,
        friends: [],
        hobbies: [],
    }),
    actions: {
        async fetchData() {
            try {
                const userId = 1;
                const userResponse = await axios.get(`api/user/${userId}/`);
                this.user = userResponse.data;
                console.log("User data", this.user);

                const hobbiesResponse = await axios.get('/api/hobbies');
                this.hobbies = hobbiesResponse.data;
                console.log("Hobbies data", this.hobbies);

                // const friendsResponse = await axios.get('/api/friends');
                // this.friends = friendsResponse.data;
            } catch (error) {
                console.error("Can't fetch initial data", error);
            }
        }
    }
});