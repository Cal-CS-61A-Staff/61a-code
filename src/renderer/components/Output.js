import * as React from "react";
import RunStopButton from "./RunStopButton";
import StdinElem from "./StdinElem";
import OutputElem from "./OutputElem";
import glWrap from "../utils/glWrap";

class Output extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            // eslint-disable-next-line react/no-unused-state
            history: [],
            // eslint-disable-next-line react/no-unused-state
            historyIndex: 0,
        };
        this.inputRef = React.createRef();
        this.outputRef = React.createRef();
    }

    componentDidMount() {
        this.postRender();
    }

    componentDidUpdate() {
        this.postRender();
    }

    componentWillUnmount() {
        this.props.onStop();
    }

    handleOutputClick = () => {
        if (this.inputRef.current) {
            setTimeout(() => {
                if (window.getSelection().rangeCount === 0
                    || window.getSelection().getRangeAt(0).collapsed) {
                    this.inputRef.current.focus();
                }
            }, 0);
        }
    };

    handleInput = (text) => {
        this.postRender(text);
        this.props.onInput(text);
    };

    postRender() {
        this.outputRef.current.scrollTop = this.outputRef.current.scrollHeight;
    }

    render() {
        return (
            <>
                <div className="outputControls">
                    <RunStopButton
                        codeRunning={this.props.outputActive}
                        onStop={this.props.onStop}
                        onRestart={this.props.onRestart}
                    />
                </div>
                {/* eslint-disable-next-line */}
                <div className="outputWrapper" ref={this.outputRef} onClick={this.handleOutputClick}>
                    <div className="output">
                        {/* eslint-disable-next-line react/no-array-index-key */}
                        {this.props.data.map((elem, index) => <OutputElem key={index} {...elem} />)}
                        {this.props.outputActive
                        && <StdinElem ref={this.inputRef} onInput={this.handleInput} />}
                        <div className="outputScrollAnchor" />
                    </div>
                </div>
            </>
        );
    }
}

export default glWrap(Output, "column", 30, "output", ["output", "okResults", "terminal"]);
