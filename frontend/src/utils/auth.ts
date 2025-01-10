import {defineStore} from 'pinia';
import Cookies from 'js-cookie';
import { User } from './interfaces.ts';

export const useAuthStore = defineStore("auth", {
    state: () => ({
        isAuthenticated: false,
        user: null as User | null,
        userid: null as number | null,
    }),
    actions: {
        login(user: User) {
            this.isAuthenticated = true;
            this.user = user;
        },
        logout() {
            this.isAuthenticated = false;
            this.user = null;
            Cookies.remove('user_id');
        }
    },
});