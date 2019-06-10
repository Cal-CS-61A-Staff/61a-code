import {send} from "./communication";
import {CLAIM_MENU} from "../../common/communication_enums.js";

export default function claimMenu(handlers) {
    const [, , detach] = send({type: CLAIM_MENU},
        (option) => {
            handlers[option]();
        }
    );
    return detach;
}
