import { runPyScript } from "../../main/runPython.js";
import { GEN_PY_TRACE, RUN_BLACK } from "./constants/communicationEnums.js";

export function receive(arg) {
    if (arg.type === GEN_PY_TRACE) {
        runPyScript(arg.key, `${__dirname}/wrapper.py`, [], [JSON.stringify(arg.data)]);
    } else if (arg.type === RUN_BLACK) {
        runPyScript(arg.key, `${__dirname}/black`, [], ["--code", arg.code]);
    }
}
