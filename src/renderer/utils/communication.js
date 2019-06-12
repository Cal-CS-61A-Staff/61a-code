import {
    ERR, EXIT, INTERACT_PROCESS, KILL_PROCESS, OUT, REQUEST_KEY,
} from "../../common/communicationEnums.js";

// eslint-disable-next-line
const { ipcRenderer } = require("electron");

const activeExecutions = {};

const dummy = () => null;

function interactProcess(key, line) {
    ipcRenderer.send("asynchronous-message", {
        type: INTERACT_PROCESS,
        key,
        line,
    });
}

function requestKey() {
    return ipcRenderer.sendSync("synchronous-message", REQUEST_KEY);
}

export function send(message, onOutput, onErr, onHalt) {
    console.log(message);

    const key = requestKey();

    ipcRenderer.send("asynchronous-message", { key, ...message });
    activeExecutions[key] = {
        onOutput: onOutput || dummy,
        onErr: onErr || dummy,
        onHalt: onHalt || dummy,
    };

    return [
        line => interactProcess(key, line),
        () => killProcess(key),
        () => detachHandlers(key),
    ];
}

export function sendNoInteract(message) {
    return new Promise((resolve, reject) => {
        let out = null;
        send(message, (val) => {
            if (out) {
                out += val;
            } else {
                out = val;
            }
        }, (arg) => {
            console.error(arg);
            reject(arg);
        }, () => resolve(out));
    });
}

function killProcess(key) {
    ipcRenderer.send("asynchronous-message", { key, type: KILL_PROCESS });
}

function detachHandlers(key) {
    if (activeExecutions[key]) {
        activeExecutions[key] = {
            onOutput: dummy,
            onErr: dummy,
            onHalt: dummy,
        };
    }
}

ipcRenderer.on("asynchronous-reply", (event, arg) => {
    if (arg.type === OUT) {
        activeExecutions[arg.key].onOutput(arg.out);
    } else if (arg.type === ERR) {
        activeExecutions[arg.key].onErr(arg.out);
    } else if (arg.type === EXIT) {
        if (!activeExecutions[arg.key]) {
            // key from previous window, is now dead :P
            return;
        }
        activeExecutions[arg.key].onHalt(arg.out);
        delete activeExecutions[arg.key];
    } else {
        console.log(arg);
    }
});
