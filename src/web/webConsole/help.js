import { checkArgs } from "./utils.js";

export default function help(args) {
    checkArgs("help", args, 0, 0);
    return `
Use the following commands:
ls -         
    `;
}
