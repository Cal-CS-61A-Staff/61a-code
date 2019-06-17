import { hot } from "react-hot-loader/root";
import * as React from "react";
import LaunchScreen from "./LaunchScreen.js";
import MainScreen from "./MainScreen.js";
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

    handleFileCreate = (file) => {
        this.setState({
            launch: false,
            initFile: file,
        });
    };

    render() {
        if (this.state.launch) {
            return <LaunchScreen onFileCreate={this.handleFileCreate} />;
        } else {
            return (
                <MainScreen
                    onAllClosed={this.handleAllClosed}
                    initFile={this.state.initFile}
                />
            );
        }
    }
}

export default hot(App);
