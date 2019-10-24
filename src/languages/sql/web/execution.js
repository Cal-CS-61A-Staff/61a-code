import $ from "jquery";
import visualize from "./visualize.js";
import { tableFormat } from "./utils.js";
import preexisting from "./default_tables.js";

let sql;
let db;

export function init() {
    sql = SQL;
    db = newDatabase();
}

function newDatabase() {
    const newDb = new sql.Database();
    try {
        newDb.exec(preexisting);
    } catch (err) {
        // pass
    }
    return newDb;
}

export default async function execute(command) {
    if (command.startsWith(".")) {
        if (command.split(" ").length > 1) {
            return [`${command.split(" ")[0]} takes no arguments, on the web interpreter.`];
        }
        // dotcommand
        if (command === ".quit" || command === ".exit") {
            // TODO: Implement .quit
            return [];
        } else if (command === ".help") {
            return [
                ".exit                  Exit this program\n"
                + ".help                  Show this message\n"
                + ".quit                  Exit this program\n"
                + ".open                  Close existing database and reopen file to be selected\n"
                + ".read                  Execute SQL in file to be selected\n"
                + ".tables                List names of tables\n"
                + ".schema                Show all CREATE statements",
            ];
        } else if (command === ".open") {
            db = newDatabase();
            return execute(".read");
        } else if (command === ".read") {
            return new Promise((resolve) => {
                $("<input type=\"file\" />").click().on("change", (e) => {
                    const file = e.target.files[0];
                    const reader = new FileReader();
                    reader.readAsText(file);
                    reader.onload = () => {
                        resolve([reader.result, execute(reader.result, db)]);
                    };
                });
            });
        } else if (command === ".tables") {
            const dbRet = db.exec("SELECT name as Tables FROM sqlite_master WHERE type = 'table';");
            return [tableFormat(dbRet[0])];
        } else if (command === ".schema") {
            const dbRet = db.exec("SELECT (sql || ';') as `CREATE Statements` FROM sqlite_master WHERE type = 'table';");
            return [tableFormat(dbRet[0])];
        } else {
            return [`The command ${command.split(" ")[0]} does not exist.`];
        }
    }

    let dbRet;
    try {
        dbRet = db.exec(command);
    } catch (err) {
        return [`<span style="color: red">Error: ${err.message}</span>`];
    }

    let visualization;
    try {
        visualization = visualize(command, db);
    } catch (err) {
        console.log(err);
    }

    const out = [];

    for (const table of dbRet) {
        out.push(tableFormat(table));
    }

    // if (visualization) {
    //     const visualizeButton = document.createElement("BUTTON");
    //     $(visualizeButton).addClass("btn btn-info btn-sm");
    //     visualizeButton.innerHTML = "Visualize";
    //     out.push(visualizeButton);
    //
    //     const visualizePane = document.createElement("DIV");
    //     $(visualizePane).addClass("card");
    //     const visualizePaneHeader = document.createElement("DIV");
    //     $(visualizePaneHeader).addClass("card-header");
    //     const innerVisualizePane = document.createElement("DIV");
    //     $(innerVisualizePane).addClass("card-body");
    //
    //     const firstButton = document.createElement("BUTTON");
    //     firstButton.innerHTML = "&lt;&lt;";
    //     $(firstButton).addClass("btn btn-secondary");
    //
    //     const prevButton = document.createElement("BUTTON");
    //     prevButton.innerHTML = "&lt;";
    //     $(prevButton).addClass("btn btn-secondary");
    //
    //     const nextButton = document.createElement("BUTTON");
    //     nextButton.innerHTML = "&gt;";
    //     $(nextButton).addClass("btn btn-secondary");
    //
    //     const lastButton = document.createElement("BUTTON");
    //     lastButton.innerHTML = "&gt;&gt;";
    //     $(lastButton).addClass("btn btn-secondary");
    //
    //     const buttons = document.createElement("DIV");
    //     $(buttons).addClass("btn-group  btn-group-sm visButtons");
    //     $(buttons).append(firstButton).append(prevButton).append(nextButton)
    //         .append(lastButton);
    //
    //     const closeVisualizeButton = document.createElement("BUTTON");
    //     closeVisualizeButton.innerHTML = "Hide Visualization";
    //     $(closeVisualizeButton).addClass("btn btn-info btn-sm");
    //
    //     $(visualizePaneHeader).append(buttons).append(closeVisualizeButton);
    //     $(visualizePane).append(visualizePaneHeader);
    //
    //     const tableRenderArea = document.createElement("DIV");
    //     $(innerVisualizePane).append(tableRenderArea);
    //
    //     $(visualizePane).append(innerVisualizePane);
    //     $(visualizePane).hide();
    //
    //     out.push(visualizePane);
    //
    //     let i = 0;
    //     $(visualizeButton).click(() => {
    //         [tableRenderArea.innerHTML] = visualization;
    //         $(visualizeButton).hide();
    //         $(nextButton).show();
    //         $(prevButton).show();
    //         $(visualizePane).show();
    //     });
    //     $(firstButton).click(() => {
    //         i = 0;
    //         tableRenderArea.innerHTML = visualization[i];
    //     });
    //     $(prevButton).click(() => {
    //         i = Math.max(i - 1, 0);
    //         tableRenderArea.innerHTML = visualization[i];
    //     });
    //     $(nextButton).click(() => {
    //         i = Math.min(i + 1, visualization.length - 1);
    //         tableRenderArea.innerHTML = visualization[i];
    //     });
    //     $(lastButton).click(() => {
    //         i = visualization.length - 1;
    //         tableRenderArea.innerHTML = visualization[i];
    //     });
    //     $(closeVisualizeButton).click(() => {
    //         $(visualizePane).hide();
    //         $(visualizeButton).show();
    //         i = 0;
    //         tableRenderArea.innerHTML = visualization[i];
    //     });
    // }

    if (visualization) {
        return { out, visualization };
    } else {
        return out;
    }
}
