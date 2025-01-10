import { defineStore } from 'pinia';
import Cookies from 'js-cookie';

const BASE_URL = 'http://127.0.0.1:8000';

export const useMainStore = defineStore('main', {
    state: () => ({
        user: null, // Get id from log in
        userId: null as string | null,
        hobbies: [],
        userHobbies: [],
        friends: [],
        isAuthenticated: false,
    }),
    actions: {
        async checkAuthentication() {
            try {
                const response = await fetch(`${BASE_URL}/authenticated/`, { credentials: 'include' });
                const data = await response.json();
                this.isAuthenticated = data.isAuthenticated;
                console.log("Is authenticated", this.isAuthenticated);
                this.userId = Cookies.get('user_id') || null;
                return this.isAuthenticated;
            } catch (error) {
                console.error("Error checking authentication", error);
                return false;
            }
        },
        async fetchData() {
            try {
                const userResponse = await fetch(`${BASE_URL}/api/user/${this.userId}/`, { credentials: 'include' });
                this.user = await userResponse.json();
                console.log("User data", this.user);

                const hobbiesResponse = await fetch(`${BASE_URL}/api/hobbies/`, { credentials: 'include' });
                this.hobbies = await hobbiesResponse.json();
                console.log("Hobbies data", this.hobbies);

                const userHobbiesResponse = await fetch(`${BASE_URL}/api/user/${this.userId}/hobbies/`, { credentials: 'include' });
                this.userHobbies = await userHobbiesResponse.json();
                console.log("Hobbies user data", this.userHobbies);

                const friendshipResponse = await fetch(`${BASE_URL}/api/user/${this.userId}/friendships/`, { credentials: 'include' });
                this.friends = await friendshipResponse.json();
                console.log("Friends data", this.friends);
            } catch (error) {
                console.error("Can't fetch initial data", error);
            }
        }
    }
});