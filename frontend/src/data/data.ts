import { defineStore } from 'pinia';
import {User, Hobbies, UserHobby, Friendship} from '../utils/interfaces';

const BASE_URL = "http://127.0.0.1:8000/api";
export const useMainStore = defineStore('main', {
    state: () => ({
        user: null as User | null, 
        userId: 1,
        hobbies: [] as Hobbies[],
        userHobbies: [] as UserHobby[],
        friends: [] as Friendship[], 
    }),
    actions: {
        async fetchData() {
            try {
                const userId = 4;

                // Fetch user data
                const userResponse = await fetch(`${BASE_URL}/user/${userId}/`);
                if (!userResponse.ok) {
                    throw new Error('Failed to fetch user data');
                }
                this.user = await userResponse.json() as User;
                this.userId = this.user.id;
                console.log("User data", this.user);

                // Fetch hobbies data
                const hobbiesResponse = await fetch(`${BASE_URL}/hobbies/`);
                if (!hobbiesResponse.ok) {
                    throw new Error('Failed to fetch hobbies data');
                }
                this.hobbies = await hobbiesResponse.json() as Hobbies[];
                console.log("Hobbies data", this.hobbies);

                // Fetch user hobbies data
                const userHobbiesResponse = await fetch(`${BASE_URL}/user/${userId}/hobbies/`);
                if (!userHobbiesResponse.ok) {
                    throw new Error('Failed to fetch user hobbies data');
                }
                this.userHobbies = await userHobbiesResponse.json() as UserHobby[];
                console.log("Hobbies user data", this.userHobbies);

                // Fetch friends data
                const friendshipResponse = await fetch(`${BASE_URL}/user/${userId}/friendships/`);
                if (!friendshipResponse.ok) {
                    throw new Error('Failed to fetch friends data');
                }
                this.friends = await friendshipResponse.json() as Friendship[];
                console.log("Friends data", this.friends);
            } catch (error) {
                console.error("Can't fetch initial data", error);
            }
        }
    }
});