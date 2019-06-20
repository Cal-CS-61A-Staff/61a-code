import $ from "jquery";
import {
    GEN_PY_TRACE, RUN_BLACK, RUN_PY_FILE, RUN_PY_CODE,
} from "../constants/communicationEnums.js";
import { runPyCode } from "../../../web/runPython.js";
import { sendAndExit } from "../../../web/webBackend.js";

export default async function receive(arg) {
    if (arg.type === RUN_PY_CODE) {
        runPyCode(arg.key, arg.code);
    } else if (arg.type === RUN_PY_FILE) {
        runPyScript(arg.key, arg.location, ["-i"], []);
    } else if (arg.type === GEN_PY_TRACE) {
        const ret = await $.post("./api/pytutor", {
            code: arg.data.setup_code + arg.data.code,
        });
        const parsed = JSON.parse(ret);
        parsed.code = { main_code: parsed.code };
        sendAndExit(arg.key, JSON.stringify(parsed));
    } else if (arg.type === RUN_BLACK) {
        alert("Unable to run BLACK at this time on the web!");
    }
}
