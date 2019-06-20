import path from "path";

importScripts(path.join(__static, "brython.js"));
importScripts(path.join(__static, "brython_stdlib.js"));

onmessage = (e) => {
    const { data } = e;
    const { text } = data;

};
