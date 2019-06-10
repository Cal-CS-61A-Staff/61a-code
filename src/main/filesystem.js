import { dialog } from "electron";
import { basename } from "path";

import { readFile, writeFile } from "fs";
import { sendAndExit } from "./communication";

// todo: split into dialog + readFile functions
export function showOpenDialog(key) {
    dialog.showOpenDialog({}, (filePaths) => {
        if (filePaths) {
            readFile(filePaths[0], (error, data) => {
                if (error) {
                    sendAndExit(key, { success: false });
                } else {
                    const content = data.toString("utf-8");
                    sendAndExit(key, {
                        success: true,
                        file: {
                            name: basename(filePaths[0]),
                            location: filePaths[0],
                            content,
                        },
                    });
                }
            });
        } else {
            sendAndExit(key, { success: false });
        }
    });
}

export function showSaveDialog(key) {
    dialog.showSaveDialog({}, (location) => {
        if (location) {
            sendAndExit(key, { success: true, name: basename(location), location });
        } else {
            sendAndExit(key, { success: false });
        }
    });
}

export function save(key, contents, location) {
    writeFile(location, contents, (error) => {
        if (error) {
            sendAndExit(key, { success: false });
        } else {
            sendAndExit(key, { success: true });
        }
    });
}
