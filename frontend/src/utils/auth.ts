import { defineStore } from 'pinia';
import { User } from './interfaces';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isAuthenticated: false,
    user: null as User | null,
    userid: null as number | null,
  }),
  actions: {
    async checkAuthentication(): Promise<boolean> {
      try {      
      alert('Calling fetch');
      const response = await fetch('http://localhost:8000/api/authenticated/', {
        credentials: 'include',
      });

      const data = await response.json();
      console.log('Data', data);
      this.isAuthenticated = data.isAuthenticated;

      if (this.isAuthenticated) {
        // alert('You are logged in! Data will be fetched.');
        this.user = data.user;
        this.userid = data.user.id;
      } else { //logging out 
        // window.alert("You are not authenticated. Please log in.");
        this.user = null;
        this.userid = null;
        window.location.href = ('http://localhost:8000/login');
      }
      console.log('Is authenticated:', this.isAuthenticated);
      return this.isAuthenticated;
      } catch (error) {
      console.error('Error checking authentication:', error);
      return false;
      }
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