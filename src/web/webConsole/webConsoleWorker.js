import splitCommand from "./tokenize.js";
import help from "./help.js";

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

stdout(genPrompt());

const COMMANDS = {
    help,
};

onmessage = (e) => {
    const { data } = e;
    const { input } = data;
    let commandName;
    let args;
    try {
        [commandName, ...args] = splitCommand(input);
    } catch (err) {
        stderr(`Parse failed with error: ${err.message}\n`);
    }
    if (commandName) {
        const command = COMMANDS[commandName];
        if (command) {
            try {
                stdout(COMMANDS[commandName](args));
            } catch (err) {
                stderr(`${err.message}\n`);
            }
        } else {
            stderr(`Command ${commandName} was not found\n`);
        }
    }
    stdout(genPrompt());
};

function genPrompt() {
    return "rahularya@berkeley.edu ~ $ ";
}
