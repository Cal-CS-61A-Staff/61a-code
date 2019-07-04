import * as React from "react";
import $ from "jquery";
import SVG from "svg.js";

function getDims() {
    const parentElement = document.body;
    const div = document.createElement("div");
    $(div).css("position", "absolute");
    $(div).css("white-space", "pre-line");
    $(div).css("font-family", "Monaco, monospace");
    $(div).css("font-size", "14px");

    div.innerHTML = "x".repeat(999) + "x\n".repeat(1000);
    parentElement.appendChild(div);
    const w = div.offsetWidth / 1000;
    const h = div.offsetHeight / 1001;
    parentElement.removeChild(div);
    return [w, h];
}

const charWidth = getDims()[0];

const minWidth = charWidth * 4 + 5;

function calcContentLength(elem) {
    if (elem[0] === "ref") {
        return minWidth;
    } else {
        return Math.max(minWidth, charWidth * elem[1].length + 10);
    }
}

function straightArrow(container, x1, y1, x2, y2) {
    container.circle(5).dx(x1 - 5 / 2).dy(y1 - 5 / 2).fill("white");
    container
        .polygon("0,0 -10,5 -10,-5")
        .fill("white")
        .dx(x2).dy(y2)
        .rotate(180 / Math.PI * Math.atan2(y2 - y1, x2 - x1), x2, y2);
    const length = Math.hypot(x2 - x1, y2 - y1);
    container
        .line(x1, y1, x2 + (x1 - x2) / length * 5, y2 + (y1 - y2) / length * 5)
        .stroke({ width: 2, color: "white" });
}

function curvedArrow(container, x1, y1, x2, y2) {
    straightArrow(container, x1, y1, x2, y2);
}

function displayElem(x, y, id, allData, container, depth, cache, index, x1 = false, y1 = false) {
    if (id[0] === "ref") {
        const data = allData[id[1]];

        if (!x1) {
            // eslint-disable-next-line no-param-reassign
            x1 = x + minWidth / 2;
            // eslint-disable-next-line
            y1 = y + minWidth / 2;
        }
        if (cache.has(id[1])) {
            curvedArrow(container, x1, y1, ...cache.get(id[1]));
            return 0;
        }
        let x2;
        let y2;
        if (depth === 0) {
            cache.set(id[1], [x, y]);
            x2 = x + minWidth + 15;
            y2 = y + minWidth / 2;
            // eslint-disable-next-line no-param-reassign
            x = x2;
        } else {
            x2 = x + minWidth / 2;
            y2 = y + (minWidth + 15) * depth;
            // eslint-disable-next-line no-param-reassign
            y = y2;
        }

        let content;
        if (data[0] === "list") {
            [, content] = data;
            straightArrow(container, x1, y1, x2, y2);
        } else {
            content = [data[1]];
            straightArrow(container, x1, y1, x, y + minWidth / 2);
        }
        cache.set(id[1], [x, y + minWidth / 2]);

        let pos = 0;
        const lens = [];
        for (const elem of content) {
            lens.push(pos);
            pos += calcContentLength(elem);
        }

        let newDepth = 0;
        for (let i = content.length - 1; i >= 0; --i) {
            if (i !== 0) {
                container.line(x + lens[i], y, x + lens[i], y + minWidth).stroke({ color: "white", width: 2 });
            }
            const elem = content[i];
            if (i !== content.length - 1 && elem[0] === "ref" && !cache.has(elem[1])) {
                newDepth += 1;
            }
            newDepth += displayElem(
                x + lens[i], y, elem, allData, container, newDepth, cache, index,
            );
        }

        if (data[0] === "promise") {
            container.circle(minWidth)
                .dx(x).dy(y)
                .stroke({ color: "white", width: 2 })
                .fill("transparent")
                .back();
        } else if (data[0] === "list") {
            container.rect(pos, minWidth)
                .dx(x).dy(y)
                .stroke({ color: "white", width: 2 })
                .fill("transparent")
                .back();
        }
        // container.text(newDepth.toString(10)).dx(x).dy(y);
        return newDepth;
    } else {
        const width = calcContentLength(id);
        container.text(id[1])
            .fill("white")
            .font("family", "Monaco, monospace").font("size", 14)
            .cx(x + width / 2)
            .cy(y + minWidth / 2);
        // container.text("0").dx(x).dy(y);
        return 0;
    }
}

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

        displayElem(0, 10, this.props.data[0], this.props.data[1], svg, 0, new Map(), -1);

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
