import React from "react";
import IntroButton from "./IntroButton";

export default function IntroBox(props) {
    return (
        <div className="introHolder">
            <div className="introTitle">61A Editor</div>
            <IntroButton name="Create new file" onClick={() => props.onCreateClick(false)} />
            <IntroButton name="Open existing file" onClick={props.onOpenClick} />
            <IntroButton name="Start Python interpreter" onClick={() => props.onCreateClick(true)} />
        </div>
    );
}
