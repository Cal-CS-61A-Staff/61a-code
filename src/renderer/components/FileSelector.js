import React from "react";
import RecentFileSelector from "./RecentFileSelector.js";
import OkBackupsButton from "./OkBackupsButton.js";
import "../style/FileSelector.css";

export default function FileSelector({ recentFiles, onFileCreate, onBackupsButtonClick }) {
    return (
        <div className="recentHolder browserFileSelector">
            <RecentFileSelector
                files={recentFiles}
                onFileSelect={onFileCreate}
            />
            <br />
            <OkBackupsButton
                onBackupsButtonClick={onBackupsButtonClick}
            />
        </div>
    );
}
