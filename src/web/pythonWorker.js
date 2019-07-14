/* eslint-disable no-restricted-globals */
import { join } from "path";

self.window = self;

importScripts(join(__static, "brython/brython.js"));
importScripts(join(__static, "brython/brython_stdlib.js"));

let code = false;
let commBuff;
let strBuff;

onmessage = async (e) => {
    const { data } = e;
    if (code) {
        handleInput(data.input);
    } else {
        ({ code, commBuff, strBuff } = data);
        const { transpiled } = data;
        initialize();
        await doBackgroundTasks();
        if (transpiled) {
            initializeTranspiledJS();
        } else {
            initializePython();
        }
    }
};

function doBackgroundTasks() {
    return new Promise((resolve) => {
        setTimeout(resolve, 0);
    });
}

// https://developers.google.com/web/updates/2012/06/How-to-convert-ArrayBuffer-to-and-from-String
function ab2str(buf) {
    return String.fromCharCode.apply(null, new Uint16Array(buf));
}

function blockingInput() {
    const arr = new Int32Array(commBuff);
    // eslint-disable-next-line no-undef
    Atomics.wait(arr, 0, 0);
    arr[0] = 0;
    return ab2str(strBuff);
}

let handler;

function initialize() {
    self.stdin = {
        on: (pyHandler) => {
            handler = pyHandler;
            postMessage("ready!");
        },
    };
    self.stdout = { write: val => postMessage({ out: true, val }) };
    self.stderr = { write: val => postMessage({ err: true, val }) };
    self.exit = { write: val => postMessage({ exit: true, val }) };
    self.blockingInput = { wait: blockingInput };
    __BRYTHON__.brython();
    __BRYTHON__.idb_open();
    __BRYTHON__.brython_path = "./static/brython/";
}

function initializePython() {
    console.log(__BRYTHON__.python_to_js(code)); // TODO: DISABLE!!!
    __BRYTHON__.run_script(code, "__main__", true);
}

function initializeTranspiledJS() {
    // eslint-disable-next-line no-eval
    (0, eval)(code);
}

function handleInput(data) {
    const arr = new Int32Array(commBuff);
    if (arr[0] !== 0) {
        arr[0] = 0;
        handler(data);
    }
}
