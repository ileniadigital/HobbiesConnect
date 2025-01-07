import { createRouter, createWebHistory } from 'vue-router'

// 1. Define route components.
import Profile from '../pages/Profile.vue';
import FindFriends from '../pages/FindFriends.vue';
import FriendRequests from '../pages/FriendRequests.vue';

let base = (import.meta.env.MODE == 'development') ? import.meta.env.BASE_URL : ''

// 2. Define some routes
// Each route should map to a component.
const router = createRouter({
    history: createWebHistory(base),
    routes: [
        { path: '/', name: 'Profile', component: Profile},
        { path: '/findfriends/', name: 'Find Friends', component: FindFriends},
        { path: '/friendrequests/', name: 'Friend Requests', component: FriendRequests}
    ]
})

export default router
