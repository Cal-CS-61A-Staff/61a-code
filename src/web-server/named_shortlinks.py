import csv

import requests
from flask import abort

from constants import ServerFile, CSV_ROOT
from db import connect_db
from refresher import setup

CSV_SHORTLINKS_SUFFIX = (
    "/export?format=csv&id=1-1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI&gid=0"
)


@setup
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
