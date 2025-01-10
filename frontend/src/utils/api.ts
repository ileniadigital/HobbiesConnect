import { User } from './interfaces.ts';
import Cookies from "js-cookie";

class API {

    private static url: string = "http://127.0.0.1:8000/api/";

    /**
     * Fetches a DTO of the current logged in user
     */
    static fetchUser = async (): Promise<User> => {
        const result = await fetch(`${this.url}users/current`, {credentials: 'include'});
        const User = await result.json() as User;
        console.log(User);
        return User;
    }
}

export default API;