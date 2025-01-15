import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Profile from '../pages/Profile.vue';
import FindFriends from '../pages/FindFriends.vue';
import FriendRequests from '../pages/FriendRequests.vue';

let base = (import.meta.env.MODE == 'development') ? import.meta.env.BASE_URL : ''

const routes: Array<RouteRecordRaw> = [
    { path: '/', name: 'Profile', component: Profile },
    { path: '/findfriends/', name: 'Find Friends', component: FindFriends },
    { path: '/friendrequests/', name: 'Friend Requests', component: FriendRequests }
]

const router = createRouter({
    history: createWebHistory(base),
    routes
})

export default router