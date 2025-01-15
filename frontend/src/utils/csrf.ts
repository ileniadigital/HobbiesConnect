export function getCsrfToken(): string | null {
    const name = 'csrftoken';
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        cookie = cookie.trim();
        if (cookie.startsWith(name + '=')) {
            // console.log('CSRF Token found:', cookie.substring(name.length + 1)); // Log the CSRF token
            return cookie.substring(name.length + 1);
        }
    }
    // console.log('CSRF Token not found'); // Log if CSRF token is not found
    return null;
}