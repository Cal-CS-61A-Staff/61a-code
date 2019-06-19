import { spawn } from "child_process";
import * as temp from "temp";

export function runPyScript(key, scriptLocation, interpreterArgs, args) {
    // const python = spawn("python3.6", ["-u"].concat(interpreterArgs).concat([scriptLocation]).concat(args));
    // registerProcess(key, python);

alert("doesn't work!!!");

    // python.stdout.on("data", data => out(key, data.toString("utf-8")));
    // python.stderr.on("data", data => err(key, data.toString("utf-8")));
    // python.on(
    //     "exit", (code, signal) => exit(key, `\nProcess finished with exit code ${code} (signal: ${signal})`),
    // );
}

export function runPyCode(key, code) {
        document.body.appendChild(codeElem);
}
