/* eslint-disable import/first,global-require */
let hot;
if (!ELECTRON) {
    ({ hot } = require("react-hot-loader/root"));
}
import * as React from "react";
import Cookies from "js-cookie";

import LaunchScreen from "./LaunchScreen.js";
import MainScreen from "./MainScreen.js";

let MenuBar;
if (!ELECTRON) {
    MenuBar = require("./MenuBar.js").default;
}
import { sendNoInteract } from "../utils/communication.js";
import { OPEN_FILE } from "../../common/communicationEnums.js";

// https://stackoverflow.com/questions/22259779/flask-setting-json-in-a-cookie-and-decoding-it-on-the-client-in-javascript?lq=1
function decodeFlaskCookie(val) {
    if (val.indexOf("\\") === -1) {
        return val; // not encoded
    }
    let out = val.replace(/\\"/g, "\"");
    out = out.replace(/\\(\d{3})/g, (match, octal) => String.fromCharCode(parseInt(octal, 8)));
    return out.replace(/\\\\/g, "\\");
}

class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            launch: true,
            initFile: null,
        };
    }

    componentDidMount() {
        if (this.props.path) {
            sendNoInteract({
                type: OPEN_FILE,
                location: this.path,
            }).then((value) => {
                if (value.success) {
                    this.handleFileCreate(value.file);
                }
            });
        }

        const shortFileLoad = Cookies.get("load");
        Cookies.remove("load");

        if (shortFileLoad) {
            console.log(decodeFlaskCookie(shortFileLoad));
            const parsed = JSON.parse(decodeFlaskCookie(shortFileLoad));
            this.handleFileCreate({
                name: parsed.fileName,
                location: null,
                content: parsed.data,

            });
        }
    }

    handleAllClosed = () => {
        this.setState({ launch: true });
    };

    handleFileCreate = (file, startInterpreter) => {
        this.setState({
            launch: false,
            initFile: file,
            startInterpreter,
        });
    };

    render() {
        let primaryElem;
        if (this.state.launch) {
            primaryElem = <LaunchScreen onFileCreate={this.handleFileCreate} />;
        } else {
            primaryElem = (
                <MainScreen
                    onAllClosed={this.handleAllClosed}
                    initFile={this.state.initFile}
                    startInterpreter={this.state.startInterpreter}
                />
            );
        }

        if (ELECTRON) {
            return primaryElem;
        } else {
            return (
                <>
                    <MenuBar />
                    { primaryElem }
                </>
            );
        }
    }
}

export default (ELECTRON ? App : hot(App));
