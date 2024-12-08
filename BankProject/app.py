from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

def connect_to_database():
    client = MongoClient(port=27017)
    return client["bank_project"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/countries')
def get_countries():
    # Using your existing MongoDB data
    db = connect_to_database()
    collection = db["cleaned_economic_data"]
    sample = collection.find_one({"indicator_type": "GDP"})
    countries = [key for key in sample.keys() 
                if key not in ['_id', 'year', 'indicator_type', 
                             'file_source', 'seasonally_adjusted']]
    return jsonify({"countries": sorted(countries)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)