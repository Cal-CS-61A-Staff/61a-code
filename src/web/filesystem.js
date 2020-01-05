import $ from "jquery";

import { openDB } from "idb";
import path from "path-browserify";
import pathParse from "path-parse";

const DATABASE = "FileStorage";
const FILE_STORE = "Files";
const VERSION = 2;

export const FILE = "FILE";
export const DIRECTORY = "DIRECTORY";

async function getDB() {
    return openDB(DATABASE, VERSION, {
        async upgrade(db, oldVersion) {
            if (oldVersion < 1) {
                db.createObjectStore(FILE_STORE, { keyPath: "location", autoIncrement: true });
            } else if (oldVersion === 1) {
                db.deleteObjectStore(FILE_STORE);
                db.createObjectStore(FILE_STORE, { keyPath: "location", autoIncrement: true });
            }
            // who needs to preserve files anyway
        },
    });
}

export async function storeFile(content, location, type) {
    return storeFileWorker(await getDB(), content, location, type);
}

export async function getFile(location) {
    const db = await getDB();
    return db.get(FILE_STORE, normalize(location));
}

export async function removeFile(location) {
    const db = await getDB();
    await db.delete(FILE_STORE, location);
    const parDir = normalize(path.dirname(location));
    const enclosingDirectory = await db.get(FILE_STORE, parDir);
    enclosingDirectory.content.splice(enclosingDirectory.content.indexOf(location));
    await db.put(FILE_STORE, enclosingDirectory);
}

export async function getAssignments() {
    return (await $.post("/api/list_assignments")).data.assignments.filter(
        ({ name }) => ["hw", "lab", "proj", "challenge"].some(x => name.includes(x)),
    );
}

export async function getBackups(endpoint) {
    const backups = [];
    const assignment = endpoint.split("/").pop();
    const { data: { backups: ret } } = await $.post("/api/get_backups", { endpoint });
    for (const { messages } of ret) {
        for (const { created, contents, kind } of messages) {
            if (kind === "file_contents") {
                for (const [name, content] of Object.entries(contents)) {
                    if (name !== "submit") {
                        backups.push({
                            name,
                            location: `cs61a/${assignment}/${name}`,
                            content,
                            type: FILE,
                            time: Date.parse(created),
                        });
                    }
                }
            }
        }
    }
    return backups;
}

export async function getRecentFiles() {
    const db = await getDB();
    const raw = await db.getAll(FILE_STORE);
    return raw.filter(x => x.type === FILE).sort((a, b) => b.time - a.time);
}

export function normalize(location) {
    const parsed = pathParse(path.normalize(location));
    return path.format(parsed);
}


export async function fileExists(location) {
    return fileExistsWorker(await getDB(), location);
}

async function fileExistsWorker(db, location) {
    return (await db.get(FILE_STORE, location)) !== undefined;
}

async function addToDirectory(db, location, dirname) {
    const directory = await db.get(FILE_STORE, dirname);
    if (directory.type !== DIRECTORY) {
        throw Error("Path does not point to directory.");
    }
    if (!directory.content.includes(location)) {
        directory.content.push(location);
    }
    await db.put(FILE_STORE, directory);
}

async function storeFileWorker(db, content, location, type) {
    if (location !== "/") {
        if (!(await fileExistsWorker(db, path.dirname(location)))) {
            await storeFileWorker(db, [], path.dirname(location), DIRECTORY);
        }
        await addToDirectory(db, location, path.dirname(location));
    }
    await db.put(FILE_STORE, {
        name: path.basename(location), location, content, type, time: new Date().getTime(),
    });
}
