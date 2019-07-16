import splitCommand from "./tokenize.js";
import help from "./help.js";
import ls from "./ls.js";
import cd from "./cd.js";

let location = "~";

// eslint-disable-next-line
export function changeDirectory(newLocation) {
    if (newLocation.startsWith("/home/")) {
        location = newLocation.slice(6);
    } else {
        location = newLocation;
    }
}

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
    help, ls, cd,
};

onmessage = async (e) => {
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
                await COMMANDS[commandName](args, location, stdout, stderr);
            } catch (err) {
                stderr(`${err.message}\n`);
            }
        } else {
            stderr(`Command ${commandName} was not found\n`);
        }
    }
    stdout("\n");
    stdout(genPrompt());
};

function genPrompt() {
    return `rahularya@berkeley.edu ${location} $ `;
}
