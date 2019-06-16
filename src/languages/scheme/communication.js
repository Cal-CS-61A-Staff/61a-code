import * as temp from "temp";
import fs from "fs";
import { runPyScript } from "../../main/runPython.js";
import { FORMAT, RUN_SCM_CODE, RUN_SCM_FILE } from "./constants/communicationEnums.js";

export default function receive(arg) {
    if (arg.type === RUN_SCM_CODE) {
        runScmCode(arg.key, arg.code);
    } else if (arg.type === RUN_SCM_FILE) {
        runPyScript(arg.key, `${__static}/scheme/scheme`, [], [arg.location, "-i"]);
    } else if (arg.type === FORMAT) {
        scmFormat(arg.key, arg.code);
    }
}

function runScmCode(key, code) {
    temp.open("scmTempFile", (fail, info) => {
        if (!fail) {
            fs.write(info.fd, code, () => {
                fs.close(info.fd, () => null);
                runPyScript(key, `${__static}/scheme/scheme`, [], [info.path, "-i"]);
            });
        }
    });
}

function scmFormat(key, code) {
    temp.open("scmTempFile", (fail, info) => {
        if (!fail) {
            fs.write(info.fd, code, () => {
                fs.close(info.fd, () => null);
                runPyScript(key, `${__static}/scheme/formatter`, [], ["--reformat", info.path]);
            });
        }
    });
}
