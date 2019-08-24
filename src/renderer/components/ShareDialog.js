import React from "react";
import { dialogWrap } from "../utils/dialogWrap.js";

function ShareDialog(props) {
    const handleClick = () => {
        navigator.clipboard.writeText(props.link);
    };

    return (
        <div className="modalCol">
            <p> Share the following link with course staff to let us access your code. </p>
            <input className="fileNameField" value={props.link} />
            <button className="fileNameSubmitBtn" type="button" onClick={handleClick}> Copy </button>
            <p />
        </div>
    );
}

export default dialogWrap("Share", ShareDialog, "column");
