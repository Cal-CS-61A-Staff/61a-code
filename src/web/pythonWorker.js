import { join } from "path";

import pyConsole from "./web_console.py";

importScripts(join(__static, "brython/brython.js"));
importScripts(join(__static, "brython/brython_stdlib.js"));

onmessage = (e) => {
    const { data } = e;
    const { code } = data;
    handleInput(code);
};

let handler;

function initializePython() {
    self.stdin = { on: (pyHandler) => { handler = pyHandler; } };
    self.stdout = { write: val => postMessage(val) };
    self.stderr = { write: val => postMessage(val) };
    __BRYTHON__.brython();
    __BRYTHON__.run_script(pyConsole, "__main__", true);
}

function handleInput(code) {
    handler(code);
}

initializePython();
