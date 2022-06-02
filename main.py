# import "packages" from flask
from flask import Flask, render_template, request


from __init__ import app

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
    return render_template("index.html")


@app.route('/platformer/')
def platformer():
    return render_template("platformer.html")

@app.route('/login/')
def login():
    return render_template("login.html")

@app.route('/database/')
def database():
    return render_template("database.html")

@app.route('/map/')
def map():
    return render_template("map.html")

@app.route('/dailychecklist/')
def dailychecklist():
    return render_template("dailychecklist.html")

@app.route('/snake/')
def snake():
    return render_template("snake.html")


@app.route('/gradecalc/')
def gradecalc():
    return render_template("gradecalc.html")

@app.route('/spinningwheel/')
def spinningwheel():
    return render_template("spinningwheel.html")

@app.route('/weather/')
def weather():
    return render_template("weather.html")

@app.route('/blog/')
def blog():
    return render_template("upload.html")

@app.route('/calculator/')
def calculator():
    return render_template("calculator.html")

@app.route('/whiteboard/')
def whiteboard():
    return render_template("whiteboard.html")

@app.route('/calendar/')
def calendar():
    return render_template("calendar.html")

@app.route('/crud/')
def crud():
    return render_template("crud.html")



@app.route('/budget/')
def budget():
    return render_template("budget.html")


@app.route('/grocerylist/')
def grocerylist():
    return render_template("grocerylist.html")








# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True,port=8000)
