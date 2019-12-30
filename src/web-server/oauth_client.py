import urllib.parse

import requests
from flask import session, url_for, request, redirect, jsonify
from flask_oauthlib.client import OAuth
from werkzeug import security

from IGNORE_secrets import SECRET
from constants import COOKIE_IS_POPUP, COOKIE_SHORTLINK_REDIRECT
from db import connect_db


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

    def kill_popup():
        response = app.make_response("<script> window.close(); </script>")
        response.delete_cookie(COOKIE_IS_POPUP)
        return response

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

    @app.route("/oauth/popup_login")
    def popup_login():
        response = remote.authorize(callback=url_for("authorized", _external=True))
        response.set_cookie(COOKIE_IS_POPUP, value="")
        return response

    @app.route("/oauth/popup_logout")
    def popup_logout():
        session.pop("dev_token", None)
        return kill_popup()

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

        if COOKIE_IS_POPUP in request.cookies:
            return kill_popup()
        if COOKIE_SHORTLINK_REDIRECT in request.cookies:
            return app.load_file(request.cookies[COOKIE_SHORTLINK_REDIRECT])
        else:
            return redirect("/")

    @app.route("/api/user", methods=["POST"])
    def client_method():
        token = session["dev_token"][0]
        r = requests.get("https://okpy.org/api/v3/user/?access_token={}".format(token))
        r.raise_for_status()
        return jsonify(r.json())

    @remote.tokengetter
    def get_oauth_token():
        return session.get("dev_token")

    def check_auth():
        ret = remote.get("user", token=session["dev_token"])
        email = ret.data["data"]["email"]
        with connect_db() as db:
            authorized = [
                prefix + "@berkeley.edu"
                for (prefix, *_) in db("SELECT * FROM authorized").fetchall()
            ]
        return email in authorized

    return check_auth


CONSUMER_KEY = "61a-web-repl"
