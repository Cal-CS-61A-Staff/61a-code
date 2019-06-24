import { exit, out } from "./webBackend.js";
import { registerProcess } from "../main/processes.js";

// eslint-disable-next-line no-unused-vars
export default function runPyScript(key, script, args) {
    const worker = new Worker("pythonWorker.js");
    worker.postMessage(script);
    worker.onmessage = (e) => {
        out(key, e.data);
    };
    registerProcess(key, {
        stdin: {
            write: line => worker.postMessage(line),
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
