import { defineStore } from 'pinia';
import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:8000';
export const useMainStore = defineStore('main', {
    state: () => ({
        user: null, //Get id from log in
        userId: 1,
        hobbies: [],
        userHobbies: [],
        friends: [],
    }),
    actions: {
        async fetchData() {
            try {
                const userId = 1;
                const userResponse = await axios.get(`/api/user/${userId}/`);
                this.user = userResponse.data;
                this.userId = this.user.id;
                console.log("User data", this.user);

                const hobbiesResponse = await axios.get('/api/hobbies/');
                this.hobbies = hobbiesResponse.data;
                console.log("Hobbies data", this.hobbies);

                const userHobbiesResponse = await axios.get(`/api/user/${userId}/hobbies/`);
                this.userHobbies = userHobbiesResponse.data;
                console.log("Hobbies user data", this.userHobbies);

                const friendshipResponse = await axios.get(`/api/user/${userId}/friendships/`);
                this.friends = friendshipResponse.data;
                console.log("Friends data", this.friends);
            } catch (error) {
                console.error("Can't fetch initial data", error);
            }
        }
    }
});