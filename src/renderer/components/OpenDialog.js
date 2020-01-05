import * as React from "react";
import UploadFileSelector from "./UploadFileSelector.js";
import { dialogWrap } from "../utils/dialogWrap.js";
import FileSelector from "./FileSelector.js";

function OpenDialog({ recents, onFileSelect, onBackupsButtonClick }) {
    return (
        <>
            <UploadFileSelector onFileSelect={onFileSelect} />
            <FileSelector
                recentFiles={recents}
                onFileSelect={onFileSelect}
                onBackupsButtonClick={onBackupsButtonClick}
            />
        </>
    );
}

export default dialogWrap("Open", OpenDialog, "row");
