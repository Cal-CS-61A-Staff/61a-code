import csv
import os

import requests

from constants import CSV_ROOT
from db import connect_db

CSV_SHORTLINKS_PATHS_SUFFIX = (
    "/export?format=csv&id=1-1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI&gid=355056023"
)


def attempt_shortlink_paths(path):
    with connect_db() as db:
        base_paths = db("SELECT * FROM linkPaths").fetchall()
        for base_path, *_ in base_paths:
            url = os.path.join(base_path, path)
            data = requests.get(url)
            if data.ok:
                text = data.text
                if path.endswith(".sql"):
                    text = ".open --new\n\n" + text
                return {"full_name": path, "data": text}


def setup_shortlink_paths():
    response = requests.get(CSV_ROOT + CSV_SHORTLINKS_PATHS_SUFFIX)
    parsed = csv.reader(response.text.split("\n"))
    next(parsed)  # discard headers
    paths = [[x[0]] for x in parsed]
    with connect_db() as db:
        db("DROP TABLE IF EXISTS linkPaths")
        db("CREATE TABLE linkPaths (path varchar(256))")
        db("INSERT INTO linkPaths VALUES (%s)", paths)
