import React from "react";
import "../style/FolderIndicator.css";

export default function FolderIndicator(props) {
    return (props.folderName
        && (
            <span className="folderIndicator pathIndicatorElem">
                {" "}
                {props.folderName}
                {" "}
                <i className="fas fa-chevron-right" />
            </span>
        )
    );
}
