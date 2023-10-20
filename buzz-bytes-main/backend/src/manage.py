from flask import Flask, render_template, redirect, request, abort, jsonify
from src.gpt.gpt import apiCall

app = Flask(__name__)
app.json.sort_keys = False

VALID_LOCATIONS = ["west-village", "north-ave-dining-hall", "brittain"]
VALID_MEALS = ["breakfast", "lunch", "dinner"]

@app.route("/api/<location>/<meal>/<targetCalories>/<dietaryRestrictions>")
def getUserData(location, meal, targetCalories, dietaryRestrictions):
    print(location, meal, targetCalories, dietaryRestrictions)
    if (location in VALID_LOCATIONS) and (meal in VALID_MEALS):
        print("processing started")
        data = apiCall(location, meal, targetCalories, dietaryRestrictions)
        return jsonify(data)

    return abort(404)