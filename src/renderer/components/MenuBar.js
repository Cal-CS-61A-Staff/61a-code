import * as React from "react";
import {
    MENU_NEW, MENU_OPEN, MENU_SAVE, MENU_SAVE_AS,
} from "../../common/communicationEnums.js";
import MenuElem from "./MenuElem.js";

export default function MenuBar() {
    const menuOptions = [
        { code: MENU_NEW, name: "New", shortcut: [] },
        { code: MENU_OPEN, name: "Open", shortcut: [] },
        { code: MENU_SAVE, name: "Save", shortcut: [] },
        { code: MENU_SAVE_AS, name: "Save As", shortcut: [] },
    ];
    const menuElems = menuOptions.map(
        // eslint-disable-next-line react/no-array-index-key
        (elem, index) => <MenuElem key={index} {...elem} />,
    );
    return (
        <div className="menuBar">
            {menuElems}
        </div>
    );
}
