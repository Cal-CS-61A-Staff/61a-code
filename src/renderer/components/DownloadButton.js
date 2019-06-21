import React from "react";

export default function DownloadButton(props) {
    return (
        <div className="modalCol">
            <p>
                Or download a copy of your code to save on your computer.
            </p>
            <button
                className="fileDownloadBtn"
                type="button"
                onClick={props.onClick}
            >
                Download
            </button>
        </div>
    );
}
