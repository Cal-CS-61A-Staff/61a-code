import React, { Component } from "react";
import LocalFileSelector from "./LocalFileSelector.js";
import BrowserFileSelector from "./BrowserFileSelector.js";

export default class OpenDialog extends Component {
    handleClick = (e) => {
        if (e.target === e.currentTarget) {
            this.props.onClose();
        }
    };

    render() {
        return (
            <div className="modal" onClick={this.handleClick}>
                <div className="modalBody">
                    <span className="close" onClick={this.props.onClose}>&times;</span>
                    <div className="modalHeader">Open</div>
                    <div className="modalContent">
                        <LocalFileSelector onFileSelect={this.props.onFileSelect} />
                        <BrowserFileSelector
                            files={this.props.recents}
                            onFileSelect={this.props.onFileSelect}
                        />
                    </div>
                </div>
            </div>
        );
    }
}
