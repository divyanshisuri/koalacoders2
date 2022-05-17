# import "packages" from flask
from flask import Flask, render_template, request
import os
import requests
import json
from requests import get
import random

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html", darkmode=darkmode)


@app.route('/platformer/')
def platformer():
    return render_template("platformer.html")

@app.route('/map/')
def map():
    return render_template("map.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True,port=8080)
