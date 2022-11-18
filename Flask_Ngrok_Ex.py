import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import request, jsonify, Flask
import random as rk

app = Flask(__name__)  # the name of the application package
run_with_ngrok(app)

planilha_json = {
    "1": {
        "name": "Mahesh",
        "Age": 25,
        "City": "Bangalore",
        "Country": "India"
    },
    "2": {
        "name": "Alex",
        "Age": 26,
        "City": "London",
        "Country": "UK"
    },
    "3": {
        "name": "David",
        "Age": 27,
        "City": "San Francisco",
        "Country": "USA"
    },
    "4": {
        "name": "John",
        "Age": 28,
        "City": "Toronto",
        "Country": "Canada"
    },
    "5": {
        "name": "Chris",
        "Age": 29,
        "City": "Paris",
        "Country": "France"
    }
}


@app.route("/")  # code to assign HomePage URL in our app to function home.
def home():
    """
    The entire line below must be written in a single line.
    """
    return planilha_json


@app.route("/input")  # code to assign Input URL in our app to function input.
def input():
    return jsonify(planilha_json)  # "d" is the dictionary we defined


@app.route('/output', methods=['GET', 'POST'])  # output page
def predJson():
    pred = r.choice(["positive", "negative"])
    nd = planilha_json  # our input
    nd["prediction"] = pred
    return jsonify(nd)


app.run()
