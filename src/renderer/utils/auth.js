import $ from "jquery";
import { useEffect, useState } from "react";

export function login() {
    window.open("/popup_login", "_blank");
}

export function logout() {
    window.open("/popup_logout", "_blank");
}

const handlers = new Set();
let currAuthData = { loggedOut: true };

export async function checkLoggedIn() {
    let newAuthData;
    try {
        newAuthData = await $.post("/api/user");
    } catch {
        newAuthData = { loggedOut: true };
    }
    if (JSON.stringify(newAuthData) !== JSON.stringify(currAuthData)) {
        currAuthData = newAuthData;
        for (const { handler } of handlers) {
            handler(currAuthData);
        }
    }
}

export function isStaff(authData) {
    return authData.data.participations.some(
        ({ course, role }) => ["staff", "instructor"].includes(role) && course.offering.startsWith("cal/cs61a/"),
    );
}

export function useAuthData() {
    const [authData, setAuthData] = useState(currAuthData);
    useEffect(() => addAuthListener(setAuthData));
    return authData;
}

checkLoggedIn();
setInterval(checkLoggedIn, 5000);

window.addEventListener("focus", checkLoggedIn);

export function addAuthListener(handler) {
    const wrappedHandler = { handler };
    handlers.add(wrappedHandler);
    return () => { handlers.delete(wrappedHandler); };
}
