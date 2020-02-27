import React from "react";
import "../style/fileIndicator.css";

export default function FileIndicator(props) {
    return (
        <span className="fileIndicator pathIndicatorElem">
            {" "}
            {props.fileName}
            {" "}
        </span>
    );
}
