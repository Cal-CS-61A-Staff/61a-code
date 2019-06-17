// eslint-disable-next-line import/no-extraneous-dependencies
import { send } from "./communication";
import { CLAIM_MENU } from "../../common/communicationEnums.js";

let remote;
if (ELECTRON) {
    ({ remote } = require("electron"));
}

export default function claimMenu(handlers) {
    if (!ELECTRON) {
        return () => null; // dummy function!
    }
    let detach;

    claim();

    function claim() {
        [, , detach] = send({ type: CLAIM_MENU },
            (option) => {
                if (!handlers[option]) {
                    console.error(option, "not available right now!");
                    return;
                }
                handlers[option]();
            });
    }

    remote.getCurrentWindow().on("focus", () => { detach(); claim(); });

    return () => {
        detach();
    };
}
