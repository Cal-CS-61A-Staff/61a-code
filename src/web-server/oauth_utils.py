from flask import session

from db import connect_db


def check_auth(app):
    email = get_user_data(app)["email"]
    with connect_db() as db:
        authorized = [
            prefix + "@berkeley.edu"
            for (prefix, *_) in db("SELECT * FROM authorized").fetchall()
        ]
    return email in authorized


def get_user_data(app):
    ret = app.remote.get("user", token=get_token())
    return ret.data["data"]


def get_token():
    return session.get("dev_token")
