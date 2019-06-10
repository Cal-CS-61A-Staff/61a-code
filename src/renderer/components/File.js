import React from "react";
import Editor from "./Editor";
import Output from "./Output";
import Debugger from "./Debugger";
import generateDebugTrace from "../../languages/python/utils/generateDebugTrace.js";
import {run_py_code, sendNoInteract} from "../utils/communication.js";
import {SAVE_FILE, SHOW_SAVE_DIALOG} from "../../common/communication_enums.js"

export default class File extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            name: this.props.initFile.name,
            editorText: this.props.initFile.content,
            savedText: this.props.initFile.content,
            location: this.props.initFile.location,

            outputData: [],
            outputActive: false,

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
    }

    componentDidMount() {
        this.editorRef.current.forceOpen();
    }

    componentWillUnmount() {
        if (this.state.killCallback) {
            this.state.detachCallback();
            this.state.killCallback();
        }
    }

    run = () => {
        if (this.state.killCallback) {
            this.state.detachCallback();
            this.state.killCallback();
        }
        const [interactCallback, killCallback, detachCallback] = run_py_code(
            this.state.editorText,
            out => this.handleOutputUpdate(out, false),
            out => this.handleOutputUpdate(out, true),
            this.handleHalt,
        );
        this.setState({
            interactCallback,
            killCallback,
            detachCallback,
            outputData: [],
            outputActive: true,
        });

        this.outputRef.current.forceOpen();
    };

    debug = async (data) => {
        let debugData;
        if (data) {
            debugData = data; // data has been generated for us by parent
        } else {
            debugData = await generateDebugTrace(this.state.editorText);
        }
        this.setState({ debugData, editorInDebugMode: true });
        this.debugRef.current.forceOpen();
    };

    format = async () => {
        // eslint-disable-next-line react/no-access-state-in-setstate
        const formatted = await format(this.state.editorText);
        this.setState({ editorText: formatted });
    };

    save = async () => {
        if (!this.state.location) {
            return this.saveAs();
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
        const ret = await sendNoInteract({ type: SHOW_SAVE_DIALOG });
        if (!ret.success) {
            return;
        }
        this.setState({
            name: ret.name,
            location: ret.location,
        }, this.save);
    };

    handleDebugUpdate = (editorDebugData) => {
        this.setState({ editorDebugData });
    };

    handleOutputUpdate = (text, isErr) => {
        this.setState((state) => {
            const outputData = state.outputData.concat([{
                text,
                isErr,
            }]);
            return { outputData };
        });
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
    };

    handleEditorChange = (editorText) => {
        this.setState(state => ({
            editorText,
            editorInDebugMode: state.editorDebugData && state.editorDebugData.code === editorText,
        }));
        this.handleActivate();
    };

    render() {
        const title = this.state.name + ((this.state.editorText === this.state.savedText) ? "" : "*");

        const editorDebugData = this.state.editorInDebugMode ? this.state.editorDebugData : null;

        return (
            <>
                <Editor
                    ref={this.editorRef}
                    text={this.state.editorText}
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
                <Debugger
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
