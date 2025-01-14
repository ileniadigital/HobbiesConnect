import { defineStore } from 'pinia';
import { User, Hobbies, UserHobby, Friendship } from '../utils/interfaces';
import { useAuthStore } from '../utils/auth';

const BASE_URL = 'http://localhost:8000';

export const useMainStore = defineStore('main', {
    state: () => ({
        user: null as User | null,
        userId: null as number | null,
        hobbies: [] as Hobbies[],
        userHobbies: [] as UserHobby[],
        friends: [] as Friendship[], 
        isAuthenticated: false 
    }),
    actions: {
        // Fetch all data
        async fetchData() {
            try {
                const authStore = useAuthStore();
                const isAuthenticated: boolean = await authStore.checkAuthentication();
                if (!isAuthenticated) {
                    throw new Error('User is not authenticated');
                }
                this.userId = authStore.get_user_id;
                // console.log("User ID", this.userId);

                await this.fetchUser();
                await this.fetchHobbies();
                await this.fetchUserHobbies();
                await this.fetchFriends();
            } catch (error) {
                console.error("Can't fetch initial data", error);
            }
        },
        // Fetch user data
        async fetchUser(): Promise<void> {
            try {
                const userResponse: Response = await fetch(`${BASE_URL}/user/${this.userId}/`, { credentials: 'include' });
                if (!userResponse.ok) {
                    throw new Error('Failed to fetch user data');
                }
                this.user = await userResponse.json() as User;
                // console.log("User data", this.user);
            } catch (error) {
                console.error("Failed to fetch user data", error);
            }
        },
        // Fetch hobbies data
        async fetchHobbies(): Promise<void> {
            try {
                const hobbiesResponse: Response = await fetch(`${BASE_URL}/api/hobbies/`, { credentials: 'include' });
                if (!hobbiesResponse.ok) {
                    throw new Error('Failed to fetch hobbies data');
                }
                this.hobbies = await hobbiesResponse.json() as Hobbies[];
                // console.log("Hobbies data", this.hobbies);
            } catch (error) {
                console.error("Failed to fetch hobbies data", error);
            }
        },
        // Fetch user hobbies data
        async fetchUserHobbies(): Promise<void> {
            try {
                const userHobbiesResponse: Response = await fetch(`${BASE_URL}/user/${this.userId}/hobbies/`, { credentials: 'include' });
                if (!userHobbiesResponse.ok) {
                    throw new Error('Failed to fetch user hobbies data');
                }
                const userHobbiesData: any[] = await userHobbiesResponse.json();
                this.userHobbies = userHobbiesData.map((uh: any) => ({
                    id: uh.id,
                    user: uh.user,
                    hobby: {
                        id: uh.hobby_id,
                        name: uh.hobby,
                        description: uh.description
                    }
                })) as UserHobby[];
                // console.log("Hobbies user data", this.userHobbies);
            } catch (error) {
                console.error("Failed to fetch user hobbies data", error);
            }
        },
        // Fetch friends data
        async fetchFriends(): Promise<void> {
            try {
                const friendshipResponse: Response = await fetch(`${BASE_URL}/user/${this.userId}/friendships/`, { credentials: 'include' });
                if (!friendshipResponse.ok) {
                    throw new Error('Failed to fetch friends data');
                }
                this.friends = await friendshipResponse.json() as Friendship[];
                // console.log("Friends data", this.friends);
            } catch (error) {
                console.error("Failed to fetch friends data", error);
            }
        }
    },
    getters: {
        get_user_id(): number | null {
            return this.userId;
        },
        get_user(): User | null {
            return this.user;
        },
    },
});