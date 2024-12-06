from flask import Flask, jsonify, render_template
from pymongo import MongoClient
import json
from bson import json_util

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
    clean_data = json.loads(json_util.dumps(data))  # Convert to JSON-compatible format
    # print(data)
    return jsonify(clean_data)


if __name__ == "__main__":
    app.run(debug=True)
