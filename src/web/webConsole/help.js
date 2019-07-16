import { checkArgs } from "./utils.js";

export default function help(args, workingDirectory, out) {
    checkArgs("help", args, 0, 0);
    out(`Use the following commands: 
ls     - Lists all files in current directory
cd     - Change to another directory
mkdir  - Create a new directory

edit   - Edit a file

python - Run the Python interpreter
scheme - Run the Scheme interpreter
sqlite - Run the SQL interpreter

verify  - Run OKPy in the current folder
submit  - Submit assignment
`);
}
