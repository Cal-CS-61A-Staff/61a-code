import csv

import requests

from constants import ServerFile, CSV_ROOT
from db import connect_db

CSV_SHORTLINKS_SUFFIX = (
    "/export?format=csv&id=1-1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI&gid=0"
)


def attempt_named_shortlinks(path):
    with connect_db() as db:
        ret = db("SELECT * FROM links WHERE short_link=%s;", [path]).fetchone()
        if ret is not None:
            return ServerFile(ret[0], ret[1], ret[2], ret[3].decode(), ret[4])._asdict()


def setup_named_shortlinks():
    response = requests.get(CSV_ROOT + CSV_SHORTLINKS_SUFFIX)
    parsed = csv.reader(response.text.split("\n"))
    next(parsed)  # discard headers
    all_files = []
    for line in parsed:
        short_link, full_name, url, discoverable, *_ = line
        data = requests.get(url).text
        file = ServerFile(short_link, full_name, url, data, int(discoverable == "TRUE"))
        all_files.append(file)

    with connect_db() as db:
        db("DROP TABLE IF EXISTS links")
        db(
            """CREATE TABLE links (
    short_link varchar(128), 
    full_name varchar(128), 
    url varchar(1024), 
    data LONGBLOB, 
    discoverable BOOLEAN)"""
        )
        db("INSERT INTO links VALUES (%s, %s, %s, %s, %s)", all_files)
