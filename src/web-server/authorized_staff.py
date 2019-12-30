import csv

import requests

from constants import CSV_ROOT
from db import connect_db
from refresher import setup

CSV_AUTHORIZED_SUFFIX = "/export?format=csv&id=1-1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI&gid=1240767129"


@setup
def setup_authorized_staff():
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
        db("CREATE TABLE authorized (email varchar(128))")
        db("INSERT INTO authorized VALUES (%s)", authorized)
