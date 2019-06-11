import { sendNoInteract } from "../../../renderer/utils/communication";
import { GEN_PY_TRACE } from "../constants/communicationEnums";

const MAX_GLOBALS = 10;

// eslint-disable-next-line camelcase
export default async function generateDebugTrace(code, modules = {}, setup_code = "", working_directory = "") {
    const params = {
        code, modules, setup_code, working_directory,
    };

    const data = JSON.parse(await sendNoInteract({
        handler: "python",
        type: GEN_PY_TRACE,
        data: params,
    }));

    const globals = data.trace[data.trace.length - 1].ordered_globals;

    if (globals.length < MAX_GLOBALS) {
        return data;
    }

    const requiredGlobals = new Set();

    for (const point of data.trace) {
        for (const frame of point.stack_to_render) {
            requiredGlobals.add(frame.func_name);
            for (const local of frame.ordered_varnames) {
                requiredGlobals.add(local);
            }
        }
    }

    for (const point of data.trace) {
        const displayedGlobals = [];
        for (const global of globals) {
            if (requiredGlobals.has(global)) {
                displayedGlobals.push(global);
            }
        }
        point.ordered_globals = displayedGlobals;
    }

    data.filtered = true;

    return data;
}
