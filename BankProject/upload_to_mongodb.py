{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "affc22b7-3a20-4dca-86ec-a6d440a91376",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in e:\\soheil\\lib\\site-packages (2.1.4)\n",
      "Requirement already satisfied: pymongo in e:\\soheil\\lib\\site-packages (4.10.1)\n",
      "Requirement already satisfied: numpy<2,>=1.26.0 in e:\\soheil\\lib\\site-packages (from pandas) (1.26.4)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in e:\\soheil\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in e:\\soheil\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in e:\\soheil\\lib\\site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: dnspython<3.0.0,>=1.16.0 in e:\\soheil\\lib\\site-packages (from pymongo) (2.7.0)\n",
      "Requirement already satisfied: six>=1.5 in e:\\soheil\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas pymongo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "a7dfc122-0234-415b-9582-21c367e68c43",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import pandas as pd\n",
    "from pymongo import MongoClient"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "2dbcdc7a-6c95-435d-ac81-76bed2c7d478",
   "metadata": {},
   "outputs": [],
   "source": [
    "client = MongoClient(port=27017)\n",
    "db = client[\"bank_project\"]\n",
    "collection = db[\"excel_data\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "a4fdb521-a6ee-4691-aa4f-047dfd472058",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Path to the folder containing Excel files\n",
    "excel_folder_path = \"GemDataEXTR\"  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "4b4a8c00-1ae7-44a0-a230-c282c3f2794a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Processing file: Core CPI, not seas. adj..xlsx\n",
      "Inserted 31 records from Core CPI, not seas. adj..xlsx into MongoDB.\n",
      "Processing file: Core CPI, seas. adj..xlsx\n",
      "Inserted 31 records from Core CPI, seas. adj..xlsx into MongoDB.\n",
      "Processing file: CPI Price, % y-o-y, median weighted, seas. adj..xlsx\n",
      "Inserted 31 records from CPI Price, % y-o-y, median weighted, seas. adj..xlsx into MongoDB.\n",
      "Processing file: CPI Price, % y-o-y, nominal, seas. adj..xlsx\n",
      "Inserted 31 records from CPI Price, % y-o-y, nominal, seas. adj..xlsx into MongoDB.\n",
      "Processing file: CPI Price, nominal, not seas. adj..xlsx\n",
      "Inserted 31 records from CPI Price, nominal, not seas. adj..xlsx into MongoDB.\n",
      "Processing file: CPI Price, nominal, seas. adj..xlsx\n",
      "Inserted 31 records from CPI Price, nominal, seas. adj..xlsx into MongoDB.\n",
      "Processing file: Exchange rate, new LCU per USD extended backward, period average.xlsx\n",
      "Inserted 31 records from Exchange rate, new LCU per USD extended backward, period average.xlsx into MongoDB.\n",
      "Processing file: Exchange rate, old LCU per USD extended forward, period average.xlsx\n",
      "Inserted 31 records from Exchange rate, old LCU per USD extended forward, period average.xlsx into MongoDB.\n",
      "Processing file: Exports Merchandise, Customs, constant 2010 US$, millions, not seas. adj..xlsx\n",
      "Inserted 31 records from Exports Merchandise, Customs, constant 2010 US$, millions, not seas. adj..xlsx into MongoDB.\n",
      "Processing file: Exports Merchandise, Customs, constant 2010 US$, millions, seas. adj..xlsx\n",
      "Inserted 31 records from Exports Merchandise, Customs, constant 2010 US$, millions, seas. adj..xlsx into MongoDB.\n",
      "Processing file: Exports Merchandise, Customs, current US$, millions, not seas. adj..xlsx\n",
      "Inserted 31 records from Exports Merchandise, Customs, current US$, millions, not seas. adj..xlsx into MongoDB.\n",
      "Processing file: Exports Merchandise, Customs, current US$, millions, seas. adj..xlsx\n",
      "Inserted 31 records from Exports Merchandise, Customs, current US$, millions, seas. adj..xlsx into MongoDB.\n",
      "Processing file: Exports Merchandise, Customs, Price, US$, not seas. adj..xlsx\n",
      "Inserted 31 records from Exports Merchandise, Customs, Price, US$, not seas. adj..xlsx into MongoDB.\n",
      "Processing file: Exports Merchandise, Customs, Price, US$, seas. adj..xlsx\n",
      "Inserted 31 records from Exports Merchandise, Customs, Price, US$, seas. adj..xlsx into MongoDB.\n",
      "Processing file: Foreign Reserves, Months Import Cover, Goods.xlsx\n",
      "Inserted 31 records from Foreign Reserves, Months Import Cover, Goods.xlsx into MongoDB.\n",
      "Processing file: GDP at market prices, constant 2010 LCU, millions, seas. adj..xlsx\n",
      "Inserted 31 records from GDP at market prices, constant 2010 LCU, millions, seas. adj..xlsx into MongoDB.\n",
      "Processing file: GDP at market prices, constant 2010 US$, millions, seas. adj..xlsx\n",
      "Inserted 31 records from GDP at market prices, constant 2010 US$, millions, seas. adj..xlsx into MongoDB.\n",
      "Processing file: GDP at market prices, current LCU, millions, seas. adj..xlsx\n",
      "Inserted 31 records from GDP at market prices, current LCU, millions, seas. adj..xlsx into MongoDB.\n",
      "Processing file: GDP at market prices, current US$, millions, seas. adj..xlsx\n",
      "Inserted 31 records from GDP at market prices, current US$, millions, seas. adj..xlsx into MongoDB.\n",
      "Processing file: GDP Deflator at Market Prices, LCU.xlsx\n",
      "Inserted 121 records from GDP Deflator at Market Prices, LCU.xlsx into MongoDB.\n",
      "Processing file: Imports Merchandise, Customs, constant 2010 US$, millions, not seas. adj..xlsx\n",
      "Inserted 31 records from Imports Merchandise, Customs, constant 2010 US$, millions, not seas. adj..xlsx into MongoDB.\n",
      "Processing file: Imports Merchandise, Customs, constant 2010 US$, millions, seas. adj..xlsx\n",
      "Inserted 31 records from Imports Merchandise, Customs, constant 2010 US$, millions, seas. adj..xlsx into MongoDB.\n",
      "Processing file: Imports Merchandise, Customs, current US$, millions, not seas. adj..xlsx\n",
      "Inserted 31 records from Imports Merchandise, Customs, current US$, millions, not seas. adj..xlsx into MongoDB.\n",
      "Processing file: Imports Merchandise, Customs, current US$, millions, seas. adj..xlsx\n",
      "Inserted 31 records from Imports Merchandise, Customs, current US$, millions, seas. adj..xlsx into MongoDB.\n",
      "Processing file: Imports Merchandise, Customs, Price, US$, not seas. adj..xlsx\n",
      "Inserted 31 records from Imports Merchandise, Customs, Price, US$, not seas. adj..xlsx into MongoDB.\n",
      "Processing file: Imports Merchandise, Customs, Price, US$, seas. adj..xlsx\n",
      "Inserted 31 records from Imports Merchandise, Customs, Price, US$, seas. adj..xlsx into MongoDB.\n",
      "Processing file: Industrial Production, constant 2010 US$, not seas. adj..xlsx\n",
      "Inserted 31 records from Industrial Production, constant 2010 US$, not seas. adj..xlsx into MongoDB.\n",
      "Processing file: Industrial Production, constant 2010 US$, seas. adj..xlsx\n",
      "Inserted 31 records from Industrial Production, constant 2010 US$, seas. adj..xlsx into MongoDB.\n",
      "Processing file: Nominal Effective Exchange Rate.xlsx\n",
      "Inserted 31 records from Nominal Effective Exchange Rate.xlsx into MongoDB.\n",
      "Processing file: Official exchange rate, LCU per USD, period average.xlsx\n",
      "Inserted 31 records from Official exchange rate, LCU per USD, period average.xlsx into MongoDB.\n",
      "Processing file: Real Effective Exchange Rate.xlsx\n",
      "Inserted 31 records from Real Effective Exchange Rate.xlsx into MongoDB.\n",
      "Processing file: Retail Sales Volume Index, seas. adj..xlsx\n",
      "Inserted 31 records from Retail Sales Volume Index, seas. adj..xlsx into MongoDB.\n",
      "Processing file: Stock Markets, LCU.xlsx\n",
      "Inserted 31 records from Stock Markets, LCU.xlsx into MongoDB.\n",
      "Processing file: Stock Markets, US$.xlsx\n",
      "Inserted 31 records from Stock Markets, US$.xlsx into MongoDB.\n",
      "Processing file: Terms of Trade.xlsx\n",
      "Inserted 361 records from Terms of Trade.xlsx into MongoDB.\n",
      "Processing file: Total Reserves.xlsx\n",
      "Inserted 31 records from Total Reserves.xlsx into MongoDB.\n",
      "Processing file: Unemployment Rate, seas. adj..xlsx\n",
      "Inserted 31 records from Unemployment Rate, seas. adj..xlsx into MongoDB.\n",
      "All files processed and uploaded to MongoDB!\n"
     ]
    }
   ],
   "source": [
    "# Iterate through all Excel files in the folder\n",
    "for file_name in os.listdir(excel_folder_path):\n",
    "    if file_name.endswith(\".xlsx\"):  # Only process Excel files\n",
    "        file_path = os.path.join(excel_folder_path, file_name)\n",
    "        print(f\"Processing file: {file_name}\")\n",
    "        \n",
    "        # Load the Excel file into a Pandas DataFrame\n",
    "        df = pd.read_excel(file_path)\n",
    "        \n",
    "        # Convert DataFrame to a list of dictionaries (JSON format for MongoDB)\n",
    "        data = df.to_dict(orient=\"records\")\n",
    "        \n",
    "        # Insert data into the MongoDB collection\n",
    "        collection.insert_many(data)\n",
    "        print(f\"Inserted {len(data)} records from {file_name} into MongoDB.\")\n",
    "\n",
    "print(\"All files processed and uploaded to MongoDB!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "f5bdbdcd-6e53-46ad-9337-2320023e213d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': ObjectId('674faa118b1c62f59177bae6'), 'Unnamed: 0': nan, 'Albania': nan, 'Armenia': nan, 'Belgium': nan, 'Belarus': nan, 'Brazil': nan, 'Canada': nan, 'Switzerland': nan, 'Chile': nan, 'China': nan, 'Cameroon': nan, 'Colombia': nan, 'Costa Rica': nan, 'Cyprus': nan, 'Czech Republic': nan, 'Germany': nan, 'Denmark': nan, 'Dominican Republic': nan, 'Ecuador': nan, 'Egypt, Arab Rep.': nan, 'Spain': nan, 'Fiji': nan, 'France': nan, 'United Kingdom': nan, 'Georgia': nan, 'Greece': nan, 'Guatemala': nan, 'Hong Kong SAR, China': nan, 'Honduras': nan, 'Croatia': nan, 'Hungary': nan, 'Indonesia': nan, 'India': nan, 'Ireland': nan, 'Iraq': nan, 'Iceland': nan, 'Israel': nan, 'Italy': nan, 'Jordan': nan, 'Japan': nan, 'Kyrgyz Republic': nan, 'Korea, Rep.': nan, 'Kuwait': nan, 'Lao, PDR': nan, 'Sri Lanka': nan, 'Lithuania': nan, 'Luxembourg': nan, 'Latvia': nan, 'Morocco': nan, 'Moldova, Rep.': nan, 'Mexico': nan, 'North Macedonia': nan, 'Malta': nan, 'Mauritius': nan, 'Malaysia': nan, 'Nigeria': nan, 'Nicaragua': nan, 'Netherlands': nan, 'Norway': nan, 'Peru': nan, 'Philippines': nan, 'Poland': nan, 'Portugal': nan, 'Paraguay': nan, 'Qatar': nan, 'Romania': nan, 'Russian Federation': nan, 'Saudi Arabia': nan, 'Senegal': nan, 'Singapore': nan, 'El Salvador': nan, 'Slovakia': nan, 'Slovenia': nan, 'Sweden': nan, 'Seychelles': nan, 'Chad': nan, 'Togo': nan, 'Thailand': nan, 'Trinidad and Tobago': nan, 'Turkey': nan, 'Taiwan, China': nan, 'Tanzania, United Rep.': nan, 'Uganda': nan, 'Uruguay': nan, 'United States': nan, 'Viet Nam': nan, 'Kosovo': nan, 'South Africa': nan}\n",
      "{'_id': ObjectId('674faa118b1c62f59177bae7'), 'Unnamed: 0': 1995.0, 'Albania': nan, 'Armenia': nan, 'Belgium': nan, 'Belarus': nan, 'Brazil': 37.98033, 'Canada': 79.53256, 'Switzerland': nan, 'Chile': nan, 'China': nan, 'Cameroon': nan, 'Colombia': nan, 'Costa Rica': nan, 'Cyprus': nan, 'Czech Republic': nan, 'Germany': nan, 'Denmark': nan, 'Dominican Republic': nan, 'Ecuador': nan, 'Egypt, Arab Rep.': nan, 'Spain': nan, 'Fiji': nan, 'France': nan, 'United Kingdom': 79.56381, 'Georgia': nan, 'Greece': nan, 'Guatemala': nan, 'Hong Kong SAR, China': nan, 'Honduras': nan, 'Croatia': nan, 'Hungary': 35.15982, 'Indonesia': nan, 'India': nan, 'Ireland': nan, 'Iraq': nan, 'Iceland': nan, 'Israel': 64.69824, 'Italy': nan, 'Jordan': nan, 'Japan': 103.051, 'Kyrgyz Republic': nan, 'Korea, Rep.': 66.38717, 'Kuwait': nan, 'Lao, PDR': nan, 'Sri Lanka': nan, 'Lithuania': nan, 'Luxembourg': nan, 'Latvia': nan, 'Morocco': nan, 'Moldova, Rep.': nan, 'Mexico': 27.91926, 'North Macedonia': nan, 'Malta': nan, 'Mauritius': nan, 'Malaysia': nan, 'Nigeria': 23.98342, 'Nicaragua': nan, 'Netherlands': nan, 'Norway': nan, 'Peru': 58.29995, 'Philippines': nan, 'Poland': nan, 'Portugal': nan, 'Paraguay': 35.40767, 'Qatar': nan, 'Romania': nan, 'Russian Federation': nan, 'Saudi Arabia': nan, 'Senegal': nan, 'Singapore': 81.00394, 'El Salvador': nan, 'Slovakia': nan, 'Slovenia': nan, 'Sweden': nan, 'Seychelles': nan, 'Chad': nan, 'Togo': nan, 'Thailand': 79.15027, 'Trinidad and Tobago': 71.87268, 'Turkey': nan, 'Taiwan, China': 91.1974, 'Tanzania, United Rep.': nan, 'Uganda': nan, 'Uruguay': nan, 'United States': 73.2441, 'Viet Nam': nan, 'Kosovo': nan, 'South Africa': nan}\n",
      "{'_id': ObjectId('674faa118b1c62f59177bae8'), 'Unnamed: 0': 1996.0, 'Albania': nan, 'Armenia': nan, 'Belgium': 83.16487, 'Belarus': nan, 'Brazil': 44.82968, 'Canada': 80.71983, 'Switzerland': nan, 'Chile': nan, 'China': nan, 'Cameroon': nan, 'Colombia': nan, 'Costa Rica': nan, 'Cyprus': 81.95864, 'Czech Republic': nan, 'Germany': 86.12581, 'Denmark': 80.36419, 'Dominican Republic': nan, 'Ecuador': nan, 'Egypt, Arab Rep.': nan, 'Spain': 72.21055, 'Fiji': nan, 'France': 82.92024, 'United Kingdom': 81.45947, 'Georgia': nan, 'Greece': 63.7778, 'Guatemala': nan, 'Hong Kong SAR, China': nan, 'Honduras': nan, 'Croatia': nan, 'Hungary': 43.00863, 'Indonesia': nan, 'India': nan, 'Ireland': 73.25017, 'Iraq': nan, 'Iceland': 52.07095, 'Israel': 71.747, 'Italy': 75.82237, 'Jordan': nan, 'Japan': 103.5497, 'Kyrgyz Republic': nan, 'Korea, Rep.': 69.72277, 'Kuwait': nan, 'Lao, PDR': nan, 'Sri Lanka': nan, 'Lithuania': nan, 'Luxembourg': 75.45563, 'Latvia': 52.60635, 'Morocco': nan, 'Moldova, Rep.': nan, 'Mexico': 37.19717, 'North Macedonia': nan, 'Malta': 75.52807, 'Mauritius': nan, 'Malaysia': nan, 'Nigeria': 29.73753, 'Nicaragua': nan, 'Netherlands': 78.94688, 'Norway': 80.64398, 'Peru': 64.11183, 'Philippines': nan, 'Poland': nan, 'Portugal': 72.94118, 'Paraguay': 38.77698, 'Qatar': nan, 'Romania': nan, 'Russian Federation': nan, 'Saudi Arabia': nan, 'Senegal': nan, 'Singapore': 82.46011, 'El Salvador': nan, 'Slovakia': nan, 'Slovenia': nan, 'Sweden': 84.77135, 'Seychelles': nan, 'Chad': nan, 'Togo': nan, 'Thailand': 82.04501, 'Trinidad and Tobago': 72.58723, 'Turkey': nan, 'Taiwan, China': 93.8405, 'Tanzania, United Rep.': nan, 'Uganda': nan, 'Uruguay': nan, 'United States': 75.22438, 'Viet Nam': nan, 'Kosovo': nan, 'South Africa': nan}\n",
      "{'_id': ObjectId('674faa118b1c62f59177bae9'), 'Unnamed: 0': 1997.0, 'Albania': nan, 'Armenia': nan, 'Belgium': 84.02403, 'Belarus': nan, 'Brazil': 48.07538, 'Canada': 81.96685, 'Switzerland': nan, 'Chile': nan, 'China': nan, 'Cameroon': nan, 'Colombia': nan, 'Costa Rica': nan, 'Cyprus': 83.56157, 'Czech Republic': nan, 'Germany': 87.2925, 'Denmark': 81.54826, 'Dominican Republic': nan, 'Ecuador': nan, 'Egypt, Arab Rep.': nan, 'Spain': 74.31408, 'Fiji': nan, 'France': 83.77587, 'United Kingdom': 83.06984, 'Georgia': nan, 'Greece': 68.10691, 'Guatemala': nan, 'Hong Kong SAR, China': nan, 'Honduras': nan, 'Croatia': nan, 'Hungary': 49.99746, 'Indonesia': nan, 'India': nan, 'Ireland': 73.9605, 'Iraq': nan, 'Iceland': 52.65557, 'Israel': 78.07375, 'Italy': 77.66813, 'Jordan': nan, 'Japan': 105.1386, 'Kyrgyz Republic': nan, 'Korea, Rep.': 72.15105, 'Kuwait': nan, 'Lao, PDR': nan, 'Sri Lanka': nan, 'Lithuania': nan, 'Luxembourg': 76.36122, 'Latvia': 61.37552, 'Morocco': nan, 'Moldova, Rep.': nan, 'Mexico': 44.60451, 'North Macedonia': nan, 'Malta': 78.58071, 'Mauritius': nan, 'Malaysia': nan, 'Nigeria': 31.97546, 'Nicaragua': nan, 'Netherlands': 79.86767, 'Norway': 82.23564, 'Peru': 69.76395, 'Philippines': nan, 'Poland': 63.64461, 'Portugal': 74.76827, 'Paraguay': 41.23501, 'Qatar': nan, 'Romania': nan, 'Russian Federation': nan, 'Saudi Arabia': nan, 'Senegal': nan, 'Singapore': 83.73055, 'El Salvador': nan, 'Slovakia': nan, 'Slovenia': nan, 'Sweden': 85.94258, 'Seychelles': nan, 'Chad': nan, 'Togo': nan, 'Thailand': 85.47935, 'Trinidad and Tobago': 73.51522, 'Turkey': nan, 'Taiwan, China': 95.1768, 'Tanzania, United Rep.': nan, 'Uganda': nan, 'Uruguay': nan, 'United States': 77.01913, 'Viet Nam': nan, 'Kosovo': nan, 'South Africa': nan}\n",
      "{'_id': ObjectId('674faa118b1c62f59177baea'), 'Unnamed: 0': 1998.0, 'Albania': nan, 'Armenia': nan, 'Belgium': 85.13964, 'Belarus': nan, 'Brazil': 49.37448, 'Canada': 83.05705, 'Switzerland': nan, 'Chile': nan, 'China': nan, 'Cameroon': nan, 'Colombia': 52.96066, 'Costa Rica': nan, 'Cyprus': 85.75354, 'Czech Republic': 90.41058, 'Germany': 88.20622, 'Denmark': 82.6516, 'Dominican Republic': nan, 'Ecuador': nan, 'Egypt, Arab Rep.': nan, 'Spain': 76.29103, 'Fiji': nan, 'France': 84.53248, 'United Kingdom': 84.48969, 'Georgia': nan, 'Greece': 71.89175, 'Guatemala': nan, 'Hong Kong SAR, China': nan, 'Honduras': nan, 'Croatia': nan, 'Hungary': 56.60071, 'Indonesia': nan, 'India': nan, 'Ireland': 75.4158, 'Iraq': nan, 'Iceland': 53.42846, 'Israel': 82.30126, 'Italy': 79.6144, 'Jordan': nan, 'Japan': 105.8908, 'Kyrgyz Republic': nan, 'Korea, Rep.': 75.6025, 'Kuwait': nan, 'Lao, PDR': nan, 'Sri Lanka': nan, 'Lithuania': nan, 'Luxembourg': 77.30549, 'Latvia': 65.55962, 'Morocco': nan, 'Moldova, Rep.': nan, 'Mexico': 51.80106, 'North Macedonia': nan, 'Malta': 81.93174, 'Mauritius': nan, 'Malaysia': nan, 'Nigeria': 33.35609, 'Nicaragua': nan, 'Netherlands': 81.40848, 'Norway': 84.02854, 'Peru': 74.4671, 'Philippines': nan, 'Poland': 68.81557, 'Portugal': 76.08734, 'Paraguay': 46.28297, 'Qatar': nan, 'Romania': nan, 'Russian Federation': nan, 'Saudi Arabia': nan, 'Senegal': nan, 'Singapore': 84.06186, 'El Salvador': nan, 'Slovakia': nan, 'Slovenia': nan, 'Sweden': 86.86977, 'Seychelles': nan, 'Chad': nan, 'Togo': nan, 'Thailand': 91.39908, 'Trinidad and Tobago': 74.82368, 'Turkey': nan, 'Taiwan, China': 95.96786, 'Tanzania, United Rep.': nan, 'Uganda': nan, 'Uruguay': nan, 'United States': 78.77981, 'Viet Nam': nan, 'Kosovo': nan, 'South Africa': nan}\n"
     ]
    }
   ],
   "source": [
    "# Verify by displaying a few records\n",
    "for record in collection.find().limit(5):\n",
    "    print(record)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab7e09c2-1509-45ef-8f45-e26a25d9274a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
