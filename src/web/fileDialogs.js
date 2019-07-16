import path from "path-browserify";
import { sendAndExit } from "./webBackend.js";
import OpenDialog from "../renderer/components/OpenDialog.js";
import SaveDialog from "../renderer/components/SaveDialog.js";
import { closeDialog, loadDialog } from "../renderer/utils/dialogWrap.js";
import {
    FILE, getFile, getRecentFiles, normalize, storeFile,
} from "./filesystem.js";

export async function showOpenDialog(key) {
    function handleClose() {
        sendAndExit(key, { success: false });
    }

    function handleFileSelect(file) {
        closeDialog();
        sendAndExit(key, { success: true, file });
    }

    const recents = await getRecentFiles();

    loadDialog(OpenDialog, {
        recents,
        onClose: handleClose,
        onFileSelect: handleFileSelect,
    });
}

export async function open(key, location) {
    const file = await getFile(location);
    sendAndExit(key, { success: true, file });
}

export function showSaveDialog(key, contents, hint) {
    function handleClose() {
        sendAndExit(key, { success: false });
    }

    function handleNameSelect(name) {
        closeDialog();
        return save(key, contents, normalize(path.join("/home/", name)));
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

    loadDialog(SaveDialog, {
        defaultValue: hint,
        onClose: handleClose,
        onNameSelect: handleNameSelect,
        onDownloadClick: handleDownloadClick,
    });
}


export async function save(key, content, location) {
    await storeFile(content, normalize(location), FILE);
    sendAndExit(key, { success: true, name: path.basename(location), location });
}


export async function getRecents(key) {
    const out = await getRecentFiles();
    if (key) {
        sendAndExit(key, out);
    }
}
