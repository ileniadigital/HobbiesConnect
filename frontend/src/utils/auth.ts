import { defineStore } from 'pinia';
import { User } from './interfaces';
import { getCsrfToken} from './csrf';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isAuthenticated: false,
    user: null as User | null,
    userid: null as number | null,
  }),
  actions: {
    async checkAuthentication(): Promise<boolean> {
      try {
      const csrfToken = getCsrfToken();
      console.log('CSRF Token:', csrfToken);
      const sessionId = document.cookie
        .split('; ')
        .find(row => row.startsWith('sessionid='))
        ?.split('=')[1];
      console.log('Session ID:', sessionId);
      
      const response = await fetch('http://localhost:8000/api/authenticated/', {
        credentials: 'include',
      });

      const data = await response.json();
      console.log('Data', data);
      this.isAuthenticated = data.isAuthenticated;

      if (this.isAuthenticated) {
        alert('You are logged in!');
        this.user = data.user;
        this.userid = data.user.id;
      } else { //logging out 
        alert('You are logged out!');
        this.user = null;
        this.userid = null;
        window.location.href = ('http://127.0.0.1:8000/login');
      }
      console.log('Is authenticated:', this.isAuthenticated);
      return this.isAuthenticated;
      } catch (error) {
      console.error('Error checking authentication:', error);
      return false;
      }
    },
    clearCsrfToken() {
      document.cookie.split(';').forEach(cookie => {
        document.cookie = cookie
          .replace(/^ +/, '')
          .replace(/=.*/, `=;expires=${new Date(0).toUTCString()};path=/`);
      });
    },
  },
  getters: {
    get_user_id(): number | null {
      return this.user ? this.user.id : null;
    },
    get_user(): User | null {
      return this.user;
    },
    get_authenticated(): boolean {
      return this.isAuthenticated;
    },
  },
});