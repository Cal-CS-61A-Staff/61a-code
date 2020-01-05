import React from "react";
import {
    GET_RECENT_FILES,
    MENU_CLOSE_TAB, MENU_HELP, MENU_LOGIN, MENU_LOGOUT,
    MENU_NEW,
    MENU_OPEN, SHOW_OK_BACKUPS_DIALOG,
    SHOW_OPEN_DIALOG,
} from "../../common/communicationEnums.js";
import IntroBox from "./IntroBox";
import { sendNoInteract } from "../utils/communication.js";
import { useMenu } from "../utils/menuHandler.js";
import { openHelp } from "../utils/help.js";
import { login, logout } from "../utils/auth.js";
import ModalButton from "./ModalButton.js";
import { useAuthData } from "../utils/okUtils.js";
import { useAsync } from "../utils/hooks.js";
import RecentFileSelector from "./RecentFileSelector.js";

function closeTab() {
    if (ELECTRON) {
        // eslint-disable-next-line global-require
        const { remote } = require("electron");
        remote.getCurrentWindow().close();
    }
}

export default function LaunchScreen({ onFileCreate }) {
    const { loggedOut } = useAuthData();

    const handleCreateClick = (extension) => {
        const realExtension = extension || "";
        const file = {
            name: `untitled${realExtension}`,
            location: null,
            content: "",
        };
        onFileCreate(file, Boolean(realExtension));
    };

    const handleOpenClick = async () => {
        const ret = await sendNoInteract({
            type: SHOW_OPEN_DIALOG,
        });
        if (ret.success) {
            onFileCreate(ret.file);
        }
    };

    const handleBackupsClick = async () => {
        if (loggedOut) {
            login();
        } else {
            const ret = await sendNoInteract({ type: SHOW_OK_BACKUPS_DIALOG });
            if (ret.success) {
                onFileCreate(ret.file);
            }
        }
    };

    const recentFiles = useAsync(
        () => sendNoInteract({ type: GET_RECENT_FILES }),
        [],
    );

    useMenu({
        [MENU_NEW]: handleCreateClick,
        [MENU_OPEN]: handleOpenClick,
        [MENU_CLOSE_TAB]: closeTab,
        [MENU_HELP]: openHelp,
        [MENU_LOGIN]: login,
        [MENU_LOGOUT]: logout,
    });

    const okButtonText = `${loggedOut ? "Login" : "Click"} to view backups`;

    return (
        <div className="row">
            <div className="introColumn">
                <IntroBox
                    onCreateClick={handleCreateClick}
                    onOpenClick={handleOpenClick}
                />
            </div>
            <div className="recentColumn">
                <div className="recentHolder browserFileSelector">
                    <RecentFileSelector
                        files={recentFiles}
                        onFileSelect={onFileCreate}
                    />
                    <br />
                    <ModalButton buttonText={okButtonText} onClick={handleBackupsClick}>
                        <div className="LaunchScreenHeader">OKPy Backups</div>
                    </ModalButton>
                </div>
            </div>
        </div>
    );
}
