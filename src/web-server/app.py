import csv
import json
import random
import sqlite3
import urllib.parse
from collections import namedtuple
from contextlib import contextmanager
from multiprocessing import Process, Queue, active_children

import black
import requests
from english_words import english_words_set as words  # list of words to generate links
from flask import (
    Flask,
    jsonify,
    make_response,
    redirect,
    request,
    session,
    url_for,
    send_from_directory,
    abort,
)
from flask_oauthlib.client import OAuth
from werkzeug import security

from IGNORE_scheme_debug import Buffer, debug_eval, scheme_read, tokenize_lines
from IGNORE_secrets import SECRET
from formatter import scm_reformat

CSV_ROOT = "https://docs.google.com/spreadsheets/d/1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI"

CSV_SHORTLINKS_SUFFIX = (
    "/export?format=csv&id=1-1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI&gid=0"
)

CSV_AUTHORIZED_SUFFIX = "/export?format=csv&id=1-1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI&gid=1240767129"

CSV_STORED_FILES_SUFFIX = (
    "/export?format=csv&id=1-1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI&gid=169284641"
)

CONSUMER_KEY = "61a-web-repl"

app = Flask(__name__, static_url_path="/static/", static_folder="static")
app.secret_key = SECRET

ServerFile = namedtuple(
    "ServerFile", ["short_link", "full_name", "url", "data", "discoverable"]
)

RETURN_RAW = "RETURN_RAW"

NOT_FOUND = "NOT_FOUND"
NOT_AUTHORIZED = "NOT_AUTHORIZED"
NOT_LOGGED_IN = "NOT_LOGGED_IN"

COOKIE_FILE_LOAD = "load"
COOKIE_SHORTLINK_REDIRECT = "shortlink"


@contextmanager
def connect_db():
    conn = sqlite3.connect("shortlinks.db")
    try:

        def db(*args):
            try:
                if isinstance(args[1][0], str):
                    raise TypeError
            except (IndexError, TypeError):
                return conn.cursor().execute(*args)
            else:
                return conn.cursor().executemany(*args)

        yield db
    finally:
        conn.commit()
        conn.close()


@app.route("/")
def root():
    return app.send_static_file("./index.html")


@app.route("/<path>/")
def load_file(path):
    raw = load_shortlink_file(path)

    if raw is NOT_LOGGED_IN:
        response = redirect(url_for("login"))
        response.set_cookie(COOKIE_SHORTLINK_REDIRECT, value=path)
        return response
    elif raw is NOT_AUTHORIZED:
        return "This file is only visible to staff."

    if raw is NOT_FOUND:
        return send_from_directory("static", path.replace("//", "/"))

    data = bytes(
        json.dumps({"fileName": raw["full_name"], "data": raw["data"]}), "utf-8"
    )

    response = make_response(redirect("/", code=302))
    response.set_cookie(COOKIE_FILE_LOAD, value=data)
    return response


@app.route("/<path>/raw")
def get_raw(path):
    return jsonify(load_shortlink_file(path))


def load_shortlink_file(path):
    with connect_db() as db:
        ret = db("SELECT * FROM links WHERE short_link=?;", [path]).fetchone()
        if ret is not None:
            return ServerFile(*ret)._asdict()

        try:
            ret = db(
                "SELECT * FROM studentLinks WHERE short_link=?;", [path]
            ).fetchone()

            if ret is None:
                return NOT_FOUND

            if check_auth():
                return ServerFile(ret[0], ret[1], "", ret[2], False)._asdict()
            else:
                return NOT_AUTHORIZED

        except Exception:
            return NOT_LOGGED_IN


@app.route("/api/load_file/<file_name>/")
def load_stored_file(file_name):
    with connect_db() as db:
        out = db(
            "SELECT * FROM stored_files WHERE file_name=?;", [file_name]
        ).fetchone()
        if out:
            return out[1]
    abort(404)


@app.route("/api/pytutor", methods=["POST"])
def pytutor_proxy():
    response = requests.post(
        "http://pythontutor.com/web_exec_py3.py",
        data={
            "user_script": request.form["code"],
            # "options_json": r'{"cumulative_mode":true,"heap_primitives":false}',
        },
    )
    return response.text


@app.route("/api/black", methods=["POST"])
def black_proxy():
    try:
        return jsonify(
            {
                "success": True,
                "code": black.format_str(request.form["code"], mode=black.FileMode())
                + "\n",
            }
        )
    except Exception as e:
        return jsonify({"success": False, "error": repr(e)})


@app.route("/api/_refresh")
def sync_refresh():
    refresh()
    return "", 204


@app.route("/api/_async_refresh", methods=["POST"])
def async_refresh():
    active_children()  # kills zombies
    p = Process(target=refresh)
    p.start()
    return "", 204


def refresh():
    # refresh shortlinks
    response = requests.get(CSV_ROOT + CSV_SHORTLINKS_SUFFIX)
    parsed = csv.reader(response.text.split("\n"))
    next(parsed)  # discard headers
    all_files = []
    for line in parsed:
        short_link, full_name, url, discoverable, *_ = line
        data = requests.get(url).text
        file = ServerFile(short_link, full_name, url, data, discoverable)
        all_files.append(file)

    with connect_db() as db:
        db("DROP TABLE IF EXISTS links")
        db("CREATE TABLE links (short_link, url, data, full_name, discoverable)")
        db("INSERT INTO links VALUES (?, ?, ?, ?, ?)", all_files)

    # refresh authorized staff
    response = requests.get(CSV_ROOT + CSV_AUTHORIZED_SUFFIX)
    parsed = csv.reader(response.text.split("\n"))
    next(parsed)  # discard headers
    authorized = []
    for line in parsed:
        email, *_ = line
        authorized.append([email])

    with connect_db() as db:
        db("DROP TABLE IF EXISTS authorized")
        db("CREATE TABLE authorized (email)")
        db("INSERT INTO authorized VALUES (?)", authorized)

    # refresh stored files
    with connect_db() as db:
        response = requests.get(CSV_ROOT + CSV_STORED_FILES_SUFFIX)
        parsed = csv.reader(response.text.split("\n"))
        next(parsed)  # discard headers
        stored_files = []
        for line in parsed:
            file_name, url, *_ = line
            data = requests.get(url).text
            stored_files.append([file_name, data])
        db("DROP TABLE IF EXISTS stored_files")
        db("CREATE TABLE stored_files (file_name, file_contents)")
        db("INSERT INTO stored_files VALUES (?, ?)", stored_files)


@app.route("/api/_registry")
def registry():
    return redirect(CSV_ROOT)


@app.route("/api/scm_debug", methods=["POST"])
def scm_debug():
    code = request.form["code"]
    q = Queue()
    p = Process(target=scm_worker, args=(code, q))
    p.start()
    p.join(10)
    if not q.empty():
        return jsonify(q.get())


@app.route("/api/scm_format", methods=["POST"])
def scm_format():
    try:
        return jsonify({"success": True, "code": scm_reformat(request.form["code"])})
    except Exception as e:
        return jsonify({"success": False, "error": repr(e)})


def scm_worker(code, queue):
    try:
        buff = Buffer(tokenize_lines(code.split("\n")))
        exprs = []
        while buff.current():
            exprs.append(scheme_read(buff))
        out = debug_eval(exprs)
    except Exception as err:
        print("ParseError:", err)
        raise

    queue.put(out)


def check_auth():
    ret = remote.get("user", token=session["dev_token"])
    email = ret.data["data"]["email"]
    with connect_db() as db:
        authorized = [
            prefix + "@berkeley.edu"
            for (prefix, *_) in db("SELECT * FROM authorized").fetchall()
        ]
    return email in authorized


@app.route("/api/share", methods=["POST"])
def share():
    file_name, file_content = request.form["fileName"], request.form["fileContent"]
    with connect_db() as db:
        link = "".join(random.sample(words, 1)[0].title() for _ in range(3))
        db("INSERT INTO studentLinks VALUES (?, ?, ?)", [link, file_name, file_content])
    return "code.cs61a.org/" + link


def create_oauth_client(app):
    oauth = OAuth(app)

    remote = oauth.remote_app(
        "ok-server",  # Server Name
        consumer_key=CONSUMER_KEY,
        consumer_secret=SECRET,
        request_token_params={"scope": "email", "state": lambda: security.gen_salt(10)},
        base_url="https://okpy.org/api/v3/",
        request_token_url=None,
        access_token_method="POST",
        access_token_url="https://okpy.org/oauth/token",
        authorize_url="https://okpy.org/oauth/authorize",
    )

    def check_req(uri, headers, body):
        """ Add access_token to the URL Request. """
        if "access_token" not in uri and session.get("dev_token"):
            params = {"access_token": session.get("dev_token")[0]}
            url_parts = list(urllib.parse.urlparse(uri))
            query = dict(urllib.parse.parse_qsl(url_parts[4]))
            query.update(params)

            url_parts[4] = urllib.parse.urlencode(query)
            uri = urllib.parse.urlunparse(url_parts)
        return uri, headers, body

    remote.pre_request = check_req

    @app.route("/login")
    def login():
        return remote.authorize(callback=url_for("authorized", _external=True))

    @app.route("/authorized")
    def authorized():
        resp = remote.authorized_response()
        if resp is None:
            return "Access denied: error=%s" % (request.args["error"])
        if isinstance(resp, dict) and "access_token" in resp:
            session["dev_token"] = (resp["access_token"], "")

        if COOKIE_SHORTLINK_REDIRECT in request.cookies:
            return load_file(request.cookies[COOKIE_SHORTLINK_REDIRECT])
        else:
            return redirect("/")

    @app.route("/user")
    def client_method():
        token = session["dev_token"][0]
        r = requests.get("https://okpy.org/api/v3/user/?access_token={}".format(token))
        r.raise_for_status()
        return jsonify(r.json())

    @remote.tokengetter
    def get_oauth_token():
        return session.get("dev_token")

    return remote


remote = create_oauth_client(app)

if __name__ == "__main__":
    app.run()
