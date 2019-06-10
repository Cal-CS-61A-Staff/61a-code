import temp from "temp";
import fs from "fs";
import {spawn} from "child_process";
import { registerProcess } from "./processes";


import { err, exit, out } from "./communication";

export function run_py_script(key, script_location, interpreter_args, args) {
    const python = spawn("python", ["-u"].concat(interpreter_args).concat([script_location]).concat(args));
    registerProcess(key, python);
    python.stdout.on("data", data => out(key, data.toString("utf-8")));
    python.stderr.on("data", data => err(key, data.toString("utf-8")));
    python.on(
        "exit", (code, signal) => exit(key, `\nProcess finished with exit code ${code} (signal: ${signal})`)
    );
}

export function run_py_code(key, code) {
    temp.open("pythonTempFile", (fail, info) => {
        if (!fail) {
            fs.write(info.fd, code, () => {
                fs.close(info.fd, () => null);
                run_py_script(key, info.path, ["-i"], []);
            });
        }
    });
}
