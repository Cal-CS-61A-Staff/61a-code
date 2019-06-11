import { RUN_BLACK } from "../constants/communicationEnums.js";
import { sendNoInteract } from "../../../renderer/utils/communication.js";

export default async function format(code) {
    const out = await sendNoInteract({
        handler: "python",
        type: RUN_BLACK,
        code,
    });
    return out.substr(0, out.length - 1);
}
