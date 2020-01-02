import React, { useRef } from "react";
import glWrap from "../utils/glWrap.js";
import Canvas from "./Canvas.js";

function draw(svg, data, currIndex) {
    // eslint-disable-next-line no-param-reassign
    for (; currIndex.current !== data.length; ++currIndex.current) {
        const [command, params] = data[currIndex.current];
        if (command === "draw_rectangular_line") {
            // todo
        } else if (command === "draw_circle") {
            // todo
        } else if (command === "fill_polygon") {
            // todo
        } else if (command === "set_bgcolor") {
            // todo
        } else if (command === "clear") {
            // todo
        } else {
            console.error(`Ignoring unknown graphics command ${command}`);
        }
    }
}

function Graphics({ data }) {
    const currIndex = useRef(0);
    return (
        <Canvas draw={svg => draw(svg, data, currIndex)} />
    );
}

export default glWrap(Graphics, "right", 50, "graphics", ["editor", "debugger"]);
