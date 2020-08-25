from os import getenv
from urllib.parse import urljoin

import requests

from constants import CSV_ROOT

HOST = "https://auth.cs61a.org"


def query(endpoint, *, course, **kwargs):
    return requests.post(
        urljoin(HOST, endpoint),
        json={"secret": getenv("AUTH_KEY"), "course": course, **kwargs},
    ).json()


def read_spreadsheet(sheet_name):
    return iter(
        query(
            "google/read_spreadsheet",
            course="cs61a",
            url=CSV_ROOT,
            sheet_name=sheet_name,
        )
    )
