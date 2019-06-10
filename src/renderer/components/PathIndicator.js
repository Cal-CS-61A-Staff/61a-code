import React from "react";
import FolderIndicator from "./FolderIndicator";
import FileIndicator from "./FileIndicator";

export default function PathIndicator(props) {
    const folderPath = props.path.slice(0, props.path.length - 1);
    const fileName = props.path[props.path.length - 1];
    const folderElems = folderPath.map(
        (elem, index) => FolderIndicator({ folderName: elem, key: index }),
    );
    return (
        <span className="pathIndicator">
            {folderElems}
            <FileIndicator fileName={fileName} />
        </span>
    );
}
