import * as React from "react";
import UploadFileSelector from "./UploadFileSelector.js";
import RecentFileSelector from "./RecentFileSelector.js";
import { dialogWrap } from "../utils/dialogWrap.js";

function OpenDialog(props) {
    return (
        <>
            <UploadFileSelector onFileSelect={props.onFileSelect} />
            <RecentFileSelector
                files={props.recents}
                onFileSelect={props.onFileSelect}
            />
        </>
    );
}

export default dialogWrap("Open", OpenDialog, "row");
