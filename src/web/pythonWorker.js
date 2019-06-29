/* eslint-disable no-restricted-globals */
import { join } from "path";

self.window = self;

console.log(self.indexedDB);

importScripts(join(__static, "brython/brython.js"));
importScripts(join(__static, "brython/brython_stdlib.js"));

let code = false;

onmessage = async (e) => {
    const { data } = e;
    if (code) {
        handleInput(data.input);
    } else {
        ({ code } = data);
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

let handler;

function initialize() {
    self.stdin = {
        on: (pyHandler) => {
            handler = pyHandler;
            postMessage("ready!");
        },
    };
    self.stdout = { write: val => postMessage(val) };
    self.stderr = { write: val => postMessage(val) };
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
    handler(data);
}
