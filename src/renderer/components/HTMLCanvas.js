import React, { useRef, useEffect } from "react";

export default function HTMLCanvas({ draw }) {
    const canvasRef = useRef();

    const deltaX = useRef(-1500);
    const deltaY = useRef(-1000);

    const baseCanvas = useRef(null);

    function getBaseCanvas() {
        if (baseCanvas.current === null) {
            baseCanvas.current = document.createElement("canvas");
            baseCanvas.current.width = 3000;
            baseCanvas.current.height = 2000;
        }
        return baseCanvas.current;
    }

    function updateRenderCanvas() {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext("2d");

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(getBaseCanvas(), deltaX.current || 0, deltaY.current || 0);
    }

    useEffect(() => {
        deltaX.current = Math.round(canvasRef.current.parentNode.offsetWidth / 2 - 1500);
        deltaY.current = Math.round(canvasRef.current.parentNode.offsetHeight / 2 - 1000);
    }, [canvasRef.current]);

    useEffect(() => {
        draw(getBaseCanvas());
        updateRenderCanvas();
    });

    useEffect(() => {
        const canvas = canvasRef.current;
        let prevCursorOffsetX;
        let prevCursorOffsetY;
        let isDragging = false;

        function mouseDownHandler(e) {
            prevCursorOffsetX = e.clientX;
            prevCursorOffsetY = e.clientY;
            isDragging = true;
        }

        function mouseMoveHandler(e) {
            if (isDragging) {
                deltaX.current += e.clientX - prevCursorOffsetX;
                deltaY.current += e.clientY - prevCursorOffsetY;
                prevCursorOffsetX = e.clientX;
                prevCursorOffsetY = e.clientY;

                updateRenderCanvas();
            }
        }
        function mouseUpHandler() {
            isDragging = false;
        }

        canvas.addEventListener("mousedown", mouseDownHandler);
        canvas.addEventListener("mousemove", mouseMoveHandler);
        canvas.addEventListener("mouseup", mouseUpHandler);

        return () => {
            canvas.removeEventListener("mousedown", mouseDownHandler);
            canvas.removeEventListener("mousemove", mouseMoveHandler);
            canvas.removeEventListener("mouseup", mouseUpHandler);
        };
    }, [canvasRef.current]);

    return (
        <div className="canvas">
            <canvas width={3000} height={2000} ref={canvasRef} />
        </div>
    );
}
