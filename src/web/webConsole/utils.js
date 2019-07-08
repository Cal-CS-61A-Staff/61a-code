// eslint-disable-next-line import/prefer-default-export
export function checkArgs(func, args, low, high) {
    if (low === high) {
        if (args.length !== low) {
            throw Error(`${func} expects ${low} arguments, received ${args.length}.`);
        }
    } else if (args.length < low || args.length > high) {
        throw Error(`${func} expects between ${low} and ${high} arguments, received ${args.length}.`);
    }
}
