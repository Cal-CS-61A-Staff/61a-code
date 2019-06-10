import path from "path";
import amdLoader from "monaco-editor/min/vs/loader.js"
import LaunchScreen from "./components/LaunchScreen.js";
import MainScreen from "./components/MainScreen.js";
import * as React from "react";
import * as ReactDOM from "react-dom";
import $ from "jquery";
const amdRequire = amdLoader.require;

import "./style.global.css";

function uriFromPath(_path) {
    let pathName = path.resolve(_path).replace(/\\/g, '/');
    if (pathName.length > 0 && pathName.charAt(0) !== '/') {
        pathName = '/' + pathName;
    }
    return encodeURI('file://' + pathName);
}

amdRequire.config({
    baseUrl: uriFromPath(path.join(__static, '/monaco-editor/min'))
});

// workaround monaco-css not understanding the environment
self.module = undefined;

amdRequire(['vs/editor/editor.main'], init);

function init() {
    console.log(window.$);
    window.$ = $;
    ReactDOM.render(<App />, document.getElementById("app"));
}

class App extends React.Component {
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
