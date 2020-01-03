import React, { useRef } from "react";

import glWrap from "../utils/glWrap.js";
import HTMLCanvas from "./HTMLCanvas.js";

function makeColorString([r, g, b]) {
    return `rgb(${r}, ${g}, ${b})`;
}

function x(val) {
    return val + 1500;
}

function y(val) {
    return -val + 1000;
}

function draw(canvas, data, currIndex) {
    const ctx = canvas.getContext("2d");

    // eslint-disable-next-line no-param-reassign
    for (; currIndex.current !== data.length; ++currIndex.current) {
        const [command, ...params] = data[currIndex.current];
        if (command === "draw_rectangular_line") {
            const [[startX, startY, endX, endY], color, width] = params;
            ctx.beginPath();
            ctx.lineWidth = width;
            ctx.strokeStyle = makeColorString(color);
            ctx.moveTo(x(startX), y(startY));
            ctx.lineTo(x(endX), y(endY));
            ctx.stroke();
        } else if (command === "draw_circle") {
            const [[centerX, centerY, radius], color, width, isFilled] = params;
            ctx.beginPath();
            ctx.lineWidth = width;
            ctx.strokeStyle = makeColorString(color);
            ctx.fillStyle = makeColorString(color);
            ctx.arc(x(centerX), y(centerY), radius, 0, 2 * Math.PI);
            ctx.stroke();
            if (isFilled) {
                ctx.fill();
            }
        } else if (command === "fill_polygon") {
            const [points, color] = params;
            ctx.beginPath();
            ctx.fillStyle = makeColorString(color);
            for (const [nextX, nextY] of points) {
                ctx.lineTo(x(nextX), y(nextY));
            }
            ctx.fill();
        } else if (command === "set_bgcolor") {
            const [color] = params;
            ctx.fillStyle = makeColorString(color);
            ctx.fillRect(0, 0, canvas.width, canvas.height);
        } else if (command === "clear") {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        } else {
            console.error(`Ignoring unknown graphics command ${command}`);
        }
    }
}

function Graphics({ data }) {
    const currIndex = useRef(0);
    currIndex.current = Math.min(currIndex.current, data.length);
    return (
        <HTMLCanvas draw={canvas => draw(canvas, data, currIndex)} />
    );
}

export default glWrap(Graphics, "right", 50, "graphics", []);
