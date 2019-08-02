import { err, exit, out } from "./webBackend.js";
import { registerProcess } from "../main/processes.js";

const strBuffLen = 1024;

// https://developers.google.com/web/updates/2012/06/How-to-convert-ArrayBuffer-to-and-from-String
function str2ab(strBuff, str) {
    const bufView = new Uint16Array(strBuff);
    for (let i = 0; i !== strBuffLen; ++i) {
        bufView[i] = 0;
    }
    for (let i = 0, strLen = str.length; i < strLen - 1 && i < strBuffLen / 2; i++) {
        bufView[i] = str.charCodeAt(i);
    }
}


export default function runPyScript(key, script, args) {
    return new Promise((resolve) => {
        const worker = new Worker("pythonWorker.js");
        const commBuff = window.Atomics ? new window.SharedArrayBuffer(4) : null;
        const strBuff = window.Atomics ? new window.SharedArrayBuffer(strBuffLen) : null;
        worker.postMessage({
            code: script, transpiled: args.transpiled, commBuff, strBuff,
        });
        worker.onmessage = () => {
            worker.onmessage = (e) => {
                if (e.data.out) {
                    out(key, e.data.val);
                } else if (e.data.err) {
                    err(key, e.data.val);
                } else if (e.data.exit) {
                    exit(key, e.data.val);
                }
            };
            registerProcess(key, {
                stdin: {
                    write: (line) => {
                        str2ab(strBuff, line);
                        const arr = (new Int32Array(commBuff));
                        arr[0] = 1;
                        if (window.Atomics) {
                            window.Atomics.notify(arr, 0, 1);
                        }
                        worker.postMessage({ input: line });
                    },
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
