/* eslint-disable react/no-array-index-key */
import React from "react";
import FileCard from "./FileCard.js";

export default function BrowserFileSelector(props) {
    const cards = props.files.map((file, index) => (
        <FileCard
            key={index}
            file={file}
            onClick={() => props.onFileSelect(file)}
        />
    ));
    return (
        <div className="modalCol browserFileSelector">
            Recent files
            {cards}
        </div>
    );
}
