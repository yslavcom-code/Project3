from flask import Flask, jsonify, render_template, url_for  
from pymongo import MongoClient
import json
from bson import json_util
import os

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

@app.route('/world-map')
def world_map():
    return render_template('map.html')


@app.route('/soheil')
def soheil_page():
    # Dynamically read images from SoheilFolder
    folder_path = os.path.join(app.static_folder, "SoheilFolder")
    image_urls = [url_for('static', filename=f"SoheilFolder/{file}") for file in os.listdir(folder_path) if file.endswith(('png', 'jpg', 'jpeg', 'gif'))]
    return render_template("gallery.html", images=image_urls, folder_name="SoheilFolder")


@app.route('/jane')
def jane_page():
    # Dynamically read images from JaneFolder
    folder_path = os.path.join(app.static_folder, "JaneFolder")
    image_urls = [url_for('static', filename=f"JaneFolder/{file}") for file in os.listdir(folder_path) if file.endswith(('png', 'jpg', 'jpeg', 'gif'))]
    return render_template("gallery.html", images=image_urls, folder_name="JaneFolder")


@app.route('/loku')
def loku_page():
    # Dynamically read images from LokuFolder
    folder_path = os.path.join(app.static_folder, "LokuFolder")
    image_urls = [url_for('static', filename=f"LokuFolder/{file}") for file in os.listdir(folder_path) if file.endswith(('png', 'jpg', 'jpeg', 'gif'))]
    return render_template("gallery.html", images=image_urls, folder_name="LokuFolder")

@app.route('/example')
def example_page():
    # Dynamically read images from Example
    folder_path = os.path.join(app.static_folder, "ExampleFolder")
    image_urls = [url_for('static', filename=f"ExampleFolder/{file}") for file in os.listdir(folder_path) if file.endswith(('png', 'jpg', 'jpeg', 'gif'))]
    return render_template("gallery.html", images=image_urls, folder_name="ExampleFolder")

if __name__ == "__main__":
    app.run(debug=True)
