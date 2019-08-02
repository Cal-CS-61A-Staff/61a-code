import React from "react";
import { dialogWrap } from "../utils/dialogWrap.js";

function ShareDialog(props) {
    return (
        <div className="modalCol">
            <p> Share the following link with course staff to let us access your code. </p>
            {/* <p> It is always safe to post this link on Piazza publicly. </p> */}
            <input className="fileNameField" value={props.publicLink} />
            <button className="fileNameSubmitBtn" type="button"> Copy </button>

            <p />
            {/*<br />
            <p>
                Share the following link to let
                {" "}
                <b>ANYONE</b>
                {" "}
                access your code.
            </p>
            <p>
                If you are posting about HW / lab / project code,
                {" "}
                <b>DO NOT</b>
                {" "}
                share this link with other students.
            </p>
            <input className="fileNameField" value={props.privateLink} />
            <button className="fileNameSubmitBtn" type="button"> Copy </button> */}
        </div>
    );
}

export default dialogWrap("Share", ShareDialog, "column");
