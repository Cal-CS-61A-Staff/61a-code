import React from "react";
import { SHOW_OPEN_DIALOG } from "../../common/communicationEnums.js";
import IntroBox from "./IntroBox";
import { sendNoInteract } from "../utils/communication.js";

export default class LaunchScreen extends React.Component {
    handleCreateClick = () => {
        const file = {
            name: "untitled",
            location: null,
            content: "",
        };
        this.props.onFileCreate(file);
    };

    handleOpenClick = async () => {
        const ret = await sendNoInteract({
            type: SHOW_OPEN_DIALOG,
        });
        if (ret.success) {
            this.props.onFileCreate(ret.file);
        }
    };

    render() {
        return (
            <div className="row">
                <div className="introColumn">
                    <IntroBox
                        onCreateClick={this.handleCreateClick}
                        onOpenClick={this.handleOpenClick}
                    />
                </div>
                <div className="recentColumn" />
            </div>
        );
    }
}
