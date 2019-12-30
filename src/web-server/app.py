from flask import Flask, render_template, send_from_directory

from IGNORE_secrets import SECRET
from constants import STATIC_FOLDER

from interpreter_links import create_interpreter_links
from language_apis import create_language_apis
from oauth_client import create_oauth_client
from refresher import create_refresher
from shortlink_generator import create_shortlink_generator
from shortlink_handler import create_shortlink_handler

app = Flask(__name__, template_folder=STATIC_FOLDER)
app.secret_key = SECRET


@app.route("/")
def root():
    return render_template("index.html", initData={})


@app.route("/service-worker.js")
def serviceworker():
    return send_from_directory(STATIC_FOLDER, "service-worker.js")


app.load_file = create_shortlink_handler(app)
app.check_auth = create_oauth_client(app)

create_refresher(app)
create_shortlink_generator(app)
create_interpreter_links(app)
create_language_apis(app)

if __name__ == "__main__":
    app.run()
