import os

import requests
from flask import send_from_directory, url_for, redirect, render_template, jsonify
from werkzeug.exceptions import NotFound

from constants import COOKIE_SHORTLINK_REDIRECT, STATIC_FOLDER, ServerFile
from db import connect_db

NOT_FOUND = "NOT_FOUND"
NOT_AUTHORIZED = "NOT_AUTHORIZED"
NOT_LOGGED_IN = "NOT_LOGGED_IN"


def create_shortlink_handler(app):
    def load_shortlink_file(path):
        with connect_db() as db:
            ret = db("SELECT * FROM links WHERE short_link=%s;", [path]).fetchone()
            if ret is not None:
                return ServerFile(
                    ret[0], ret[1], ret[2], ret[3].decode(), ret[4]
                )._asdict()

            base_paths = db("SELECT * FROM linkPaths").fetchall()
            for base_path, *_ in base_paths:
                url = os.path.join(base_path, path)
                data = requests.get(url)
                if data.ok:
                    text = data.text
                    if path.endswith(".sql"):
                        text = ".open --new\n\n" + text
                    return {"full_name": path, "data": text}

            ret = db("SELECT * FROM staffLinks WHERE link=%s;", [path]).fetchone()
            if ret is not None:
                return ServerFile(ret[0], ret[1], "", ret[2].decode(), False)._asdict()

            try:
                ret = db("SELECT * FROM studentLinks WHERE link=%s;", [path]).fetchone()

                if ret is None:
                    return NOT_FOUND

                if app.check_auth():
                    return ServerFile(
                        ret[0], ret[1], "", ret[2].decode(), False
                    )._asdict()
                else:
                    return NOT_AUTHORIZED

            except Exception:
                return NOT_LOGGED_IN

    @app.route("/<path>/")
    def load_file(path):
        try:
            out = send_from_directory(STATIC_FOLDER, path.replace("//", "/"))
        except NotFound:
            pass
        else:
            return out

        raw = load_shortlink_file(path)

        if raw is NOT_LOGGED_IN:
            response = redirect(url_for("login"))
            response.set_cookie(COOKIE_SHORTLINK_REDIRECT, value=path)
            return response
        elif raw is NOT_AUTHORIZED:
            return "This file is only visible to staff."

        if raw is NOT_FOUND:
            return "File not found", 404

        data = {"fileName": raw["full_name"], "data": raw["data"]}

        return render_template("index.html", initData={"loadFile": data})

    @app.route("/<path>/raw")
    def get_raw(path):
        return jsonify(load_shortlink_file(path))

    app.load_file = load_file
