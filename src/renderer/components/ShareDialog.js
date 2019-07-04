import React from "react";
import { dialogWrap } from "../utils/dialogWrap.js";

function ShareDialog() {
    return (
        <div className="fileUploadButton">
            <span className="centeredTextHolder"> Or click here to select files. </span>
        </div>
    );
}

export default dialogWrap("Share", ShareDialog, "column");
