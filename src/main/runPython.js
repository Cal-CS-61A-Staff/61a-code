import { spawn } from "child_process";
import * as temp from "temp";
import fs from "fs";
import { registerProcess } from "./processes";

import { err, exit, out } from "./communication";

export function runPyScript(key, scriptLocation, interpreterArgs, args) {
    const python = spawn("python", ["-u"].concat(interpreterArgs).concat([scriptLocation]).concat(args));
    registerProcess(key, python);
    // const bufferedOut = makeBuffer(x => out(key, x), 50, 500);
    // const bufferedErr = makeBuffer(x => err(key, x), 50, 500);

    python.stdout.on("data", data => out(key, data.toString("utf-8")));
    python.stderr.on("data", data => err(key, data.toString("utf-8")));
    python.on(
        "exit", (code, signal) => exit(key, `\nProcess finished with exit code ${code} (signal: ${signal})`),
    );
}

// function makeBuffer(f, limit, hardLimit) {
//     let cnt = 0;
//     let buff = [];
//     let timeoutActive = false;
//
//     return (data) => {
//         ++cnt;
//         if (cnt < limit) {
//             f(data); // ignore buffer
//         } else if (cnt < hardLimit) {
//             buff.push(data);
//             if (!timeoutActive) {
//                 timeoutActive = true;
//                 setTimeout(() => {
//                     timeoutActive = false;
//                     f(buff.join(""));
//                     buff = [];
//                 }, 500);
//             }
//         } else if (cnt === hardLimit) {
//             const stopMsg = "[Truncating stream]";
//             if (timeoutActive) {
//                 buff.push(stopMsg);
//             } else {
//                 f(stopMsg);
//             }
//         }
//     };
// }

export function runPyCode(key, code) {
    temp.open("pythonTempFile", (fail, info) => {
        if (!fail) {
            fs.write(info.fd, code, () => {
                fs.close(info.fd, () => null);
                runPyScript(key, info.path, ["-i"], []);
            });
        }
    });
}
