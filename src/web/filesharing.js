import { sendAndExit } from "./webBackend.js";
import ShareDialog from "../renderer/components/ShareDialog.js";
import { loadDialog } from "../renderer/utils/dialogWrap.js";

export default function showShareDialog(key) {
    loadDialog(ShareDialog, {
        onClose: () => {
            sendAndExit(key, { success: false });
        },
    });
}
