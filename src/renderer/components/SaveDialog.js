import React from "react";
import FileNameField from "./FileNameField.js";
import DownloadButton from "./DownloadButton.js";
import { dialogWrap } from "../utils/dialogWrap.js";

function SaveDialog(props) {
    return (
        <>
            <FileNameField
                defaultValue={props.defaultValue}
                onClick={props.onNameSelect}
            />
            <DownloadButton onClick={props.onDownloadClick} />
        </>
    );
}

export default dialogWrap("Save", SaveDialog, "column");
