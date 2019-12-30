import os
from collections import namedtuple

COOKIE_IS_POPUP = "is_popup"
COOKIE_SHORTLINK_REDIRECT = "shortlink"
STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
ServerFile = namedtuple(
    "ServerFile", ["short_link", "full_name", "url", "data", "discoverable"]
)
