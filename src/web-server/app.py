from flask import Flask, request
import requests

app = Flask(__name__)


# FIXME: DO NOT DEPLOY, unless you want Prof. Guo to be _very_ angry :P
@app.route('/api/pytutor', methods=['POST'])
def pytutor_proxy():
    response = requests.post("http://pythontutor.com/web_exec_py3.py", data={
        "user_script": request.form["code"],
    })
    return response.text


if __name__ == "__main__":
    app.run()
