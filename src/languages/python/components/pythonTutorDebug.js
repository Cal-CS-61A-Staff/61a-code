import * as React from "react";
import CommandIcon from "../../../renderer/components/CommandIcon.js";

import "../pytutor/jquery-ui-1.11.4/jquery-ui.css";
import "../pytutor/pytutor.css";
import "./pytutorOverrides.css";

export default class PythonTutorDebug extends React.PureComponent {
    constructor(props) {
        super(props);
        this.vizRef = React.createRef();
        this.vizDivID = Math.random().toString(36).replace(/[^a-z]+/g, "").substr(2, 10);
        this.viz = null;
        this.state = { index: 0 };
        // this.highlights = [];
    }

    componentDidMount() {
        setTimeout(this.postRender, 0);
    }

    componentDidUpdate() {
        setTimeout(this.postRender, 0);
    }

    componentWillUnmount() {
        this.props.onUpdate(null);
    }

    postRender = () => {
        // this.editorRef.current.editor.setValue(this.props.data.code);
        this.viz = new ExecutionVisualizer(
            this.vizDivID,
            this.props.data,
            { hideCode: true, startingInstruction: this.state.index },
        );
        this.viz.redrawConnectors();

        const point = this.props.data.trace[this.state.index];
        let fileName = point.custom_module_name;
        if (!fileName) {
            fileName = "main_code";
        }
        this.props.onUpdate({
            code: this.props.data.code[fileName],
            line: point.line,
        });
    };

    handleResize = () => {
        if (this.viz) {
            this.viz.redrawConnectors();
        }
    };

    handleChange = (index) => {
        this.setState({ index });
    };

    // eslint-disable-next-line camelcase
    UNSAFE_componentWillReceiveProps(nextProps) {
        if (this.props.data !== nextProps.data) {
            this.setState({ index: 0 });
        }
    }

    render() {
        return (
            <>
                <div className="pyVizEnvs">
                    <PositionChooser
                        num={this.props.data.trace.length - 1}
                        value={this.state.index}
                        onChange={this.handleChange}
                    />
                    <div
                        id={this.vizDivID}
                        className="pyVizEnvsHolder"
                        onScroll={this.handleResize}
                        ref={this.vizRef}
                    />
                </div>
            </>
        );
    }
}

// PythonTutorDebug.propTypes = {
//     data: PropTypes.object,
//     glContainer: PropTypes.shape({
//         on: PropTypes.func,
//     }),
//     onUpdate: PropTypes.func,
// };

class PositionChooser extends React.Component {
    handlePrevClick = () => {
        this.props.onChange(Math.max(this.props.value - 1, 0));
    };

    handleNextClick = () => {
        this.props.onChange(Math.min(this.props.value + 1, this.props.num));
    };

    handleDrag = (e) => {
        this.props.onChange(parseInt(e.target.value, 10));
    };

    render() {
        return (
            <div className="pyPosChooser">
                <NavButton prev onClick={this.handlePrevClick} />
                <PositionSlider
                    num={this.props.num}
                    value={this.props.value}
                    onChange={this.handleDrag}
                />
                <NavButton next onClick={this.handleNextClick} />
            </div>
        );
    }
}

// PositionChooser.propTypes = {
//     onChange: PropTypes.func,
//     value: PropTypes.number,
//     num: PropTypes.number,
// };

function NavButton(props) {
    if (props.prev) {
        return (
            <CommandIcon
                commandName="Prev"
                style={{ backgroundColor: "black" }}
                onClick={props.onClick}
            />
        );
    } else {
        return (
            <CommandIcon
                commandName="Next"
                style={{ backgroundColor: "black" }}
                onClick={props.onClick}
            />
        );
    }
}

function PositionSlider(props) {
    return (
        <div className="pyPosSlider">
            <input
                type="range"
                min={0}
                max={props.num}
                value={props.value}
                step={1}
                className="pyPosSliderElem"
                onChange={props.onChange}
            />
        </div>
    );
}

// PositionSlider.propTypes = {
//     onChange: PropTypes.func,
//     value: PropTypes.number,
//     num: PropTypes.number,
// };
