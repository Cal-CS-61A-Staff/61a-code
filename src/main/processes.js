let processes = {};

export function registerProcess(key, process) {
    processes[key] = process;
}

export function getProcess(key) {
    return processes[key];
}

export function interactProcess(key, line) {
    getProcess(key).stdin.write(line, "utf-8");
}

export function killProcess(key) {
    getProcess(key).kill();
}
