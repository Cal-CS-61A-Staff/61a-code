import React from "react";
import {
    MENU_CLOSE_TAB,
    MENU_NEW, MENU_OPEN, MENU_SAVE, MENU_SAVE_AS, MENU_SHARE, SHOW_OPEN_DIALOG,
} from "../../common/communicationEnums.js";
import NavBar from "./NavBar";
import OKResults from "./OKResults";
import { initGoldenLayout } from "../utils/goldenLayout";
import registerOKPyHandler from "../utils/receiveOKResults";
import claimMenu from "../utils/menuHandler";
import File from "./File";
import generateDebugTrace from "../../languages/python/utils/generateDebugTrace.js";
import { sendNoInteract } from "../utils/communication.js";

export default class MainScreen extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            files: {},
            activeFileKey: null,

            okResults: null,
            cachedOKModules: {},
            okPath: null,
            detachOKPyCallback:
                registerOKPyHandler(this.handleOKPyUpdate),

            detachMenuCallback:
                claimMenu({
                    [MENU_NEW]: this.newFile,
                    [MENU_OPEN]: this.openFile,
                    [MENU_SAVE]: this.save,
                    [MENU_SAVE_AS]: this.saveAs,
                    [MENU_CLOSE_TAB]: this.closeTab,
                    [MENU_SHARE]: this.share,
                }),
        };

        this.keyCnt = 0;

        this.okResultsRef = React.createRef();
    }

    componentDidMount() {
        initGoldenLayout(this.props.onAllClosed);
        const files = {
            [this.keyCnt++]:
                {
                    ref: React.createRef(),
                    initData: this.props.initFile,
                    startInterpreter: this.props.startInterpreter,
                },
        };
        this.setState({ files });
    }

    componentWillUnmount() {
        this.state.detachOKPyCallback();
        this.state.detachMenuCallback();
    }

    newFile = () => {
        this.setState(state => ({
            files: {
                ...state.files,
                [this.keyCnt++]: {
                    ref: React.createRef(),
                    initData: {
                        name: "untitled",
                        location: null,
                        content: "",
                    },
                },
            },
        }));
    };

    openFile = async () => {
        const ret = await sendNoInteract({
            type: SHOW_OPEN_DIALOG,
        });
        if (ret.success) {
            this.setState(state => ({
                files: {
                    ...state.files,
                    [this.keyCnt++]: {
                        ref: React.createRef(),
                        initData: ret.file,
                    },
                },
            }));
        }
    };

    save = () => {
        this.state.files[this.state.activeFileKey].ref.current.save();
    };

    saveAs = () => {
        this.state.files[this.state.activeFileKey].ref.current.saveAs();
    };

    closeTab = () => {
        console.error("close-tab shortcut not yet implemented!");
    };

    share = () => {
        this.state.files[this.state.activeFileKey].ref.current.share();
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

        // todo: make language agnostic
        const debugData = await generateDebugTrace(
            caseCodeStr,
            this.state.cachedOKModules,
            setupCodeStr,
            this.state.okPath,
        );

        this.state.files[this.state.activeFileKey].ref.current.debug(debugData);
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
        this.state.files[activeFileKey].ref.current[action]();
    };

    render() {
        const fileElems = Object.keys(this.state.files).map(key => (
            <File
                key={key}
                id={key}
                ref={this.state.files[key].ref}
                initFile={this.state.files[key].initData}
                startInterpreter={this.state.files[key].startInterpreter}
                onActivate={this.handleFileActivate}
            />
        ));

        const { activeFileKey } = this.state;
        let activePath = [];

        if (activeFileKey) {
            const activeFile = this.state.files[activeFileKey].ref.current;
            if (activeFile) {
                const { location } = activeFile.state;
                if (location) {
                    activePath = location.split("/");
                }
            }
        }

        return (
            <>
                <NavBar
                    path={activePath}
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
