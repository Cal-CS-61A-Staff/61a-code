import React from "react";
import * as ReactDOM from "react-dom";
import { openDB } from "idb";
import { sendAndExit } from "./webBackend.js";
import OpenDialog from "../renderer/components/OpenDialog.js";
import SaveDialog from "../renderer/components/SaveDialog.js";

const DATABASE = "FileStorage";
const OBJECT_STORE = "Files";
const VERSION = 1;

export async function showOpenDialog(key) {
    const elem = document.getElementById("modalOverlay");

    function handleClose() {
        ReactDOM.unmountComponentAtNode(elem);
        sendAndExit(key, { success: false });
    }

    function handleFileSelect(file) {
        ReactDOM.unmountComponentAtNode(elem);
        sendAndExit(key, { success: true, file });
    }

    const recents = await getRecentFiles();

    ReactDOM.render(
        <OpenDialog
            recents={recents}
            onClose={handleClose}
            onFileSelect={handleFileSelect}
        />,
        elem,
    );
}

export async function open(key, location) {
    const db = await getDB();
    const file = await db.get(OBJECT_STORE, location);
    sendAndExit(key, { success: true, file });
}

export function showSaveDialog(key, contents, hint) {
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
        // https://stackoverflow.com/questions/3665115/how-to-create-a-file-in-memory-for-user-to-download-but-not-through-server
        const element = document.createElement("a");
        element.setAttribute("href", `data:text/plain;charset=utf-8,${encodeURIComponent(contents)}`);
        element.setAttribute("download", hint);

        element.style.display = "none";
        document.body.appendChild(element);

        element.click();

        document.body.removeChild(element);
    }


    ReactDOM.render(
        <SaveDialog
            defaultValue={hint}
            onClose={handleClose}
            onNameSelect={handleNameSelect}
            onDownloadClick={handleDownloadClick}
        />,
        elem,
    );
}

async function getDB() {
    return openDB(DATABASE, VERSION, {
        upgrade(db) {
            db.createObjectStore(OBJECT_STORE, { keyPath: "location" });
            // who needs to preserve files anyway
        },
    });
}

export async function save(key, content, location) {
    const db = await getDB();
    await db.put(OBJECT_STORE, {
        name: location, location, content, time: new Date().getTime(),
    });
    sendAndExit(key, { success: true, name: location, location });
}

export async function getRecentFiles(key) {
    const db = await openDB(DATABASE, VERSION);
    const out = await db.getAll(OBJECT_STORE);
    out.sort((a, b) => b.time - a.time);
    if (key) {
        sendAndExit(key, out);
    }
    return out;
}
