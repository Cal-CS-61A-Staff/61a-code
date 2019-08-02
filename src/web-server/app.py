import csv
import json
import os
import random
import sqlite3
import urllib.parse

from collections import namedtuple
from contextlib import contextmanager
from csv import reader
from werkzeug import security
from english_words import english_words_set as words # list of words to generate links
from multiprocessing import Process, Queue

from rauth import OAuth2Service, OAuth1Service

from IGNORE_scheme_debug import Buffer, tokenize_lines, debug_eval, scheme_read

import black
import requests
from flask import Flask, redirect, url_for, session, request, jsonify, abort, send_from_directory, make_response
from flask_oauthlib.client import OAuth

remote = None

CSV = "https://docs.google.com/spreadsheets/u/1/d/1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI/export?format=csv&id=1-1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI&gid=0"

CONSUMER_KEY = '61a-web-repl'
SECRET = 'cDVC96t2mwb0AKtF8EPRd2wWSy9S4Vm'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STAFF_EMAILS = os.path.join(BASE_DIR, "staff_emails.csv")

app = Flask(__name__, static_url_path='', static_folder="")
ServerFile = namedtuple("ServerFile", ["short_link", "full_name", "url", "data", "discoverable"])


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


@app.route('/')
def root():
    return app.send_static_file('./index.html')


@app.route('/<path>/')
def load_file(path):
    raw = get_raw(path, True)
    filename = os.path.basename(path)
    if filename.startswith("IGNORE"):
        return None
    if raw is 'REDIRECT':
        return redirect(url_for('login'))
    if raw is None:
        return app.send_static_file(path)
    data = bytes(json.dumps({"fileName": raw["full_name"], "data": raw["data"]}), "utf-8")

    response = make_response(redirect("/", code=302))
    response.set_cookie("load", value=data)
    return response


@app.route('/<path>/raw')
def get_raw(path, internal=False):
    with connect_db() as db:
        ret = db("SELECT * FROM links WHERE short_link=?;", [path]).fetchone()
        if ret is not None:
            out = ServerFile(*ret)._asdict()
        else:
            ret = db("SELECT * FROM studentLinks WHERE short_link=?;", [path]).fetchone()
            try:
                if 'dev_token' in session:
                    if ret is not None and ok_auth():
                        out = ServerFile(ret[0], ret[1], "", ret[2], False)._asdict()
                    else:
                        out = None
                else:
                    if internal:
                        return 'REDIRECT'
                    else:
                        return redirect(url_for('login'))
            except Exception as e:
                return 'REDIRECT'
        if internal:
            return out
        else:
            return jsonify(out)


@app.route('/api/pytutor', methods=['POST'])
def pytutor_proxy():
    response = requests.post("http://pythontutor.com/web_exec_py3.py", data={
        "user_script": request.form["code"],
    })
    return response.text


@app.route("/api/black", methods=["POST"])
def black_proxy():
    try:
        return jsonify({"success": True, "code": black.format_str(request.form["code"], mode=black.FileMode()) + "\n"})
    except Exception as e:
        return jsonify({"success": False, "error": repr(e)})


@app.route("/api/_refresh")
def refresh():
    response = requests.get(CSV)
    parsed = reader(response.text.split("\n"))
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

    return jsonify(all_files)


@app.route('/api/scm_debug', methods=['POST'])
def scm_debug():
    code = request.form["code"]
    q = Queue()
    p = Process(target=scm_worker, args=(code, q))
    p.start()
    p.join(10)
    if not q.empty():
        return jsonify(q.get())


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


@app.route('/redirect/ok_auth')
def ok_auth():
    try:
        ret = remote.get('user', token=session['dev_token'])
        email = ret.data['data']['email']
        with open(STAFF_EMAILS) as emails:
            reader = csv.reader(emails)
            header = next(reader)
            for row in reader:
                if row[0] == email:
                    return True

    except Exception as e:
        print(e)
        pass
    return False

@app.route('/api/share', methods=['POST'])
def shareFile():
    fileName, fileContent = request.form["fileName"], request.form["fileContent"]
    with connect_db() as db:
        # Generate three random words from the set
        a, b, c = random.sample(words, 1)[0], random.sample(words, 1)[0], random.sample(words, 1)[0]
        # Capitalize first letter to increase readability
        a, b, c = a[0].upper() + a[1:], b[0].upper() + b[1:], c[0].upper() + c[1:]
        link = a+b+c
        db("INSERT INTO studentLinks VALUES (?, ?, ?)", [link, fileName, fileContent])
    return "code.cs61a.org/home/" + link

def create_client(app):
    oauth = OAuth(app)

    remote = oauth.remote_app(
        'ok-server',  # Server Name
        consumer_key=CONSUMER_KEY,
        consumer_secret=SECRET,
        request_token_params={'scope': 'email',
                              'state': lambda: security.gen_salt(10)},
        base_url='https://okpy.org/api/v3/',
        request_token_url=None,
        access_token_method='POST',
        access_token_url='https://okpy.org/oauth/token',
        authorize_url='https://okpy.org/oauth/authorize'
    )

    def check_req(uri, headers, body):
        """ Add access_token to the URL Request. """
        if 'access_token' not in uri and session.get('dev_token'):
            params = {'access_token': session.get('dev_token')[0]}
            url_parts = list(urllib.parse.urlparse(uri))
            query = dict(urllib.parse.parse_qsl(url_parts[4]))
            query.update(params)

            url_parts[4] = urllib.parse.urlencode(query)
            uri = urllib.parse.urlunparse(url_parts)
        return uri, headers, body
    remote.pre_request = check_req

    @app.route('/login')
    def login():
        print(url_for('authorized', _external=True))
        return remote.authorize(callback=url_for('authorized', _external=True))

    @app.route('/logout')
    def logout():
        session.pop('dev_token', None)
        return redirect(url_for('root'))

    @app.route('/authorized')
    def authorized():
        resp = remote.authorized_response()
        if resp is None:
            return 'Access denied: error=%s' % (
                request.args['error']
            )
        if isinstance(resp, dict) and 'access_token' in resp:
            session['dev_token'] = (resp['access_token'], '')
        return redirect("/")

    @app.route('/user')
    def client_method():
        token = session['dev_token'][0]
        r = requests.get('http://localhost:5000/api/v3/user/?access_token={}'.format(token))
        r.raise_for_status()
        return jsonify(r.json())

    @remote.tokengetter
    def get_oauth_token():
        return session.get('dev_token')

    return remote

if __name__ == "__main__":
    app.secret_key = SECRET
    remote = create_client(app)
    app.run()
