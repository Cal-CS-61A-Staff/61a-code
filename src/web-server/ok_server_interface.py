from flask import request, jsonify

from oauth_utils import get_user_data

SEMESTER = "fa19"


def create_ok_server_interface(app):
    @app.route("/api/get_backups", methods=["POST"])
    def get_backups():
        endpoint = request.form["endpoint"]
        email = get_user_data(app)["email"]
        resp = app.remote.get(
            "assignment/{}/export/{}?limit=1".format(endpoint, email)
        ).data
        return jsonify(resp)

    @app.route("/api/list_assignments", methods=["POST"])
    def list_assignments():
        return jsonify(
            app.remote.get("course/cal/cs61a/{}/assignments".format(SEMESTER)).data
        )

    @app.route("/api/save_backup", methods=["POST"])
    def save_backup():
        file_name = request.form["file"]
        file_content = request.form["content"]
        assignment = request.form["assignment"]

        email = get_user_data(app)["email"]
        endpoint = "cal/cs61a/{}/{}".format(SEMESTER, assignment)

        ret = app.remote.get(
            "assignment/{}/export/{}?limit=1".format(endpoint, email)
        ).data

        backups = ret["data"]["backups"]

        files = {file_name: file_content}

        if len(backups) > 0:
            assert len(backups) == 1
            messages = backups[0]["messages"]
            for message in messages:
                if message["kind"] == "file_contents":
                    for name, content in message["contents"].items():
                        if name == "submit":
                            continue
                        if name in files:
                            continue
                        files[name] = content

        ret = app.remote.post(
            "backups/",
            data={
                "assignment": endpoint,
                "submit": False,
                "messages": {"file_contents": files},
            },
            format="json",
        ).data

        return jsonify({"success": ret["message"] == "success"})
