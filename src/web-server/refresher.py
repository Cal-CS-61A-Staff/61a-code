import csv
import re
from base64 import b64encode
from multiprocessing import active_children, Process
from flask import redirect

import requests

from constants import ServerFile
from db import connect_db

CSV_ROOT = "https://docs.google.com/spreadsheets/d/1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI"

CSV_SHORTLINKS_SUFFIX = (
    "/export?format=csv&id=1-1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI&gid=0"
)

CSV_SHORTLINKS_PATHS_SUFFIX = (
    "/export?format=csv&id=1-1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI&gid=355056023"
)

CSV_AUTHORIZED_SUFFIX = "/export?format=csv&id=1-1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI&gid=1240767129"

CSV_STORED_FILES_SUFFIX = (
    "/export?format=csv&id=1-1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI&gid=169284641"
)

CSV_PRELOADED_TABLES_SUFFIX = "/export?format=csv&id=1-1v3N9fak7a-pf70zBhAIUuzplRw84NdLP5ptrhq_fKnI&gid=1808429477"


def create_refresher(app):
    @app.route("/api/_registry")
    def registry():
        return redirect(CSV_ROOT)

    @app.route("/api/_refresh")
    def sync_refresh():
        refresh()
        return (
            "Success! All public shortlinks, members of staff, and stored files successfully updated!",
            200,
        )

    @app.route("/api/_async_refresh", methods=["POST"])
    def async_refresh():
        active_children()  # kills zombies
        p = Process(target=refresh)
        p.start()
        return "", 204

    def refresh():
        # refresh shortlinks
        response = requests.get(CSV_ROOT + CSV_SHORTLINKS_SUFFIX)
        parsed = csv.reader(response.text.split("\n"))
        next(parsed)  # discard headers
        all_files = []
        for line in parsed:
            short_link, full_name, url, discoverable, *_ = line
            data = requests.get(url).text
            file = ServerFile(
                short_link, full_name, url, data, int(discoverable == "TRUE")
            )
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

        # load shortlink paths
        response = requests.get(CSV_ROOT + CSV_SHORTLINKS_PATHS_SUFFIX)
        parsed = csv.reader(response.text.split("\n"))
        next(parsed)  # discard headers
        paths = [[x[0]] for x in parsed]
        with connect_db() as db:
            db("DROP TABLE IF EXISTS linkPaths")
            db("CREATE TABLE linkPaths (path varchar(256))")
            db("INSERT INTO linkPaths VALUES (%s)", paths)

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

        # refresh stored files
        response = requests.get(CSV_ROOT + CSV_STORED_FILES_SUFFIX)
        parsed = csv.reader(response.text.split("\n"))
        next(parsed)  # discard headers
        stored_files = []
        for line in parsed:
            file_name, url, *_ = line
            data = requests.get(url).text
            stored_files.append([file_name, data])

        with connect_db() as db:
            db("DROP TABLE IF EXISTS stored_files")
            db(
                "CREATE TABLE stored_files (file_name varchar(128), file_contents LONGBLOB)"
            )
            db("INSERT INTO stored_files VALUES (%s, %s)", stored_files)

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
