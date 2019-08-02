import * as React from "react";
import StdoutElem from "./StdoutElem.js";
import OutputDrawElem from "./OutputDrawElem.js";

const DRAW_MARKER = "DRAW: ";

export default function OutputElem(props) {
    if (props.text.startsWith(DRAW_MARKER)) {
        try {
            return <OutputDrawElem data={JSON.parse(props.text.substr(DRAW_MARKER.length))} />;
        } catch (e) {
            throw e;
        }
    }
    // eslint-disable-next-line no-underscore-dangle
    if (props.text.__html) {
        // eslint-disable-next-line react/no-danger
        return <div dangerouslySetInnerHTML={props.text} />;
    }
    return <StdoutElem text={props.text} lang={props.lang} type={props.type} />;
}
