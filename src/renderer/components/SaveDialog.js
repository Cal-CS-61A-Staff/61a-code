import React from "react";
import FileNameField from "./FileNameField.js";
import DownloadButton from "./DownloadButton.js";

export default function SaveDialog(props) {
    return (
        <div className="modal">
            <div className="modalBody">
                <span className="close" onClick={props.onClose}>&times;</span>
                <div className="modalHeader">Save As</div>
                <div className="modalContent" style={{ flexDirection: "column" }}>
                    <FileNameField onClick={props.onNameSelect} />
                    <DownloadButton onClick={props.onDownloadClick} />
                </div>
            </div>
        </div>
    );
}
