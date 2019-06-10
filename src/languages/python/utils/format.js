import { RUN_BLACK } from "./common/communication_enums.js";
import { sendNoInteract } from "../communication.js";

export async function format(code) {
    return sendNoInteract({
        handler: "python",
        type: RUN_BLACK,
        code,
    });
}
