import csv

import requests

from constants import CSV_ROOT
from db import connect_db
from refresher import setup

CSV_SHORTLINKS_PATHS_SUFFIX = (
    "/export?format=csv&id=1-1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI&gid=355056023"
)


@setup
def setup_shortlink_paths():
    response = requests.get(CSV_ROOT + CSV_SHORTLINKS_PATHS_SUFFIX)
    parsed = csv.reader(response.text.split("\n"))
    next(parsed)  # discard headers
    paths = [[x[0]] for x in parsed]
    with connect_db() as db:
        db("DROP TABLE IF EXISTS linkPaths")
        db("CREATE TABLE linkPaths (path varchar(256))")
        db("INSERT INTO linkPaths VALUES (%s)", paths)
