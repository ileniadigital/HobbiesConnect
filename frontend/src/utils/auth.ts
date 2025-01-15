import { defineStore } from 'pinia';
import { User } from './interfaces';

export const useAuthStore = defineStore('auth', {
  state: () : { isAuthenticated: boolean; user: User | null; userid: number | null } => ({
    isAuthenticated: false,
    user: null as User | null,
    userid: null as number | null,
  }),
  actions: {
    async checkAuthentication(): Promise<boolean> {
      try {      
      const response = await fetch('http://localhost:8000/api/authenticated/', {
        credentials: 'include',
      });

      const data: { isAuthenticated: boolean; user: User } = await response.json();
      // console.log('Data', data);
      this.isAuthenticated = data.isAuthenticated;

      if (this.isAuthenticated) {
        this.user = data.user;
        this.userid = data.user.id;
      } else { //logging out 
        this.user = null;
        this.userid = null;
        window.location.href = ('http://localhost:8000/login');
      }
      // console.log('Is authenticated:', this.isAuthenticated);
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
    get_authenticated(): boolean {
      return this.isAuthenticated;
    },
  },
});