import { FORMAT } from "../constants/communicationEnums.js";
import { sendNoInteract } from "../../../renderer/utils/communication.js";
import { SCHEME } from "../../../common/languages.js";

export default async function format(code) {
    const out = await sendNoInteract({
        handler: SCHEME,
        type: FORMAT,
        code,
    });
    return out.substr(0, out.length - 1);
}
