import * as React from "react";

export default class ErrorDialog extends React.Component {
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
                    <div className="modalHeader">{this.props.title}</div>
                    <div className="modalContent">
                        {this.props.content}
                    </div>
                </div>
            </div>
        );
    }
}
