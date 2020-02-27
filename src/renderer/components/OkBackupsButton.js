import React from "react";
import { login } from "../utils/auth.js";
import { useAuthData } from "../utils/okUtils.js";

import "../style/OkBackupsButton.css";

export default function OkBackupsButton({ onBackupsButtonClick }) {
    const { loggedOut } = useAuthData();

    const handleBackupsClick = async () => {
        if (loggedOut) {
            login();
        } else {
            onBackupsButtonClick();
        }
    };

    const okButtonText = `${loggedOut ? "Login" : "Click"} to view backups`;

    return (
        <div>
            <div className="LaunchScreenHeader">OKPy Backups</div>
            <button className="BackupButton" onClick={handleBackupsClick} type="button">
                {okButtonText}
            </button>
        </div>
    );
}
