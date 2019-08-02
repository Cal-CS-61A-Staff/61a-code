import * as React from "react";
import {
    MENU_NEW, MENU_OPEN, MENU_NEW_CONSOLE, MENU_SAVE, MENU_SAVE_AS, MENU_SHARE
} from "../../common/communicationEnums.js";
import MenuElem from "./MenuElem.js";

export default function MenuBar() {
    const menuOptions = [
        { code: MENU_NEW, name: "New", shortcut: "mod+n" },
        { code: MENU_OPEN, name: "Open", shortcut: "mod+o" },
        { code: MENU_NEW_CONSOLE, name: "Console", shortcut: "mod+shift+c" },
        { code: MENU_SAVE, name: "Save", shortcut: "mod+s" },
        { code: MENU_SAVE_AS, name: "Save As", shortcut: "mod+shift+s" },
        { code: MENU_SHARE, name: "Share", shortcut: "mod+shift+option+s" },
    ];
    const menuElems = menuOptions.map(
        // eslint-disable-next-line react/no-array-index-key
        (elem, index) => <MenuElem key={index} flexBasis={60} {...elem} />,
    );
    return (
        <div className="menuBar">
            {menuElems}
        </div>
    );
}
