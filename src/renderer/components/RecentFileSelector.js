/* eslint-disable react/no-array-index-key */
import React from "react";
import FileCard from "./FileCard.js";

export default function RecentFileSelector(props) {
    const cards = props.files.map((file, index) => (
        <FileCard
            key={index}
            file={file}
            onClick={() => props.onFileSelect(file)}
        />
    ));
    let content;
    if (props.files.length > 0) {
        content = (
            <>
            Recent files
                {cards}
            </>
        );
    } else {
        content = "No recent files.";
    }
    return (
        <div className="modalCol browserFileSelector">
            {content}
        </div>
    );
}
