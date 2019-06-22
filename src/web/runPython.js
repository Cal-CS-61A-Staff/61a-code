import { exit, out } from "./webBackend.js";
import { registerProcess } from "../main/processes.js";

// eslint-disable-next-line no-unused-vars
export function runPyScript(key, scriptLocation, interpreterArgs, args) {
    // TODO
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
