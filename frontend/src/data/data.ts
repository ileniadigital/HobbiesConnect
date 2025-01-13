import { defineStore } from 'pinia';
import { User, Hobbies, UserHobby, Friendship } from '../utils/interfaces';

const BASE_URL = 'http://127.0.0.1:8000';

export const useMainStore = defineStore('main', {
    state: () => ({
        user: null as User | null, 
        userId: 4,
        hobbies: [] as Hobbies[],
        userHobbies: [] as UserHobby[],
        friends: [] as Friendship[], 
    }),
    actions: {
        async fetchData() {
            try {
                // Fetch user data
                const userResponse = await fetch(`${BASE_URL}/user/${this.userId}/`, { credentials: 'include' });
                if (!userResponse.ok) {
                    throw new Error('Failed to fetch user data');
                }
                this.user = await userResponse.json() as User;
                this.userId = this.user.id;
                console.log("User data", this.user);

                const hobbiesResponse = await fetch(`${BASE_URL}/api/hobbies/`, { credentials: 'include' });
                this.hobbies = await hobbiesResponse.json();
                console.log("Hobbies data", this.hobbies);

                // Fetch user hobbies data
                const userHobbiesResponse = await fetch(`${BASE_URL}/user/${this.userId}/hobbies/`, { credentials: 'include' });
                if (!userHobbiesResponse.ok) {
                    throw new Error('Failed to fetch user hobbies data');
                }
                const userHobbiesData = await userHobbiesResponse.json();
                this.userHobbies = userHobbiesData.map((uh: any) => ({
                    id: uh.id,
                    user: uh.user,
                    hobby: {
                        id: uh.hobby_id,
                        name: uh.hobby,
                        description: uh.description
                    }
                })) as UserHobby[];
                console.log("Hobbies user data", this.userHobbies);

                // Fetch friends data
                const friendshipResponse = await fetch(`${BASE_URL}/user/${this.userId}/friendships/`, { credentials: 'include' });
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