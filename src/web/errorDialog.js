import ErrorDialog from "../renderer/components/ErrorDialog.js";
import { loadDialog } from "../renderer/utils/dialogWrap.js";

export default function showErrorDialog(title, content) {
    loadDialog(ErrorDialog, { title, content });
}
