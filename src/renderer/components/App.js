import * as React from "react";
import LaunchScreen from "./LaunchScreen.js";
import MainScreen from "./MainScreen.js";

export default class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            launch: true,
            initFile: null,
        };
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
