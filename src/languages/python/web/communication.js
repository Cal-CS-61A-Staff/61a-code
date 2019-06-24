import $ from "jquery";
import {
    GEN_PY_TRACE, RUN_BLACK, RUN_PY_CODE,
} from "../constants/communicationEnums.js";
import { sendAndExit } from "../../../web/webBackend.js";
import { interactProcess } from "../../../main/processes.js";

import webConsole from "./web_console.py";
import runPyScript from "../../../web/runPython.js";

export default async function receive(arg) {
    if (arg.type === RUN_PY_CODE) {
        runPyCode(arg.key, arg.code);
    } else if (arg.type === GEN_PY_TRACE) {
        const ret = await $.post("./api/pytutor", {
            code: arg.data.setup_code + arg.data.code,
        });
        const parsed = JSON.parse(ret);
        parsed.code = { main_code: parsed.code };
        sendAndExit(arg.key, JSON.stringify(parsed));
    } else if (arg.type === RUN_BLACK) {
        // FIXME
        // eslint-disable-next-line no-alert
        alert("Unable to run BLACK at this time on the web!");
    }
}

function runPyCode(key, code) {
    runPyScript(key, webConsole, []);
    interactProcess(key, code);
}
