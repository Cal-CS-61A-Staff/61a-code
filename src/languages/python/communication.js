import {run_py_script} from "../../main/run_python.js";
import {GEN_PY_TRACE, RUN_BLACK} from "./constants/communicationEnums.js";

export function receive(arg) {
    if (arg.type === GEN_PY_TRACE) {
        run_py_script(arg.key, `${__dirname}/wrapper.py`, [], [JSON.stringify(arg.data)]);
    } else if (arg.type === RUN_BLACK) {
        run_py_script(arg.key, `${__dirname}/black`, [], ["--code", arg.code]);
    }
}
