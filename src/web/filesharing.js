import $ from "jquery";

import { sendAndExit } from "./webBackend.js";
import ShareDialog from "../renderer/components/ShareDialog.js";
import { loadDialog } from "../renderer/utils/dialogWrap.js";

export default async function showShareDialog(key, name, contents) {
    const link = await $.post("./api/share", { fileName: name, fileContent: contents });
    loadDialog(ShareDialog, {
        onClose: () => {
            sendAndExit(key, { success: false });
        },
        link,
    });
}
