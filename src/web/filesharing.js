import $ from "jquery";

import { sendAndExit } from "./webBackend.js";
import ShareDialog from "../renderer/components/ShareDialog.js";
import { loadDialog } from "../renderer/utils/dialogWrap.js";

export default async function showShareDialog(key, name, contents) {
    const fileData = { fileName: name, fileContent: contents };
    const link = await $.post("./api/share", fileData);
    loadDialog(ShareDialog, {
        onClose: () => {
            sendAndExit(key, { success: false });
        },
        fileData,
        link,
    });
}
