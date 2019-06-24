import React from "react";
import Editor from "./Editor";
import Output from "./Output";
import { sendNoInteract } from "../utils/communication.js";
import { SAVE_FILE, SHOW_SAVE_DIALOG } from "../../common/communicationEnums.js";
import { PYTHON, SCHEME, SQL } from "../../common/languages.js";
import {
    Debugger,
    format, generateDebugTrace, runCode, runFile,
} from "../utils/dispatch.js";

const DEBUG_MARKER = "DEBUG: ";
const EDITOR_MARKER = "EDITOR: ";

export default class File extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            name: this.props.initFile.name,
            editorText: this.props.initFile.content,
            savedText: this.props.initFile.location ? this.props.initFile.content : -1,
            location: this.props.initFile.location,

            outputData: [],
            outputActive: false,

            executedCode: [],

            debugData: null,
            editorInDebugMode: false,
            editorDebugData: null,

            interactCallback: null,
            killCallback: null,
            detachCallback: null,
        };

        this.editorRef = React.createRef();
        this.outputRef = React.createRef();
        this.debugRef = React.createRef();

        this.props.onActivate(this.props.id);
    }

    componentDidMount() {
        if (this.props.startInterpreter) {
            this.run();
        } else {
            this.editorRef.current.forceOpen();
        }
    }

    componentWillUnmount() {
        if (this.state.killCallback) {
            this.state.detachCallback();
            this.state.killCallback();
        }
    }

    run = async () => {
        if (this.state.location) {
            await this.save();
        }
        if (this.state.killCallback) {
            this.state.detachCallback();
            this.state.killCallback();
        }
        let interactCallback;
        let killCallback;
        let detachCallback;

        if (ELECTRON && this.state.location) {
            [interactCallback, killCallback, detachCallback] = runFile(this.identifyLanguage())(
                this.state.location,
                out => this.handleOutputUpdate(out, false),
                out => this.handleOutputUpdate(out, true),
                this.handleHalt,
            );
        } else {
            [interactCallback, killCallback, detachCallback] = runCode(this.identifyLanguage())(
                this.state.editorText,
                out => this.handleOutputUpdate(out, false),
                out => this.handleOutputUpdate(out, true),
                this.handleHalt,
            );
        }

        const numTrunc = this.state.outputData.length;

        this.setState(state => ({
            // eslint-disable-next-line react/no-access-state-in-setstate
            executedCode: [this.state.editorText],
            interactCallback,
            killCallback,
            detachCallback,
            outputData: state.outputData.slice(numTrunc),
            outputActive: true,
        }));

        this.outputRef.current.forceOpen();
    };

    debug = async (data) => {
        let debugData;
        if (data) {
            debugData = data; // data has been generated for us by parent
        } else if (this.state.editorText !== "") {
            debugData = await generateDebugTrace(this.identifyLanguage())(this.state.editorText);
        } else {
            this.debugExecutedCode();
            return;
        }
        this.setState({ debugData, editorInDebugMode: true });
        this.editorRef.current.forceOpen();
        this.debugRef.current.forceOpen();
    };

    debugExecutedCode = async () => {
        const TEMPLATE_CODE = "# these lines stub out the debugging functions you have available\n"
            + "def draw(): pass\n"
            + "def autodraw(): pass\n"
            + "def disableAutodraw(): pass\n"
            + "def visualize(): pass\n"
            + "def editor(): pass\n\n"
            + "# your code is below\n";
        const code = TEMPLATE_CODE + this.state.executedCode.join("\n");
        const debugData = await generateDebugTrace(this.identifyLanguage())(code);
        this.setState({ debugData, editorInDebugMode: true });
        this.debugRef.current.forceOpen();
    };

    format = async () => {
        // eslint-disable-next-line react/no-access-state-in-setstate
        const formatted = await format(this.identifyLanguage())(this.state.editorText);
        this.setState({ editorText: formatted });
    };

    save = async () => {
        if (!this.state.location) {
            await this.saveAs();
        } else {
            const savedText = this.state.editorText;
            const ret = await sendNoInteract({
                type: SAVE_FILE,
                contents: savedText,
                location: this.state.location,
            });
            if (ret.success) {
                this.setState({ savedText });
            }
        }
    };

    saveAs = async () => {
        const savedText = this.state.editorText;
        const ret = await sendNoInteract({
            type: SHOW_SAVE_DIALOG,
            contents: savedText,
            hint: this.state.name,
        });
        if (ret.success) {
            this.setState({
                name: ret.name,
                savedText,
                location: ret.location,
            });
        }
    };

    handleDebugUpdate = (editorDebugData) => {
        this.setState({ editorDebugData });
    };

    handleOutputUpdate = (text, isErr) => {
        if (text.startsWith(DEBUG_MARKER)) {
            this.debugExecutedCode();
        } else if (text.startsWith(EDITOR_MARKER)) {
            this.editorRef.current.forceOpen();
        } else {
            this.setState((state) => {
                const outputData = state.outputData.concat([{
                    text,
                    isErr,
                }]);
                return { outputData };
            });
        }
    };

    handleHalt = (text) => {
        this.handleOutputUpdate(text, true);
        this.setState({ outputActive: false });
    };

    handleStop = () => {
        this.state.killCallback();
    };

    handleActivate = () => {
        this.props.onActivate(this.props.id);
    };

    handleInput = (line) => {
        this.state.interactCallback(line);
        this.handleOutputUpdate(line, false);
        this.setState(state => ({ executedCode: state.executedCode.concat([line]) }));
    };

    handleEditorChange = (editorText) => {
        this.setState(state => ({
            editorText,
            editorInDebugMode: state.editorDebugData && state.editorDebugData.code === editorText,
        }));
        this.handleActivate();
    };

    identifyLanguage = () => {
        const name = this.state.name.toLowerCase();
        if (name.endsWith(".py")) {
            return PYTHON;
        } else if (name.endsWith(".scm")) {
            return SCHEME;
        } else if (name.endsWith(".sql")) {
            return SQL;
        } else {
            const code = this.state.editorText.toLowerCase();
            if (code.split("select").length > 1) {
                return SQL;
            } else if (code.split("def ") > 1) {
                return PYTHON;
            } else if (code.trim()[0] === "(" || code.split(";") > 1) {
                return SCHEME;
            } else {
                return PYTHON;
            }
        }
    };

    render() {
        const title = this.state.name + ((this.state.editorText === this.state.savedText) ? "" : "*");
        const editorDebugData = this.state.editorInDebugMode ? this.state.editorDebugData : null;
        const language = this.identifyLanguage();

        const CurrDebugger = Debugger(language);

        return (
            <>
                <Editor
                    ref={this.editorRef}
                    text={this.state.editorText}
                    language={language}
                    title={title}
                    onActivate={this.handleActivate}
                    onChange={this.handleEditorChange}
                    debugData={editorDebugData}
                />
                <Output
                    ref={this.outputRef}
                    title={`${this.state.name} (Output)`}
                    data={this.state.outputData}
                    outputActive={this.state.outputActive}
                    onStop={this.handleStop}
                    onRestart={this.run}
                    onInput={this.handleInput}
                />
                <CurrDebugger
                    ref={this.debugRef}
                    title={`${this.state.name} (Debug)`}
                    data={this.state.debugData}
                    onUpdate={this.handleDebugUpdate}
                />
            </>
        );
    }
}

// File.propTypes = {
//     id: PropTypes.object,
//     initFile: PropTypes.shape({
//         name: PropTypes.string,
//         content: PropTypes.string,
//         location: PropTypes.object,
//     }),
//     onActivate: PropTypes.func,
// };
