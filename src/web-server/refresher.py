from multiprocessing import Process, active_children

from flask import redirect

from constants import CSV_ROOT


def create_refresher(app):
    @app.route("/data/registry")
    def registry():
        return redirect(CSV_ROOT)

    @app.route("/data/refresh")
    def sync_refresh():
        refresh()
        return (
            "Success! All public shortlinks, members of staff, and stored files successfully updated!",
            200,
        )

    @app.route("/api/async_refresh", methods=["POST"])
    @app.route("/api/_async_refresh", methods=["POST"])  # deprecated
    def async_refresh():
        active_children()  # kills zombies
        p = Process(target=refresh)
        p.start()
        return "", 204

    def refresh():
        for f in setup_funcs:
            f()

    refresh()


setup_funcs = []


def setup(f):
    setup_funcs.append(f)
    return f
