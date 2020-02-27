import React from "react";
import "../style/IntroButton.css";

export default function IntroButton(props) {
    return (
        <div className="introButton" onClick={props.onClick}>
            {props.name}
        </div>
    );
}
