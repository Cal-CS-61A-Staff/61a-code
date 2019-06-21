import React, { Component } from "react";

export default class LocalFileSelector extends Component {
    handleDragEnter = (e) => {
        e.preventDefault();
        e.stopPropagation();

        this.highlight(e.currentTarget);
    };

    handleDragOver = (e) => {
        e.preventDefault();
        e.stopPropagation();
        this.highlight(e.currentTarget);
    };

    handleDragLeave = (e) => {
        e.preventDefault();
        e.stopPropagation();

        this.unHighlight(e.currentTarget);
    };

    handleDrop = (e) => {
        e.preventDefault();
        e.stopPropagation();

        this.unHighlight(e.currentTarget);

        const dt = e.dataTransfer;
        const { files } = dt;
        const file = files[0];
        const reader = new FileReader();
        reader.readAsText(file);
        reader.onload = () => {
            this.props.onFileSelect({
                name: file.name ? file.name : "untitled",
                location: null,
                content: reader.result,
            });
        };
    };

    highlight = (elem) => {
        // eslint-disable-next-line no-param-reassign
        elem.style.borderColor = "yellow";
    };

    unHighlight = (elem) => {
        // eslint-disable-next-line no-param-reassign
        elem.style.borderColor = "white";
    };

    render() {
        return (
            <div className="modalCol localFileSelector">
                <div
                    className="fileDropTarget"
                    onDragEnter={this.handleDragEnter}
                    onDragOver={this.handleDragOver}
                    onDragLeave={this.handleDragLeave}
                    onDrop={this.handleDrop}
                >
                    <span className="textHolder"> Drag files here to upload. </span>
                </div>
                <div className="fileUploadButton">
                    <span className="textHolder"> Or click here to select files. </span>
                </div>
            </div>
        );
    }
}
