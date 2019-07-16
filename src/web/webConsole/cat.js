import { checkArgs, resolveRelativePath } from "./utils.js";
import { FILE, getFile } from "../filesystem.js";

export default async function cat(args, workingDirectory, out, err) {
    checkArgs("cat", args, 1, 1);
    const target = resolveRelativePath(args[0] || workingDirectory, workingDirectory);
    const file = await getFile(target);
    if (!file || file.type !== FILE) {
        err("File not found.");
        return 1;
    }
    out(file.content);
    return 0;
}
