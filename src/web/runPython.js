import { exit, out } from "./webBackend.js";
import { registerProcess } from "../main/processes.js";

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
    const worker = new Worker("pythonWorker.js");
    worker.postMessage({ code });
    worker.onmessage = (e) => {
        out(key, e.data);
    };
    registerProcess(key, {
        stdin: {
            write: line => worker.postMessage({ code: line }),
        },
        kill: () => {
            try {
                worker.terminate();
            } catch {
                exit(key, "\n\nBrython web worker did not terminate correctly. "
                    + "You may want to refresh the page.");
                return;
            }
            exit(key, "\n\nBrython web worker terminated.");
        },
    });
}
