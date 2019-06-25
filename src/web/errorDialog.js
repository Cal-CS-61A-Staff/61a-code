import React from "react";
import * as ReactDOM from "react-dom";
import ErrorDialog from "../renderer/components/ErrorDialog.js";

export default function showErrorDialog(title, message) {
    const elem = document.getElementById("modalOverlay");

    function handleClose() {
        ReactDOM.unmountComponentAtNode(elem);
    }

    ReactDOM.render(
        <ErrorDialog
            title={title}
            content={message}
            onClose={handleClose}
        />,
        elem,
    );
}
