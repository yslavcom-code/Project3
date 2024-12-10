from pymongo import MongoClient
import pandas as pd

def get_db(db_handle, db_name, collection_name):
    db = db_handle[db_name]  # Specify the database name
    collection = db[collection_name]  # Specify the collection name
    
    return db, collection


def save_to_db(file_path, db_handle, db_name, collection_name):   
    df = pd.read_excel(file_path)
    
    #Convert NaN to None (MongoDB-friendly format)
    df = df.where(pd.notnull(df), None)
    
    db, collection = get_db(db_handle, db_name, collection_name)
    collection.delete_many({}) # Delete the existing ones if any
    data = df.to_dict("records")  # Convert the DataFrame to a list of dictionaries
    collection.insert_many(data)

def check_db(db_handle, db_name, collection_name):
    # Check mongoDB
    db, collection = get_db(db_handle, db_name, collection_name)
    #print(f"collection_name: {collection_name}")
    #print(f"document count: {collection.count_documents({})}")
    result = collection.find().limit(5)  # Fetch 5 records for inspection
    #for record in result:
    #    print(record)

def update_from_spreadsheet():
    db_handle = MongoClient(port=27017)
    db_name = "economic_data"
    
    # List of spreadsheet file names
    files = [
        "../ResourceIar/GDP Deflator at Market Prices, LCU.xlsx"
        , "../ResourceIar/GDP at market prices, current US$, millions, seas. adj..xlsx"
        , "../ResourceIar/GDP at market prices, current LCU, millions, seas. adj..xlsx"
        , "../ResourceIar/GDP at market prices, constant 2010 US$, millions, seas. adj..xlsx"
        , "../ResourceIar/GDP at market prices, constant 2010 LCU, millions, seas. adj..xlsx"
    ]

    collection_names = [
        "gdp_deflator",
        "market_prices_current_US",
        "market_prices_current_LCU",
        "market_prices_constant_2010_US",
        "market_prices_constant_2010_LCU",
    ]
    
    [save_to_db(file, db_handle, db_name, collection) for file, collection in zip(files, collection_names)]
    [check_db(db_handle, db_name, collection) for collection in collection_names]
    db_handle.close()
    return "True"
    
def delete_db():
    db_handle = MongoClient(port=27017)
    db_name = "economic_data"
    db_handle.drop_database(db_name)
    return "True"
    
if __name__ == "__main__":
    update_from_spreadsheet()