import { send } from "./communication";
import { CLAIM_MENU } from "../../common/communicationEnums.js";

export default function claimMenu(handlers) {
    const [, , detach] = send({ type: CLAIM_MENU },
        (option) => {
            handlers[option]();
        });
    return detach;
}
