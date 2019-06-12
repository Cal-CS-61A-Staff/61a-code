import { spawn } from "child_process";
import * as temp from "temp";
import fs from "fs";
import { registerProcess } from "./processes";

import { err, exit, out } from "./communication";

export function runPyScript(key, scriptLocation, interpreterArgs, args) {
    const python = spawn("python", ["-u"].concat(interpreterArgs).concat([scriptLocation]).concat(args));
    registerProcess(key, python);
    python.stdout.on("data", data => out(key, data.toString("utf-8")));
    python.stderr.on("data", data => err(key, data.toString("utf-8")));
    python.on(
        "exit", (code, signal) => exit(key, `\nProcess finished with exit code ${code} (signal: ${signal})`),
    );
}

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
