import React from "react";
import FileTree from "./FileTree.js";

export default function TreeFileSelector({ onFileSelect }) {
    return (
        <div className="modalCol">
            <div className="TreeFileSelector">
                <span className="browserFileSelector">Select Files</span>
                <FileTree onFileSelect={onFileSelect} />
            </div>
        </div>
    );
}
