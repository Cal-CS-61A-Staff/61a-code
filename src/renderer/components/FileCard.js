import React from "react";

export default function FileCard(props) {
    return (
        <div className="fileCard" onClick={props.onClick}>
            {props.file.location}
        </div>
    );
}
