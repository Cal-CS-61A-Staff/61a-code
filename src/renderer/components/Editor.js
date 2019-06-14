import React from "react";
import * as ReactDOM from "react-dom";
import glWrap from "../utils/glWrap.js";
import MonacoEditor from "../../../static/monaco-react/editor.js";

class Editor extends React.Component {
    constructor(props) {
        super(props);
        this.highlights = [];
        this.editorRef = React.createRef();
        this.monaco = null;
        this.props.glContainer.on("show", () => this.props.onActivate());
    }

    componentDidUpdate() {
        if (!this.props.debugData) {
            if (this.highlights !== []) {
                this.highlights = this.editorRef.current.editor.deltaDecorations(
                    this.highlights, [],
                );
            }
            return;
        }
        const { line } = this.props.debugData;
        this.highlights = this.editorRef.current.editor.deltaDecorations(this.highlights, [
            { range: new this.monaco.Range(line, 1, line, 1000), options: { isWholeLine: true, className: "activeLine" } },
        ]);
        this.editorRef.current.editor.revealLineInCenterIfOutsideViewport(line);
    }

    onChange = (newValue) => {
        this.props.onChange(newValue);
    };

    editorDidMount = (editor, monaco) => {
        this.monaco = monaco;
        editor.focus();
        this.props.onActivate();
        this.props.glContainer.on("resize", editor.layout.bind(editor));
    };

    render() {
        const code = this.props.debugData ? this.props.debugData.code : this.props.text;
        const options = {
            selectOnLineNumbers: true,
            fontSize: 14,
            readOnly: this.props.debugData ? this.props.debugData.code !== this.props.text : false,
        };
        return ReactDOM.createPortal(
            <MonacoEditor
                language={this.props.language}
                theme="vs-dark"
                ref={this.editorRef}
                value={code}
                options={options}
                onChange={this.onChange}
                editorDidMount={this.editorDidMount}
            />, this.props.glContainer.getElement().get(0),
        );
    }
}

export default glWrap(Editor, "column", 50, "editor", ["editor", "debugger"]);
