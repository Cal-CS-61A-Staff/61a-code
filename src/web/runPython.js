import startConsole from "./start_console.py";
import console from "./web_console.py";

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

function addPyScriptElem(id, script, web) {
    const elem = document.createElement("script");
    elem.innerHTML = script;
    elem.type = "text/python";
    elem.class = "webworker";
    elem.id = id;
    document.body.appendChild(elem);
}

export function runPyCode(key, code) {
    // const worker = new Worker("pythonWorker.js");
    // worker.postMessage({ code });
    // worker.onmessage = (e) => {
    //     console.log(e.data);
    // };
    addPyScriptElem("pyMain", startConsole);
    addPyScriptElem("pyWorker", console);
    brython();
}
