import csv
import os

import requests

from auth import read_spreadsheet
from constants import CSV_ROOT
from db import connect_db


def attempt_shortlink_paths(path):
    with connect_db() as db:
        base_paths = db(
            "SELECT candidate_path, requested_path FROM linkPaths"
        ).fetchall()
        for candidate_path, requested_path in base_paths:
            if not path.startswith(requested_path):
                continue
            trunc_path = path[len(requested_path) :]
            url = os.path.join(candidate_path, trunc_path)
            data = requests.get(url)
            if data.ok:
                text = data.text
                if path.endswith(".sql"):
                    text = ".open --new\n\n" + text
                return {"full_name": trunc_path, "data": text, "share_ref": None}


def setup_shortlink_paths():
    parsed = read_spreadsheet("Shortlink Paths")
    next(parsed)  # discard headers
    paths = []
    for candidate_path, requested_path, *_ in parsed:
        if requested_path.startswith("/"):
            requested_path = requested_path[1:]
        if requested_path and not requested_path.endswith("/"):
            requested_path += "/"
        paths.append([candidate_path, requested_path])
    with connect_db() as db:
        db("DROP TABLE IF EXISTS linkPaths")
        db(
            "CREATE TABLE linkPaths (candidate_path varchar(256), requested_path varchar(256))"
        )
        db("INSERT INTO linkPaths VALUES (%s, %s)", paths)
