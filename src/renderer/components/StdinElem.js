import * as React from "react";

export default class StdinElem extends React.Component {
    constructor(props) {
        super(props);
        this.inputRef = React.createRef();
    }

    setText(text) {
        this.inputRef.current.innerText = text;
        this.goToEnd();
    }

    handleKeyDown = (e) => {
        if (e.keyCode === 9) {
            e.preventDefault();
            document.execCommand("insertHTML", false, "    ");
        } else if (e.keyCode === 13) {
            e.preventDefault();
            this.props.onInput(`${this.inputRef.current.innerText}\n`);
            this.setText("");
        }
    };

    handleInput = (e) => {
        let text = e.currentTarget.innerText;
        const lines = text.split(/\r\n|\r|\n/);
        for (let i = 0; i !== lines.length - 1; ++i) {
            if (lines[i] === "" && i === lines.length - 2) {
                continue; // TODO: FIX UGLY HACK
            }
            this.props.onInput(`${lines[i]}\n`);
        }
        text = lines[lines.length - 1];
        if (lines.length > 1) {
            this.setText(text);
        }
    };

    // https://stackoverflow.com/questions/1125292/how-to-move-cursor-to-end-of-contenteditable-entity/3866442#3866442
    goToEnd() {
        const range = document.createRange();
        range.selectNodeContents(this.inputRef.current);
        range.collapse(false);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
    }


    focus() {
        this.inputRef.current.focus();
    }

    render() {
        return (
            <span
                ref={this.inputRef}
                className="consoleInput"
                onInput={this.handleInput}
                onKeyDown={this.handleKeyDown}
                contentEditable="true"
            />
        );
    }
}
