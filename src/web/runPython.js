import { err, out } from "./webBackend.js";

export function runPyScript(key, scriptLocation, interpreterArgs, args) {
    // const python = spawn("python3.6", ["-u"].concat(interpreterArgs).concat([scriptLocation]).concat(args));
    // registerProcess(key, python);

    alert("doesn't work!!!");

    // python.stdout.on("data", data => out(key, data.toString("utf-8")));
    // python.stderr.on("data", data => err(key, data.toString("utf-8")));
    // python.on(
    //     "exit", (code, signal) => exit(key, `\nProcess finished with exit code ${code} (signal: ${signal})`),
    // );
}

function randomID() {
    return Math.random().toString(36).replace(/[^a-z]+/g, "").substr(2, 10);
}

function interceptWrite(handler) {
    const id = randomID();
    window[id] = {
        write: handler,
    };
    return id;
}

export function runPyCode(key, code) {
    const stdout = interceptWrite(data => out(key, data));
    const stderr = interceptWrite(data => err(key, data));
    const realCode = `
import sys
import browser

class Stream:
    def __init__(self, obj):
        self.obj = obj
    def write(self, raw):
        self.obj.write(raw)

sys.stdout = Stream(browser.window.${stdout})
sys.stderr = Stream(browser.window.${stderr})

${code}`;
    const js = __BRYTHON__.python_to_js(realCode);
    console.log(js);
    brython();
    try {
        (1, eval)(js); // FIXME: NO!
    } catch (err) {
        console.error(err);
    }
}
