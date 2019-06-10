import {
    RUN_PY_CODE,
    INTERACT_PROCESS,
    KILL_PROCESS,
    OUT,
    ERR,
    EXIT,
} from "../../common/communication_enums.js"

const { ipcRenderer } = require("electron");

const activeExecutions = {};
let nextKey = 0; // todo: make key allocation controlled by server to allow for multiple windows

const dummy = () => null;

export function run_py_code(code, onOutput, onErr, onHalt) {
    return send(
        { type: RUN_PY_CODE, code },
        onOutput,
        onErr,
        onHalt,
    );
}

function interact_process(key, line) {
    ipcRenderer.send("asynchronous-message", {
        type: INTERACT_PROCESS,
        key,
        line,
    });
}

export function send(message, onOutput, onErr, onHalt) {
    console.log(message);

    const key = nextKey++;

    ipcRenderer.send("asynchronous-message", { key, ...message });
    activeExecutions[key] = {
        onOutput: onOutput || dummy,
        onErr: onErr || dummy,
        onHalt: onHalt || dummy,
    };

    return [
        line => interact_process(key, line),
        () => kill_process(key),
        () => detach_handlers(key),
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

function kill_process(key) {
    ipcRenderer.send("asynchronous-message", { key, type: KILL_PROCESS });
}

function detach_handlers(key) {
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
        activeExecutions[arg.key].onHalt(arg.out);
        delete activeExecutions[arg.key];
    } else {
        console.log(arg);
    }
});
