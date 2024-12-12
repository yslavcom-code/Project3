from flask import Flask, jsonify, render_template, url_for  
from pymongo import MongoClient
import json
from bson import json_util
import os
import subprocess
from read_xlsx import update_from_spreadsheet, delete_db

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client['economic_data']
collection = db['gdp_deflator']


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/update-data", methods=["POST"])
def update_data():
    try:
        result = update_from_spreadsheet()
        return jsonify({"message": "Data updated successfully!", "output": result})
    except subprocess.CalledProcessError as e:
        return jsonify({"message": "Error updating data.", "error": e.stderr}), 500

@app.route("/update-data")
def update_page():
    try:
        result = update_from_spreadsheet()
        return render_template("update_status.html", status="success", message=result)
    except subprocess.CalledProcessError as e:
        return render_template("update_status.html", status="failure", message=e.stderr)

@app.route("/delete-data")
def delete_data_page():
    try:
        result = delete_db()
        return render_template("update_status.html", status="success", message=result)
    except subprocess.CalledProcessError as e:
        return render_template("update_status.html", status="failure", message=e.stderr)

@app.route("/data")
def get_data():
    # Exclude MongoDB's `_id` field
    data = list(collection.find({}, {'_id': 0}))
    clean_data = json.loads(json_util.dumps(data))  # Convert to JSON-compatible format
    # print(data)
    return jsonify(clean_data)

@app.route('/chart_page')
def world_map():
    return render_template('chart_page.html')


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

if __name__ == "__main__":
    update_from_spreadsheet() # Update DB on start for simplicity
    app.run(debug=True)
