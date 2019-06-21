import React, { Component } from "react";
import FileNameField from "./FileNameField.js";
import DownloadButton from "./DownloadButton.js";

export default class SaveDialog extends Component {
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
                    <div className="modalHeader">Save As</div>
                    <div className="modalContent" style={{ flexDirection: "column" }}>
                        <FileNameField
                            defaultValue={this.props.defaultValue}
                            onClick={this.props.onNameSelect}
                        />
                        <DownloadButton onClick={this.props.onDownloadClick} />
                    </div>
                </div>
            </div>
        );
    }
}
