import React from "react";
import FileNameField from "./FileNameField.js";
import ModalButton from "./ModalButton.js";
import { dialogWrap } from "../utils/dialogWrap.js";

function SaveDialog(props) {
    return (
        <>
            <FileNameField
                defaultValue={props.defaultValue}
                onClick={props.onNameSelect}
            />
            <ModalButton buttonText="Download" onClick={props.onDownloadClick}>
                <p>Or download a copy of your code to save on your computer.</p>
            </ModalButton>
        </>
    );
}

export default dialogWrap("Save", SaveDialog, "column");
