import random

from flask import request, abort

from english_words import english_words_set as words  # list of words to generate links

from db import connect_db


def create_shortlink_generator(app):
    def save_file(db_name):
        file_name, file_content = request.form["fileName"], request.form["fileContent"]
        with connect_db() as db:
            link = "".join(random.sample(words, 1)[0].title() for _ in range(3))
            db(
                f"INSERT INTO {db_name} VALUES (%s, %s, %s)",
                [link, file_name, file_content],
            )
        return "code.cs61a.org/" + link

    @app.route("/api/share", methods=["POST"])
    def share():
        return save_file("studentLinks")

    @app.route("/api/staff_share", methods=["POST"])
    def staff_share():
        if not app.check_auth():
            abort(403)

        return save_file("staffLinks")


def setup_shortlink_generator():
    with connect_db() as db:
        db(
            """CREATE TABLE IF NOT EXISTS studentLinks (
           link varchar(128),
           fileName varchar(128),
           fileContent BLOB)"""
        )
        db(
            """CREATE TABLE IF NOT EXISTS staffLinks (
           link varchar(128),
           fileName varchar(128),
           fileContent BLOB)"""
        )
