import { defineStore } from 'pinia';
import { User } from './interfaces';
import { getCsrfToken } from './csrf';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isAuthenticated: false,
    user: null as User | null,
    userid: null as number | null,
  }),
  actions: {
    async checkAuthentication() {
      try {
        const csrfToken = await this.waitForCsrfToken();
        console.log('CSRF Token:', csrfToken);

        const response = await fetch('http://127.0.0.1:8000/api/authenticated/', {
          credentials: 'include',
          headers: {
            'X-CSRFToken': csrfToken || '',
          },
        });

        const data = await response.json();
        console.log('Data', data);

        if (data.isAuthenticated) {
          this.isAuthenticated = data.isAuthenticated;
          this.user = data.user;
          this.userid = data.user.id;
        } else {
          this.isAuthenticated = false;
          this.user = null;
          this.userid = null;
          window.location.replace('http://127.0.0.1:8000/login/');
        }
        console.log('Is authenticated:', this.isAuthenticated);
      } catch (error) {
        console.error('Error checking authentication:', error);
      }
    },

    // Retry loop to wait for CSRF token to appear in cookies.
    async waitForCsrfToken(retries = 100, delay = 200): Promise<string | null> {
      for (let i = 0; i < retries; i++) {
        const token = getCsrfToken();
        if (token) return token;
        await new Promise(resolve => setTimeout(resolve, delay));
      }
      return null;
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