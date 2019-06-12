import { PYTHON, SCHEME } from "../../common/languages.js";
import pyFormat from "../../languages/python/utils/format.js";
import scmFormat from "../../languages/scheme/utils/format.js";
import pyGenerateDebugTrace from "../../languages/python/utils/generateDebugTrace.js";
import { runPyCode, runPyFile } from "../../languages/python/utils/run.js";
import { runScmCode, runScmFile } from "../../languages/scheme/utils/run.js";

export function format(language) {
    const options = {
        [PYTHON]: pyFormat,
        [SCHEME]: scmFormat,
    };
    return options[language];
}

export function generateDebugTrace(language) {
    const options = {
        [PYTHON]: pyGenerateDebugTrace,
    };
    return options[language];
}

export function runCode(language) {
    const options = {
        [PYTHON]: runPyCode,
        [SCHEME]: runScmCode,
    };
    return options[language];
}

export function runFile(language) {
    const options = {
        [PYTHON]: runPyFile,
        [SCHEME]: runScmFile,
    };
    return options[language];
}
