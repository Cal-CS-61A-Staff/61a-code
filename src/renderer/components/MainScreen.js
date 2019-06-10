import React from "react";
import {MENU_SAVE, MENU_SAVE_AS} from "../../common/communication_enums.js";
import NavBar from "./NavBar";
import OKResults from "./OKResults";
import {initGoldenLayout} from "../utils/goldenLayout";
import registerOKPyHandler from "../utils/receiveOKResults";
import claimMenu from "../utils/menuHandler";
import File from "./File";
import generateDebugTrace from "../../languages/python/utils/generateDebugTrace.js";

export default class MainScreen extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            fileRefs: {},
            activeFileKey: null,

            okResults: null,
            cachedOKModules: {},
            okPath: null,
            detachOKPyCallback:
                registerOKPyHandler(this.handleOKPyUpdate),

            detachMenuCallback:
                claimMenu({
                    [MENU_SAVE]: this.save,
                    [MENU_SAVE_AS]: this.saveAs,
                }),
        };
        this.okResultsRef = React.createRef();
        this.terminalRef = React.createRef();
    }

    componentDidMount() {
        initGoldenLayout(this.props.onAllClosed);
        const fileRefs = { 0: React.createRef() };
        this.setState({ fileRefs });
    }

    componentWillUnmount() {
        this.state.detachOKPyCallback();
        this.state.detachMenuCallback();
    }

    save = () => {
        this.state.fileRefs[this.state.activeFileKey].current.save();
    };

    saveAs = () => {
        this.state.fileRefs[this.state.activeFileKey].current.saveAs();
    };

    handleOKPyUpdate = (okResults, cachedOKModules, okPath) => {
        this.setState({ okResults, cachedOKModules, okPath });
        this.okResultsRef.current.forceOpen();
    };

    handleOKPyDebug = async (testData) => {
        const setupCode = [];
        const caseCode = [];
        let i = 0;
        for (; i !== testData.code.length; ++i) {
            if (!testData.code[i].includes("import")) {
                break;
            }
            setupCode.push(testData.code[i]);
        }
        for (; i !== testData.code.length; ++i) {
            caseCode.push(testData.code[i]);
        }

        const setupCodeStr = setupCode.join("\n");
        const caseCodeStr = caseCode.join("\n");

        const debugData = await generateDebugTrace(
            caseCodeStr,
            this.state.cachedOKModules,
            setupCodeStr,
            this.state.okPath,
        );

        this.state.fileRefs[this.state.activeFileKey].current.debug(debugData);
    };

    handleFileActivate = (key) => {
        if (key !== this.state.activeFileKey) {
            this.setState({
                activeFileKey: key,
            });
        }
    };

    handleActionClick = (action) => {
        const { activeFileKey } = this.state;
        this.state.fileRefs[activeFileKey].current[action]();
    };

    render() {
        const fileElems = Object.keys(this.state.fileRefs).map(key => (
            <File
                key={key}
                id={key}
                ref={this.state.fileRefs[key]}
                initFile={this.props.initFile}
                onActivate={this.handleFileActivate}
            />
        ));
        return (
            <>
                <NavBar
                    path={["folder1", "folder2", "file.py"]}
                    onActionClick={this.handleActionClick}
                />
                {fileElems}
                <div id="tabRoot" />
                <OKResults
                    ref={this.okResultsRef}
                    title="(OKPy Results)"
                    onDebug={this.handleOKPyDebug}
                    data={this.state.okResults}
                />
            </>
        );
    }
}
