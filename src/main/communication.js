// eslint-disable-next-line import/no-extraneous-dependencies
import { ipcMain } from "electron";

import { runPyCode } from "./runPython";
import { interactProcess, killProcess } from "./processes";
import { save, showOpenDialog, showSaveDialog } from "./filesystem";
import {
    INTERACT_PROCESS,
    KILL_PROCESS,
    RUN_PY_CODE,
    SHOW_OPEN_DIALOG,
    SHOW_SAVE_DIALOG,
    OUT,
    ERR,
    EXIT,
    CLAIM_MENU,
    SAVE_FILE,
    REGISTER_OKPY_HANDLER,
} from "../common/communication_enums.js";

import * as python from "../languages/python/communication";
import { assignMenuKey } from "./initializeMenu";
import { registerOKPyHandler } from "./ok_interface";

let commonEvent;

export function addHandlers() {
    ipcMain.on("asynchronous-message", (event, arg) => {
        if (!commonEvent) {
            commonEvent = event;
        }
        receive(arg);
    });
}

function receive(arg) {
    console.log("Receive", arg);
    if (!arg.handler) {
        // main server handler
        if (arg.type === RUN_PY_CODE) {
            runPyCode(arg.key, arg.code);
        } else if (arg.type === INTERACT_PROCESS) {
            interactProcess(arg.key, arg.line);
        } else if (arg.type === KILL_PROCESS) {
            killProcess(arg.key);
        } else if (arg.type === SHOW_OPEN_DIALOG) {
            showOpenDialog(arg.key);
        } else if (arg.type === SHOW_SAVE_DIALOG) {
            showSaveDialog(arg.key);
        } else if (arg.type === CLAIM_MENU) {
            assignMenuKey(arg.key);
        } else if (arg.type === SAVE_FILE) {
            save(arg.key, arg.contents, arg.location);
        } else if (arg.type === REGISTER_OKPY_HANDLER) {
            registerOKPyHandler(arg.key, arg.fileName);
        } else {
            console.error(`Unknown (or missing) type: ${arg.type}`);
        }
    } else if (arg.handler === "python") {
        python.receive(arg);
    } else {
        console.error(`Unknown handler: ${arg.handler}`);
    }
}

export function send(arg) {
    console.log("Send", arg);
    commonEvent.sender.send("asynchronous-reply", arg);
}

export function out(key, val) {
    send({ key, type: OUT, out: val });
}

export function err(key, val) {
    send({ key, type: ERR, out: val });
}

export function exit(key, val) {
    send({ key, type: EXIT, out: val });
}

export function sendAndExit(key, msg) {
    out(key, msg);
    exit(key);
}
