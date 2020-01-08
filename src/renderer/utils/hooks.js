import { useEffect, useState } from "react";

export function useAsync(callback, initialState = null, deps = []) {
    const [data, setData] = useState(initialState);

    useEffect(() => {
        let go = true;
        setData(initialState);
        Promise.resolve(callback()).then((x) => { if (go) setData(x); });
        return () => { go = false; };
    }, deps);

    return data;
}

export function useRequestAnimationFrame(callback, deps) {
    let initialTime;
    let running = true;
    useEffect(() => {
        const worker = (time) => {
            if (!initialTime) {
                initialTime = time;
            }
            const delta = time - initialTime;
            callback(delta);
            if (running) {
                requestAnimationFrame(worker);
            }
        };
        requestAnimationFrame(worker);
        return () => { running = false; };
    }, deps);
}
