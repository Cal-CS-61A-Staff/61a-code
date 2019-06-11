import React from "react";
import IntroButton from "./IntroButton";

export default function IntroBox(props) {
    return (
        <div className="introHolder">
            <div className="introTitle">61A Editor</div>
            <IntroButton name="Create new file" onClick={props.onCreateClick} />
            <IntroButton name="Open existing file" onClick={props.onOpenClick} />
        </div>
    );
}
