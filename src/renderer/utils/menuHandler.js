// eslint-disable-next-line import/no-extraneous-dependencies
import { remote } from "electron";
import { send } from "./communication";
import { CLAIM_MENU } from "../../common/communicationEnums.js";

export default function claimMenu(handlers) {
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
