import React, { Component } from "react";

export default class FileNameField extends Component {
    constructor(props) {
        super(props);
        this.inputRef = React.createRef();
    }

    handleKeyUp = (e) => {
        if (e.keyCode === 13) {
            this.handleClick();
        }
    };

    handleClick = () => {
        this.props.onClick(this.inputRef.current.value);
    };

    render() {
        return (
            <div className="modalCol">
                <p>
                    Enter file name to save your work in the browser:
                </p>
                <input
                    ref={this.inputRef}
                    className="fileNameField"
                    onKeyUp={this.handleKeyUp}
                />
                <button className="fileNameSubmitBtn" type="button" onClick={this.handleClick}>
                    Save
                </button>
            </div>
        );
    }
}
