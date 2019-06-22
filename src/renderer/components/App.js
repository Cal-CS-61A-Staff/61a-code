/* eslint-disable import/first,global-require */
let hot;
if (!ELECTRON) {
    ({ hot } = require("react-hot-loader/root"));
}
import * as React from "react";
import LaunchScreen from "./LaunchScreen.js";
import MainScreen from "./MainScreen.js";
// eslint-disable-next-line no-unused-vars
import MenuBar from "./MenuBar.js";
import { sendNoInteract } from "../utils/communication.js";
import { OPEN_FILE } from "../../common/communicationEnums.js";

class App extends React.Component {
    constructor(props) {
        super(props);

        console.log(props.path);

        this.state = {
            launch: true,
            initFile: null,
        };

        if (props.path) {
            sendNoInteract({
                type: OPEN_FILE,
                location: props.path,
            }).then((value) => {
                if (value.success) {
                    this.handleFileCreate(value.file);
                }
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
