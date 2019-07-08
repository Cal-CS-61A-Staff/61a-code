import * as React from "react";
import { dialogWrap } from "../utils/dialogWrap.js";

class ErrorDialog extends React.Component {
    render() {
        return this.props.content;
    }
}

export default dialogWrap("Error", ErrorDialog, "row");
