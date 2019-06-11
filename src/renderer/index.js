import path from "path";
import amdLoader from "monaco-editor/min/vs/loader.js";
import * as React from "react";
import * as ReactDOM from "react-dom";
import MainScreen from "./components/MainScreen.js";
import LaunchScreen from "./components/LaunchScreen.js";

import "./style.global.css";

const amdRequire = amdLoader.require;

function uriFromPath(_path) {
    let pathName = path.resolve(_path).replace(/\\/g, "/");
    if (pathName.length > 0 && pathName.charAt(0) !== "/") {
        pathName = `/${pathName}`;
    }
    return encodeURI(`file://${pathName}`);
}

amdRequire.config({
    baseUrl: uriFromPath(path.join(__static, "/monaco-editor/min")),
});

// workaround monaco-css not understanding the environment
// eslint-disable-next-line no-restricted-globals
self.module = undefined;

amdRequire(["vs/editor/editor.main"], init);

function injectScript(src) {
    return new Promise((resolve) => {
        const script = document.createElement("script");
        script.src = uriFromPath(path.join(__static, src));
        document.body.appendChild(script);
        script.onload = () => resolve();
    });
}

async function init() {
    await injectScript("d3.v2.min.js");
    await injectScript("jquery-1.8.2.min.js");
    await injectScript("jquery.ba-bbq.min.js");
    await injectScript("jquery-ui.min.js");
    await injectScript("jquery.jsPlumb-1.3.10-all-min.js");
    await injectScript("pytutor.js");
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
