/* eslint-disable no-restricted-globals */
import { join } from "path";

importScripts(join(__static, "brython/brython.js"));
importScripts(join(__static, "brython/brython_stdlib.js"));

let pyCode = false;

onmessage = (e) => {
    const { data } = e;
    if (pyCode) {
        handleInput(data);
    } else {
        pyCode = data;
        initializePython();
    }
};

let handler;

function initializePython() {
    self.stdin = { on: (pyHandler) => { handler = pyHandler; } };
    self.stdout = { write: val => postMessage(val) };
    self.stderr = { write: val => postMessage(val) };
    __BRYTHON__.brython();
    __BRYTHON__.run_script(pyCode, "__main__", true);
}

function handleInput(data) {
    handler(data);
}
