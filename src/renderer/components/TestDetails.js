import React from "react";
import SuccessIcon from "./SuccessIcon";
import CommandIcon from "./CommandIcon";

export default class TestDetails extends React.Component {
    constructor(props) {
        super(props);
        this.divRef = React.createRef();
    }

    componentDidMount() {
        this.postRender();
    }

    componentDidUpdate() {
        this.postRender();
    }

    postRender() {
        this.divRef.current.scrollTo(0, 0);
    }

    render() {
        if (!this.props.data.rawName) {
            return (
                <div ref={this.divRef} className="testDetails testDetailsHeader testDetailsCongrats">
                    <SuccessIcon success={this.props.data.success} />
                    {" "}
                    All tests passed! Congratulations!
                </div>
            );
        }
        return (
            <div className="testDetails" ref={this.divRef}>
                <div
                    className="testDetailsHeader"
                    style={{ borderBottomColor: this.props.data.success ? "green" : "red" }}
                >
                    <SuccessIcon success={this.props.data.success} />
                    {"  "}
                    {this.props.data.rawName}
                    <CommandIcon
                        style={{
                            float: "right", marginRight: "25px", width: 30, height: 30,
                        }}
                        commandName="Debug"
                        onClick={() => this.props.onDebug(this.props.data)}
                    />
                </div>
                <pre className="rawOKPyOutput">
                    {this.props.data.raw.slice(this.props.data.raw.indexOf("\n"))
                        .trim()}
                </pre>
            </div>
        );
    }
}
