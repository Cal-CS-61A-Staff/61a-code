import React, { Component } from "react";
import UploadFileSelector from "./UploadFileSelector.js";
import RecentFileSelector from "./RecentFileSelector.js";

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
                        <UploadFileSelector onFileSelect={this.props.onFileSelect} />
                        <RecentFileSelector
                            files={this.props.recents}
                            onFileSelect={this.props.onFileSelect}
                        />
                    </div>
                </div>
            </div>
        );
    }
}
