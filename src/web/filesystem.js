import React from "react";
import * as ReactDOM from "react-dom";
import { openDB } from "idb";
import { sendAndExit } from "./webBackend.js";
import OpenDialog from "../renderer/components/OpenDialog.js";
import SaveDialog from "../renderer/components/SaveDialog.js";

const DATABASE = "FileStorage";
const OBJECT_STORE = "Files";
const VERSION = 1;

export function showOpenDialog(key) {
    const elem = document.getElementById("modalOverlay");

    function handleClose() {
        ReactDOM.unmountComponentAtNode(elem);
        sendAndExit(key, { success: false });
    }

    function handleFileSelect(file) {
        ReactDOM.unmountComponentAtNode(elem);
        sendAndExit(key, { success: true, file });
    }

    ReactDOM.render(
        <OpenDialog
            onClose={handleClose}
            onFileSelect={handleFileSelect}
        />,
        elem,
    );
}

export function open(key, location) {
    readFile(location, (error, data) => {
        if (error) {
            sendAndExit(key, { success: false });
        } else {
            const content = data.toString("utf-8");
            sendAndExit(key, {
                success: true,
                file: {
                    name: basename(location),
                    location,
                    content,
                },
            });
        }
    });
}

export function showSaveDialog(key, contents) {
    const elem = document.getElementById("modalOverlay");

    function handleClose() {
        ReactDOM.unmountComponentAtNode(elem);
        sendAndExit(key, { success: false });
    }

    function handleNameSelect(name) {
        ReactDOM.unmountComponentAtNode(elem);
        return save(key, contents, name);
    }

    function handleDownloadClick() {
        alert("Not yet implemented!");
    }

    ReactDOM.render(
        <SaveDialog
            onClose={handleClose}
            onNameSelect={handleNameSelect}
            onDownloadClick={handleDownloadClick}
        />,
        elem,
    );
}

export async function save(key, contents, location) {
    try {
        const db = await openDB(DATABASE, VERSION, {
            upgrade(db) {
                db.createObjectStore(OBJECT_STORE, { keyPath: "location" });
                // who needs to preserve files anyway
            },
        });

        await db.put(OBJECT_STORE, { location, contents });

        sendAndExit(key, { success: true, name: location, location });
    } catch {
        alert("Unable to save! Make sure to grant this app access to IndexedDB");
        sendAndExit(key, { success: false });
    }
}
