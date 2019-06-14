import { runPyCode, runPyScript } from "../../main/runPython.js";
import {
    GEN_PY_TRACE, RUN_BLACK, RUN_PY_FILE, RUN_PY_CODE,
} from "./constants/communicationEnums.js";

export default function receive(arg) {
    if (arg.type === RUN_PY_CODE) {
        runPyCode(arg.key, arg.code);
    } else if (arg.type === RUN_PY_FILE) {
        runPyScript(arg.key, arg.location, ["-i"], []);
    } else if (arg.type === GEN_PY_TRACE) {
        runPyScript(arg.key, `${__dirname}/wrapper.py`, [], [JSON.stringify(arg.data)]);
    } else if (arg.type === RUN_BLACK) {
        runPyScript(arg.key, `${__dirname}/black`, [], ["--code", arg.code]);
    }
}
