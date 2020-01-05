from flask import request, jsonify

from oauth_utils import get_user_data, get_token


def create_ok_server_interface(app):
    @app.route("/api/get_backups", methods=["POST"])
    def get_backups():
        endpoint = request.form["endpoint"]
        email = get_user_data(app)["email"]
        email = "takaokakegawa@berkeley.edu"
        resp = app.remote.get(
            "assignment/{}/export/{}?limit=1".format(endpoint, email)
        ).data
        return jsonify(resp)

    @app.route("/api/list_assignments", methods=["POST"])
    def list_assignments():
        return jsonify(
            app.remote.get("course/cal/cs61a/fa19/assignments", token=get_token()).data
        )
