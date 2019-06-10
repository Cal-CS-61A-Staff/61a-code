import React from "react";

export default function FileIndicator(props) {
    return (
        <span>
            <button type="button">
                {props.fileName}
            </button>
        </span>
    );
}
