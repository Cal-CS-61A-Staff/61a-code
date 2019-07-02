import $ from "jquery";
import { FORMAT, GEN_SCM_TRACE, RUN_SCM_CODE } from "../constants/communicationEnums.js";
import { err, exit, sendAndExit } from "../../../web/webBackend.js";
import { interactProcess } from "../../../main/processes.js";

// import webConsole from "./web_console.py";
import interpreter from "./IGNORE_needed.py";
// import transpiledInterpreter from "!!raw-loader!./IGNORE_scheme_transpiled.js";
import runPyScript from "../../../web/runPython.js";

export default async function receive(arg) {
    if (arg.type === RUN_SCM_CODE) {
        runScmCode(arg.key, arg.code);
    } else if (arg.type === GEN_SCM_TRACE) {
        const ret = await $.post("./api/pytutor", {
            code: arg.data.setup_code + arg.data.code,
        });
        const parsed = JSON.parse(ret);
        parsed.code = { main_code: parsed.code };
        sendAndExit(arg.key, JSON.stringify(parsed));
    } else if (arg.type === FORMAT) {
        const ret = await $.post("./api/scmFormat", { code: arg.code });
        if (ret.success) {
            sendAndExit(arg.key, ret.code);
        } else {
            err(arg.key, ret.error);
            exit(arg.key);
        }
    }
}

async function runScmCode(key, code) {
    await runPyScript(key, interpreter, []);
    // await runPyScript(key, transpiledInterpreter, { transpiled: true });
    interactProcess(key, code);
}
