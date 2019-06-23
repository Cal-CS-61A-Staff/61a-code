from flask import Flask, request
import requests

app = Flask(__name__, static_url_path='', static_folder="")


@app.route('/')
def root():
    return app.send_static_file('dist/web/index.html')


# FIXME: DO NOT DEPLOY
@app.route('/api/pytutor', methods=['POST'])
def pytutor_proxy():
    response = requests.post("http://pythontutor.com/web_exec_py3.py", data={
        "user_script": request.form["code"],
    })
    return response.text


if __name__ == "__main__":
    app.run()
