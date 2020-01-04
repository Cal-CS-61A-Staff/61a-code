/* eslint-disable no-unused-vars,no-param-reassign */
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

function draw(mainCanvas, turtleCanvas, data, currIndex, turtleState) {
    const ctx = mainCanvas.getContext("2d");

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
            ctx.fillRect(0, 0, mainCanvas.width, mainCanvas.height);
        } else if (command === "clear") {
            ctx.clearRect(0, 0, mainCanvas.width, mainCanvas.height);
            turtleState.current = [[0, 0], 0];
        } else if (command === "report_position") {
            turtleState.current[0] = params;
        } else if (command === "report_angle") {
            [turtleState.current[1]] = params;
        } else {
            console.error(`Ignoring unknown graphics command ${command}`);
        }
    }

    const { current: [[turtleX, turtleY], angle] } = turtleState;

    const turtleCtx = turtleCanvas.getContext("2d");
    turtleCtx.clearRect(0, 0, turtleCanvas.width, turtleCanvas.height);
    turtleCtx.save();
    turtleCtx.translate(x(turtleX), y(turtleY));
    turtleCtx.rotate(angle * Math.PI / 180);
    turtleCtx.beginPath();
    turtleCtx.fillStyle = makeColorString([0, 0, 0]);
    turtleCtx.moveTo(-5, 5);
    turtleCtx.lineTo(5, 5);
    turtleCtx.lineTo(0, 0);
    turtleCtx.fill();
    turtleCtx.restore();
}

function Graphics({ data }) {
    const currIndex = useRef(0);
    const turtleState = useRef([[0, 0], 0]);
    return (
        <HTMLCanvas
            layers={2}
            draw={([mainCanvas, turtleCanvas]) => draw(
                mainCanvas, turtleCanvas, data, currIndex, turtleState,
            )}
        />
    );
}

export default glWrap(Graphics, "right", 50, "graphics", []);
