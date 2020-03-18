import React from "react";
import AceEditor from "react-ace";
import * as ReactDOM from "react-dom";
import glWrap from "../utils/glWrap.js";

import "ace-builds/src-noconflict/mode-python";
import "ace-builds/src-noconflict/ext-language_tools";
import "ace-builds/src-min-noconflict/ext-searchbox";

import "ace-builds/src-noconflict/mode-scheme";
import "ace-builds/src-noconflict/mode-sql";
import "ace-builds/src-noconflict/theme-merbivore_soft";


class Editor extends React.Component {
    constructor(props) {
        super(props);
        this.editorRef = React.createRef();
        this.monaco = null;
        this.props.glContainer.on("show", () => this.props.onActivate());
    }

    componentDidMount() {
        this.editorRef.current.editor.focus();
        this.editorRef.current.editor.getSession().setUseSoftTabs(true);
        this.props.onActivate();
        this.props.glContainer.on("resize", () => this.editorRef.current.editor.resize());
    }

    onChange = (newValue) => {
        this.props.onChange(newValue);
    };

    render() {
        const code = this.props.debugData ? this.props.debugData.code : this.props.text;

        const markers = this.props.debugData ? [{
            startRow: this.props.debugData.line - 1,
            startCol: 0,
            endRow: this.props.debugData.line - 1,
            type: "fullLine",
            className: "activeLine",
        }] : [];

        return ReactDOM.createPortal(
            <AceEditor
                mode={this.props.language.toLowerCase()}
                theme="merbivore_soft"
                ref={this.editorRef}
                value={code}
                onChange={this.onChange}
                name="editor-component"
                width="100%"
                height="100%"
                fontSize={14}
                readOnly={
                    this.props.debugData ? this.props.debugData.code !== this.props.text : false
                }
                setOptions={{
                    enableBasicAutocompletion: true,
                    enableLiveAutocompletion: true,
                }}
                markers={markers}
            />, this.props.glContainer.getElement().get(0),
        );
    }
}

export default glWrap(Editor, "top", 50, "editor", ["editor"]);
