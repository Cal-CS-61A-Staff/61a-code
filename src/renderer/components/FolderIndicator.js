import React from "react";

export default function FolderIndicator(props) {
    return (
        <span key={props.key}>
            <button type="button">
                {props.folderName}
            </button>
        </span>
    );
}
