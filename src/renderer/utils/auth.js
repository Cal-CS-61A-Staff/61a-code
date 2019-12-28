import $ from "jquery";

export function login() {
    window.open("/popup_login", "_blank");
}

export function logout() {
    window.open("/popup_logout", "_blank");
}

const handlers = new Set();
let authData = { loggedOut: true };

export async function checkLoggedIn() {
    let newAuthData;
    try {
        newAuthData = await $.post("/api/user");
    } catch {
        newAuthData = { loggedOut: true };
    }
    if (JSON.stringify(newAuthData) !== JSON.stringify(authData)) {
        authData = newAuthData;
        for (const { handler } of handlers) {
            handler(authData);
        }
    }
}

setInterval(checkLoggedIn, 5000);

window.addEventListener("focus", checkLoggedIn);

export function addAuthListener(handler) {
    const wrappedHandler = { handler };
    handlers.add(wrappedHandler);
    return () => { handlers.remove(wrappedHandler); };
}
