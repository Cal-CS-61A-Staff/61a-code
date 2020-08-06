import csv
import re
from base64 import b64encode, b64decode

import requests
from flask import jsonify

from constants import CSV_ROOT
from db import connect_db

CSV_PRELOADED_TABLES_SUFFIX = "/export?format=csv&id=1-1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI&gid=1808429477"


def create_preloaded_tables(app):
    @app.route("/api/preloaded_tables", methods=["POST"])
    def preloaded_tables():
        try:
            with connect_db() as db:
                return jsonify(
                    {
                        "success": True,
                        "data": b64decode(
                            db("SELECT data FROM preloaded_tables").fetchone()[0]
                        ).decode("utf-8"),
                    }
                )
        except Exception as e:
            print(e)
            return jsonify({"success": False, "data": ""})


def setup_preloaded_tables():
    # refresh SQL preloaded tables
    response = requests.get(CSV_ROOT + CSV_PRELOADED_TABLES_SUFFIX)
    parsed = csv.reader(response.text.split("\n"))
    next(parsed)  # discard headers
    init_sql = []
    for line in parsed:
        url, *_ = line
        resp = requests.get(url)
        if resp.status_code == 200:
            init_sql.append(resp.text)
    with connect_db() as db:
        joined_sql = "\n\n".join(init_sql)
        joined_sql = re.sub(
            r"create\s+table(?!\s+if\b)",
            "CREATE TABLE IF NOT EXISTS ",
            joined_sql,
            flags=re.IGNORECASE,
        )
        encoded = b64encode(bytes(joined_sql, "utf-8"))
        db("DROP TABLE IF EXISTS preloaded_tables")
        db("CREATE TABLE preloaded_tables (data LONGBLOB)")
        db("INSERT INTO preloaded_tables VALUES (%s)", [encoded])
