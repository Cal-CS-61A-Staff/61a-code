import { join } from "path";
import execute, { init } from "./execution.js";

importScripts(join(__static, "./sql/sql.js"));

const launchText = `CS61A SQL Web Interpreter
--------------------------------------------------------------------------------
Welcome to the 61A SQL web interpreter!
Check out the code for this app on GitHub.

[Dotcommands involving the filesystem WILL crash the app!!!]
Type .help for instructions, or .read to load a file from your computer.
The tables used in homework, labs, and lecture are already available to use.
`;

function stdout(val) {
    postMessage({ out: true, val });
}

function stderr(val) {
    postMessage({ error: true, val });
}

// eslint-disable-next-line no-unused-vars
function exit(val) {
    postMessage({ exit: true, val });
}

let buff = "";

stdout(launchText);

init();

onmessage = async (e) => {
    const { data } = e;
    const { input } = data;
    buff += input;
    if (!input.trimEnd() || buff.trimEnd().endsWith(";") || input.startsWith(".")) {
        const ret = await execute(buff.trimEnd());
        for (const elem of ret) {
            stdout(elem);
            stdout("\n");
        }
        buff = "";
    }
    if (buff) {
        stderr("...> ");
    } else {
        stderr("sql> ");
    }
};
