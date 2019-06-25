from flask import Flask, request, jsonify
import requests
import black

app = Flask(__name__, static_url_path='', static_folder="")


@app.route('/')
def root():
    return app.send_static_file('./index.html')


# FIXME: DO NOT DEPLOY
@app.route('/api/pytutor', methods=['POST'])
def pytutor_proxy():
    response = requests.post("http://pythontutor.com/web_exec_py3.py", data={
        "user_script": request.form["code"],
    })
    return response.text


@app.route("/api/black", methods=["POST"])
def black_proxy():
    try:
        return jsonify({"success": True, "code": black.format_str(request.form["code"], mode=black.FileMode()) + "\n"})
    except Exception as e:
        return jsonify({"success": False, "error": repr(e)})


if __name__ == "__main__":
    app.run()
