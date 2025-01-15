import { defineStore } from 'pinia';
import { User, Hobbies, UserHobby, Friendship } from '../utils/interfaces';
import { useAuthStore } from '../utils/auth';
import { getCsrfToken } from '../utils/csrf';

export const useMainStore = defineStore('main', {
    state: () => ({
        user: null as User | null,
        userId: null as number | null,
        hobbies: [] as Hobbies[],
        userHobbies: [] as UserHobby[],
        pending_friend_requests: [] as Friendship[],
        friends: [] as Friendship[], 
        similarUsers: [] as User[],
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
                const userResponse: Response = await fetch(`/user/${this.userId}/`, { credentials: 'include' });
                if (!userResponse.ok) {
                    throw new Error('Failed to fetch user data');
                }
                this.user = await userResponse.json() as User;
                // console.log("User data", this.user);
            } catch (error) {
                console.error("Failed to fetch user data", error);
            }
        },
        // Fetch similar users based on age filter
        async fetchSimilarUsers(filter: { ageFrom: number, ageTo: number }): Promise<void> {
            try {
                const response = await fetch(`/api/similar-users/${this.userId}?age_from=${filter.ageFrom}&age_to=${filter.ageTo}`, { credentials: 'include' });
                if (!response.ok) {
                    throw new Error('Failed to fetch similar users');
                }
                const data = await response.json();
                this.similarUsers = data.users;
                console.log('Similar users:', this.similarUsers);
            } catch (error) {
                console.error('Error fetching similar users:', error);
            }
        },
        // Fetch hobbies data
        async fetchHobbies(): Promise<void> {
            try {
                const hobbiesResponse: Response = await fetch(`/api/hobbies/`, { credentials: 'include' });
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
                const userHobbiesResponse: Response = await fetch(`/user/${this.userId}/hobbies/`, { credentials: 'include' });
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
            } catch (error) {
                console.error("Failed to fetch user hobbies data", error);
            }
        },
        // Fetch friends data
        async fetchFriends(): Promise<void> {
            try {
                const friendshipResponse: Response = await fetch(`/user/${this.userId}/friendships/`, { credentials: 'include' });
                if (!friendshipResponse.ok) {
                    throw new Error('Failed to fetch friends data');
                }
                const friendshipData = await friendshipResponse.json();
                this.pending_friend_requests = friendshipData.pending_requests as Friendship[];
                this.friends = friendshipData.friends as Friendship[];
                console.log("Pending friend requests", this.pending_friend_requests);
                console.log("Friends data", this.friends);
            } catch (error) {
                console.error("Failed to fetch friends data", error);
            }
        },
        // Add friend
        async handleAddFriend(userId: number, friendId: number): Promise<void> {
            try {
                const response = await fetch(`/api/friendship/create/`, {
                    credentials: 'include',
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCsrfToken() || '',
                    },
                    body: JSON.stringify({ 
                        user_id: userId,
                        friend_id: friendId 
                    })
                });
                const data = await response.json();
                if (!response.ok) {
                    throw new Error(data.message || 'Failed to add friend');
                }
                console.log('Friend added:', data);
            } catch (error) {
                console.error('Error adding friend:', (error as any).message);
            }
        },
        // Accept friend request
        async acceptFriendRequest(friendshipId: number): Promise<void> {
            try {
                const response = await fetch(`/friendship/accept/${friendshipId}/`, {
                    method: 'PUT',
                    credentials: 'include',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCsrfToken() || '',
                    },
                });
                if (!response.ok) {
                    throw new Error('Failed to accept friend request');
                }
                await this.fetchFriends();
            } catch (error) {
                console.error("Failed to accept friend request", error);
            }
        },
        // Delete friend request or unfriend
        async deleteFriendship(friendshipId: number): Promise<void> {
            try {
                const response = await fetch(`/friendship/delete/${friendshipId}/`, {
                    method: 'DELETE',
                    credentials: 'include',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCsrfToken() || '',
                    },
                });
                if (!response.ok) {
                    throw new Error('Failed to delete friendship');
                }
                await this.fetchFriends();
            } catch (error) {
                console.error("Failed to delete friendship", error);
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