import * as React from "react";
import UploadFileSelector from "./UploadFileSelector.js";
import { dialogWrap } from "../utils/dialogWrap.js";
import RecentFileSelector from "./RecentFileSelector.js";

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
