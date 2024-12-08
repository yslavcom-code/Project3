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
@app.route('/api/economic-data')
def get_economic_data():
    # Get the parameters sent by the user's selections
    countries = request.args.getlist('countries[]')  
    indicator = request.args.get('indicator', 'GDP')  
    
    # Connect to our database
    db = connect_to_database()
    collection = db["cleaned_economic_data"]
    
    # Set up our database query
    query = {"indicator_type": indicator}
    
    # Specify which fields we want to get from the database
    projection = {
        "year": 1,    # We always need the year
        "_id": 0      # We don't need MongoDB's internal ID
    }
    
    # Add each selected country to our projection
    for country in countries:
        projection[country] = 1
        
    # Get the data and sort it by year
    data = list(collection.find(query, projection).sort("year", 1))
    
    # Send the data back to the webpage
    return jsonify({"data": data})
if __name__ == '__main__':
    app.run(debug=True, port=5000)
