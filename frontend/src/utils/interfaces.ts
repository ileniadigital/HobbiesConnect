export interface User {
    id: number;
    email: string;
    first_name: string;
    last_name: string;
    dob: string;
    is_staff?: boolean;
    is_superuser?: boolean;
    groups?: string[];
    user_permissions?: string[];
    hobbies?: Hobbies[];
    age?: number;
    common_hobbies_count?: number;
}

export interface Hobbies {
    id: number;
    name: string;
    description: string;
}

export interface UserHobby {
    user: User;
    hobby: Hobbies;
}

export interface Friendship {
    id: number;
    user: string;
    friend: string;
    status: 'PENDING' | 'ACCEPTED' | 'REJECTED';
    accepted: boolean;
    created_at: string;
}