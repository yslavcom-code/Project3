from pymongo import MongoClient
import pandas as pd

mongo = MongoClient(port=27017)

def save_to_db(db_handle, file_path, db_name, collection_name):   
    df = pd.read_excel(file_path)
    df.fillna(None, inplace=True)  # Replace NaN with None for MongoDB compatibility
    db = db_handle[db_name]  # Specify the database name
    collection = db[collection_name]  # Specify the collection name
    data = df.to_dict("records")  # Convert the DataFrame to a list of dictionaries
    collection.insert_many(data)
    
file_path = "../ResourceIar/GDP Deflator at Market Prices, LCU.xlsx"
db_name = "economic_data"
save_to_db(mongo, file_path, db_name)