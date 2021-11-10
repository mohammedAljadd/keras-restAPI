from flask.globals import request
from app import app
from flask import render_template


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def result():
    return render_template("result.html")