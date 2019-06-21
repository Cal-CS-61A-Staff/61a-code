import React from "react";
import FileSystemOpen from "./LocalFileSelector.js";
import BrowserFileSelector from "./BrowserFileSelector.js";

export default function OpenDialog(props) {
    return (
        <div className="modal">
            <div className="modalBody">
                <span className="close" onClick={props.onClose}>&times;</span>
                <div className="modalHeader">Open</div>
                <div className="modalContent">
                    <FileSystemOpen onFileSelect={props.onFileSelect} />
                    <BrowserFileSelector onFileSelect={props.onFileSelect} />
                </div>
            </div>
        </div>
    );
}
