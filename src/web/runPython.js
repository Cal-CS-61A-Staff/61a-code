import { exit, out } from "./webBackend.js";
import { registerProcess } from "../main/processes.js";

// eslint-disable-next-line no-unused-vars
export default function runPyScript(key, script, args) {
    return new Promise((resolve) => {
        const worker = new Worker("pythonWorker.js");
        worker.postMessage({ code: script, transpiled: args.transpiled });
        worker.onmessage = () => {
            worker.onmessage = (e) => {
                out(key, e.data);
            };
            registerProcess(key, {
                stdin: {
                    write: line => worker.postMessage({ input: line }),
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
            resolve();
        };
    });
}
