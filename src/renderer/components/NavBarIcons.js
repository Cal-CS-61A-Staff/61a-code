import React from "react";
import NavBarIcon from "./NavBarIcon";
import "../style/NavBarIcons.css";

export default function NavBarIcons(props) {
    const actions = ["Format", "Debug", "Run"];
    const icons = actions.map(action => (
        <NavBarIcon
            key={action}
            commandName={action}
            onActionClick={props.onActionClick}
        />
    ));
    return <span className="commandIcons">{icons}</span>;
}
