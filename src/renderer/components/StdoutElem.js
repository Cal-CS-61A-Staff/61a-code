import * as React from "react";
import * as hljs from "highlight.js";
import { ERROR, INPUT } from "./File.js";

export default class StdoutElem extends React.Component {
    constructor(props) {
        super(props);
        this.spanRef = React.createRef();
    }

    componentDidMount() {
        this.postRender();
    }

    componentDidUpdate() {
        this.postRender();
    }

    postRender() {
        if (this.props.type === INPUT) {
            hljs.highlightBlock(this.spanRef.current);
        } else if (this.props.type === ERROR) {
            this.spanRef.current.style.color = "palegreen";
        }
    }

    render() {
        return <span ref={this.spanRef} className={`lang-${this.props.lang}`}>{this.props.text}</span>;
    }
}
