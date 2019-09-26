import * as React from "react";
import SVG from "svg.js";
import { displayElem, displayTree } from "../utils/diagramming.js";

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
        console.log(this.props);
        const id = this.props.data[0]; const allData = this.props.data[1];
        if (id[0] === "ref") {
            const data = allData[id[1]];
            if (data[0] === "Tree") {
                displayTree(allData[id[1]], svg);
            }
            else {
                displayElem(0, 10, id, allData, svg, 0, new Map(), "white");
            }
        }    

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
