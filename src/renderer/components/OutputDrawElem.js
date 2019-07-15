import * as React from "react";
import SVG from "svg.js";
import displayElem from "../utils/diagramming.js";

export default class OutputDrawElem extends React.PureComponent {
    constructor(props) {
        super(props);
        this.svgRef = React.createRef();
    }

    componentDidMount() {
        this.draw(this.svgRef.current);
    }

    draw(rawSVG) {
        const svg = SVG(rawSVG);
        svg.clear();

        displayElem(0, 10, this.props.data[0], this.props.data[1], svg, 0, new Map(), "white");

        rawSVG.setAttribute("height", svg.bbox().h + 20);
    }

    render() {
        return (
            <div>
                <svg
                    ref={this.svgRef}
                    style={{ width: "100%" }}
                />
            </div>
        );
    }
}
