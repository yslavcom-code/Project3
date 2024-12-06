from flask import Flask, jsonify, render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client['economic_data']
collection = db['gdp_deflator']


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def get_data():
    # Exclude MongoDB's `_id` field
    data = list(collection.find({}, {'_id': 0}))  
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
