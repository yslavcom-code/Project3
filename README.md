# Project3

-------------------------------------------------------------------------------
__Iaroslav Dochien part__

Datasets were downloaded following the link:
https://datacatalogfiles.worldbank.org/ddh-published/0037798/DR0092042/GemDataEXTR.zip?versionId=2024-11-28T11:02:38.3956286Z

Web page: https://datacatalog.worldbank.org/search/dataset/0037798/Global-Economic-Monitor

```text
License
Data Access and Licensing
Classification: Public
This dataset is classified as Public under the Access to Information Classification Policy. Users inside and outside the Bank can access this dataset.
License: Creative Commons Attribution 4.0
This dataset is licensed under Creative Commons Attribution 4.0
```

Current project directory structure
```text
.
├── 15.3 Citi Bike Project with Leaflet & Intro to Projects.pdf
├── GemDataEXTR
│   ├── CPI Price, % y-o-y, median weighted, seas. adj..xlsx
│   ├── CPI Price, % y-o-y, nominal, seas. adj..xlsx
│   ├── CPI Price, nominal, not seas. adj..xlsx
│   ├── CPI Price, nominal, seas. adj..xlsx
│   ├── Core CPI, not seas. adj..xlsx
│   ├── Core CPI, seas. adj..xlsx
│   ├── Exchange rate, new LCU per USD extended backward, period average.xlsx
│   ├── Exchange rate, old LCU per USD extended forward, period average.xlsx
│   ├── Exports Merchandise, Customs, Price, US$, not seas. adj..xlsx
│   ├── Exports Merchandise, Customs, Price, US$, seas. adj..xlsx
│   ├── Exports Merchandise, Customs, constant 2010 US$, millions, not seas. adj..xlsx
│   ├── Exports Merchandise, Customs, constant 2010 US$, millions, seas. adj..xlsx
│   ├── Exports Merchandise, Customs, current US$, millions, not seas. adj..xlsx
│   ├── Exports Merchandise, Customs, current US$, millions, seas. adj..xlsx
│   ├── Foreign Reserves, Months Import Cover, Goods.xlsx
│   ├── GDP Deflator at Market Prices, LCU.xlsx
│   ├── GDP at market prices, constant 2010 LCU, millions, seas. adj..xlsx
│   ├── GDP at market prices, constant 2010 US$, millions, seas. adj..xlsx
│   ├── GDP at market prices, current LCU, millions, seas. adj..xlsx
│   ├── GDP at market prices, current US$, millions, seas. adj..xlsx
│   ├── Imports Merchandise, Customs, Price, US$, not seas. adj..xlsx
│   ├── Imports Merchandise, Customs, Price, US$, seas. adj..xlsx
│   ├── Imports Merchandise, Customs, constant 2010 US$, millions, not seas. adj..xlsx
│   ├── Imports Merchandise, Customs, constant 2010 US$, millions, seas. adj..xlsx
│   ├── Imports Merchandise, Customs, current US$, millions, not seas. adj..xlsx
│   ├── Imports Merchandise, Customs, current US$, millions, seas. adj..xlsx
│   ├── Industrial Production, constant 2010 US$, not seas. adj..xlsx
│   ├── Industrial Production, constant 2010 US$, seas. adj..xlsx
│   ├── Nominal Effective Exchange Rate.xlsx
│   ├── Official exchange rate, LCU per USD, period average.xlsx
│   ├── Real Effective Exchange Rate.xlsx
│   ├── Retail Sales Volume Index, seas. adj..xlsx
│   ├── Stock Markets, LCU.xlsx
│   ├── Stock Markets, US$.xlsx
│   ├── Terms of Trade.xlsx
│   ├── Total Reserves.xlsx
│   └── Unemployment Rate, seas. adj..xlsx
├── GemDataEXTR.zip
├── image.png
├── link.txt
└── prj
    ├── BankProject
    │   ├── Final
    │   │   ├── Australia_unemployment_rate.ipynb
    │   │   ├── Australian_Unemployment_rate.png
    │   │   ├── Comprehensive_analysis.html
    │   │   └── Unemployment_Rate01.csv
    │   ├── GemDataEXTR
    │   │   ├── CPI Price, % y-o-y, median weighted, seas. adj..xlsx
    │   │   ├── CPI Price, % y-o-y, nominal, seas. adj..xlsx
    │   │   ├── CPI Price, nominal, not seas. adj..xlsx
    │   │   ├── CPI Price, nominal, seas. adj..xlsx
    │   │   ├── Core CPI, not seas. adj..xlsx
    │   │   ├── Core CPI, seas. adj..xlsx
    │   │   ├── GDP Deflator at Market Prices, LCU.xlsx
    │   │   ├── GDP at market prices, constant 2010 LCU, millions, seas. adj..xlsx
    │   │   ├── GDP at market prices, constant 2010 US$, millions, seas. adj..xlsx
    │   │   ├── GDP at market prices, current LCU, millions, seas. adj..xlsx
    │   │   ├── GDP at market prices, current US$, millions, seas. adj..xlsx
    │   │   └── Not Use
    │   │       ├── Exchange rate, new LCU per USD extended backward, period average.xlsx
    │   │       ├── Exchange rate, old LCU per USD extended forward, period average.xlsx
    │   │       ├── Exports Merchandise, Customs, Price, US$, not seas. adj..xlsx
    │   │       ├── Exports Merchandise, Customs, Price, US$, seas. adj..xlsx
    │   │       ├── Exports Merchandise, Customs, constant 2010 US$, millions, not seas. adj..xlsx
    │   │       ├── Exports Merchandise, Customs, constant 2010 US$, millions, seas. adj..xlsx
    │   │       ├── Exports Merchandise, Customs, current US$, millions, not seas. adj..xlsx
    │   │       ├── Exports Merchandise, Customs, current US$, millions, seas. adj..xlsx
    │   │       ├── Foreign Reserves, Months Import Cover, Goods.xlsx
    │   │       ├── Imports Merchandise, Customs, Price, US$, not seas. adj..xlsx
    │   │       ├── Imports Merchandise, Customs, Price, US$, seas. adj..xlsx
    │   │       ├── Imports Merchandise, Customs, constant 2010 US$, millions, not seas. adj..xlsx
    │   │       ├── Imports Merchandise, Customs, constant 2010 US$, millions, seas. adj..xlsx
    │   │       ├── Imports Merchandise, Customs, current US$, millions, not seas. adj..xlsx
    │   │       ├── Imports Merchandise, Customs, current US$, millions, seas. adj..xlsx
    │   │       ├── Industrial Production, constant 2010 US$, not seas. adj..xlsx
    │   │       ├── Industrial Production, constant 2010 US$, seas. adj..xlsx
    │   │       ├── Nominal Effective Exchange Rate.xlsx
    │   │       ├── Official exchange rate, LCU per USD, period average.xlsx
    │   │       ├── Real Effective Exchange Rate.xlsx
    │   │       ├── Retail Sales Volume Index, seas. adj..xlsx
    │   │       ├── Stock Markets, LCU.xlsx
    │   │       ├── Stock Markets, US$.xlsx
    │   │       ├── Terms of Trade.xlsx
    │   │       ├── Total Reserves.xlsx
    │   │       └── Unemployment Rate, seas. adj..xlsx
    │   ├── Unemployment_Rate_Monthly
    │   │   ├── Unemployment_Rate.csv
    │   │   └── Untitled.ipynb
    │   ├── app.py
    │   ├── dataset
    │   │   ├── Unemployment_Rate01.csv
    │   │   ├── unemployment_rate_cleaned.csv
    │   │   └── unemployment_statistics.csv
    │   ├── static
    │   │   └── map.js
    │   └── templates
    │       ├── index.html
    │       └── map.html
    ├── CPI final.ipynb
    ├── CodeIar
    │   ├── __pycache__
    │   │   └── read_xlsx.cpython-312.pyc
    │   ├── app.py
    │   ├── read_xlsx.py
    │   ├── static
    │   │   ├── JaneFolder
    │   │   │   ├── monthly-core-cpi-trend-analysis-seas-adjusted.png
    │   │   │   └── monthly-core-cpi-trend.png
    │   │   ├── LokuFolder
    │   │   │   ├── global_trends_plot.png
    │   │   │   ├── regional_bar_plot.png
    │   │   │   └── regional_trends_plot.png
    │   │   ├── SoheilFolder
    │   │   │   ├── Australian Unemployment Rate during Major Economic Crises.png
    │   │   │   └── Australian_Unemployment_rate.png
    │   │   ├── map.js
    │   │   └── script.js
    │   └── templates
    │       ├── Comprehensive_analysis.html
    │       ├── chart_page.html
    │       ├── gallery.html
    │       ├── index.html
    │       └── update_status.html
    ├── Output
    │   ├── cleaned_stock_data.xlsx
    │   ├── global_trends_plot.html
    │   ├── global_trends_plot.png
    │   ├── regional_bar_plot.html
    │   ├── regional_bar_plot.png
    │   ├── regional_trends_plot.html
    │   └── regional_trends_plot.png
    ├── Project 3 Presentation.pdf
    ├── Project3
    ├── README.md
    ├── ResourceIar
    │   ├── CPI Price, % y-o-y, median weighted, seas. adj..xlsx
    │   ├── CPI Price, % y-o-y, nominal, seas. adj..xlsx
    │   ├── CPI Price, nominal, not seas. adj..xlsx
    │   ├── CPI Price, nominal, seas. adj..xlsx
    │   ├── Core CPI, not seas. adj..xlsx
    │   ├── Core CPI, seas. adj..xlsx
    │   ├── Exchange rate, new LCU per USD extended backward, period average.xlsx
    │   ├── Exchange rate, old LCU per USD extended forward, period average.xlsx
    │   ├── Exports Merchandise, Customs, Price, US$, not seas. adj..xlsx
    │   ├── Exports Merchandise, Customs, Price, US$, seas. adj..xlsx
    │   ├── Exports Merchandise, Customs, constant 2010 US$, millions, not seas. adj..xlsx
    │   ├── Exports Merchandise, Customs, constant 2010 US$, millions, seas. adj..xlsx
    │   ├── Exports Merchandise, Customs, current US$, millions, not seas. adj..xlsx
    │   ├── Exports Merchandise, Customs, current US$, millions, seas. adj..xlsx
    │   ├── Foreign Reserves, Months Import Cover, Goods.xlsx
    │   ├── GDP Deflator at Market Prices, LCU.xlsx
    │   ├── GDP at market prices, constant 2010 LCU, millions, seas. adj..xlsx
    │   ├── GDP at market prices, constant 2010 US$, millions, seas. adj..xlsx
    │   ├── GDP at market prices, current LCU, millions, seas. adj..xlsx
    │   ├── GDP at market prices, current US$, millions, seas. adj..xlsx
    │   ├── Imports Merchandise, Customs, Price, US$, not seas. adj..xlsx
    │   ├── Imports Merchandise, Customs, Price, US$, seas. adj..xlsx
    │   ├── Imports Merchandise, Customs, constant 2010 US$, millions, not seas. adj..xlsx
    │   ├── Imports Merchandise, Customs, constant 2010 US$, millions, seas. adj..xlsx
    │   ├── Imports Merchandise, Customs, current US$, millions, not seas. adj..xlsx
    │   ├── Imports Merchandise, Customs, current US$, millions, seas. adj..xlsx
    │   ├── Industrial Production, constant 2010 US$, not seas. adj..xlsx
    │   ├── Industrial Production, constant 2010 US$, seas. adj..xlsx
    │   ├── Nominal Effective Exchange Rate.xlsx
    │   ├── Official exchange rate, LCU per USD, period average.xlsx
    │   ├── Real Effective Exchange Rate.xlsx
    │   ├── Retail Sales Volume Index, seas. adj..xlsx
    │   ├── Stock Markets, LCU.xlsx
    │   ├── Stock Markets, US$.xlsx
    │   ├── Terms of Trade.xlsx
    │   ├── Total Reserves.xlsx
    │   └── Unemployment Rate, seas. adj..xlsx
    ├── Resources
    │   └── Stock Markets, US$.xlsx
    └── Stock Markets final.ipynb
```

I focused primarily on backend and visualisation of data.
From directory [CodeIar](https://github.com/yslavcom-code/Project3/tree/dev/combined/CodeIar), launch server by typing
__python app.py__
then access from browser such as 
__http://127.0.0.1:5000/__

It should open a page with the World Map with tags for the countries present in the datasets for this project.

```text
The following paths are available
/            - home page (world map with country tags)
/update-data - launches script to update the mongodb database with data from Deflator Spreadsheets
/delete-data - deletes the database in mongo db for debug purposes
/data        - fetches data from mongo db database for interactive visuals
/chart_page  - page to display GDP Deflator for various countries in interactive mode, data fetched from mongo db
/soheil      - Folder for snapshots provided by Soheil
/jane        - Folder for snapshots provided by Jane
/loku        - Folder for snapshots provided by Loku
```
```text
The following libraries were used
- flask
- pymongo
- json
- bson
- leaflet
- chart.js
```
From the GDP Deflator chart is seen that mainly it grows over time for most of the countried and the post-covid time has had a significant impact,
especially on Argentina.

Sone slides are given in __Project 3 Presentation.pdf__

-------------------------------------------------------------------------------
__Samadhi Lokuhewage part__

Stock Data Analysis Project

Overview

This project analyzes stock data for multiple countries between 1995 and 2024. It calculates global averages, regional trends, and visualizes the results using various plots. The data is stored in MongoDB for future analysis.

Steps

1. Setup
Install the required dependencies for the project. Ensure MongoDB is running, or update the connection URL in the script.



3. Load and Clean Data
Load the stock data from an Excel file.
Rename the 'Unnamed: 0' column to 'Year'.
Remove rows where the 'Year' column is NaN and reset the index.
Convert the 'Year' column to integers.
Replace '0.0' values with NaN and fill missing values with 0 for all columns except 'Year'.



5. Insert Data into MongoDB
Connect to MongoDB.
Convert the cleaned data into a list of dictionaries and insert it into the MongoDB collection.



7. Calculate Global Averages
Calculate the global average and median stock value for each year across all countries.
8. Regional Trends
Define regions and group countries accordingly.
Calculate the average stock value for each region for each year.


10. Save Regional Trends to MongoDB
Insert the calculated regional trends into the MongoDB collection.



12. Visualize Trends
Create and save plots to visualize global trends (line plot for global average and median) and regional trends (stacked area plot for regional averages).
Save the plots in both PNG and interactive HTML formats.



14. Retrieve Data from MongoDB
Retrieve the global averages and regional trends from MongoDB and display them.
Conclusion

This project provides a comprehensive analysis of stock trends at global and regional levels, with all data stored in MongoDB for future use. It also generates visualizations to help better understand the stock trends over time.










Data Source(s)

Stock market data is sourced from the Excel file Stock Markets, US$.xlsx available on the project directory. The data spans multiple years (1995-2024) for various countries.

Stock Market Data Source: https://data.worldbank.org

Pandas Documentation: https://pandas.pydata.org/

Matplotlib Documentation: https://matplotlib.org/

mpld3 Documentation: https://mpld3.github.io/

MongoDB Documentation: https://www.mongodb.com/docs/




## Repository Structure
```
.
├── Resources
│   ├── .PNG
├── stock_analysis.py
├── requirements.txt
├── global_trends_plot.html
├── regional_trends_plot.html
├── regional_bar_plot.html
├── README.md
```

-------------------------------------------------------------------------------
__Soheil part__

For this project, I focused on analyzing unemployment trends across major economic crises, with a particular emphasis on Australia's experience during the 2008 Global Financial Crisis and the COVID-19 pandemic.

Data Cleaning Process:

I began by leveraging Python's powerful data analysis libraries such as Pandas, numpy and matplotlib and seaborn for visualisation.

First Phase:
- Loaded the raw unemployment data from the World Bank dataset
- Cleaned column names by removing unwanted whitespace
- Removed problematic rows and standardized the data structure
- Converted the Year column to proper integer format for time-series analysis

Second Phase:

- Handled missing values by converting 'NA' entries to numpy's NaN
- Transformed all unemployment rate columns to numeric values
- Validated data types to ensure consistency across all measurements
- Created a clean subset focusing on Australian unemployment data

Statistical Analysis:

- Generated descriptive statistics for the entire period
- Created specific subsets for crisis periods (2007-2009 and 2019-2021)
- Calculated key metrics like:
    - Peak unemployment rates during each crisis
    - Rate of change during crisis onset
    - Recovery patterns post-crisis

By following this methodical approach, I was able to prepare a clean, reliable dataset that formed the basis for our visualisation work. What I found particularly interesting was how this structured approach revealed clear patterns in the data, especially around crisis periods. For instance, when looking at the Australian data, we discovered distinct differences in how unemployment responded to different types of economic shocks. This leads us to our visualisation strategy, which I designed to highlight these contrasts effectively.Visualisation :

I created this line chart using a combination of matplotlib and seaborn libraries, with several key design elements:
- A clear blue trend line showing the unemployment rate over time
- Highlighted crisis periods using color-coded shading (orange for the Global Financial Crisis and pink for the COVID-19 Crisis)
- Professional gridlines to aid in reading precise values
- Clear annotations marking peak unemployment rates during crisis periods

Key Insights from the Visualization:
1. Long-term Trend:
2. We can see a general downward trend in unemployment from the mid-1990s (around 8%) to pre-GFC levels (around 4%)
3. Crisis Comparisons:
4. Global Financial Crisis (2007-2009): Shows a gradual increase in unemployment, peaking at about 5.6%
5. COVID-19 Crisis (2019-2021): Displays a much sharper spike, reaching approximately 6.4%, but with a faster recovery
6. Recovery Patterns:
7. Post-GFC: The recovery was relatively gradual, with unemployment taking several years to return to pre-crisis levels
8. Post-COVID: We observe a more V-shaped recovery, with unemployment rates dropping more rapidly

This visualization effectively communicates both the immediate impact of economic crises and their longer-term effects on Australia's labor market. The use of shaded regions helps viewers instantly identify crisis periods and compare their relative impacts.

-------------------------------------------------------------------------------
__Jane part__

# Global Economic Indicators Analysis Project

## Overview
Comprehensive analysis of three key economic indicators from 1994-2024:
- CPI Price Index
- Inflation Rates
- Core CPI


## Key Findings

### Price Index Analysis:
- Advanced economies show steady, controlled growth
- Emerging markets demonstrate higher volatility
- Significant regional variations in price levels
- Clear impact of global economic events

### Inflation Analysis:
- Advanced economies maintained stability (0-3% typical range)
- Notable spikes during 2008 and 2022-2023
- Emerging markets show higher but improving stability
- Recent global synchronization in inflation trends

### Core CPI Trends:
- More stable than headline inflation
- Regional divergences in structural inflation
- Advanced economies show better containment
- Emerging markets display gradual improvement

## Technical Implementation

### Requirements
- Python 3.x
- MongoDB
- Required packages:
  ```
  pandas
  numpy
  pymongo
  matplotlib
  seaborn
  ```

## Key Insights
1. Global Trends:
   - Increasing economic integration
   - Convergence in advanced economy patterns
   - Emerging market improvements

2. Regional Patterns:
   - Advanced economies: Most stable
   - East Asia: Strong performance
   - Europe & Central Asia: Significant progress
   - South Asia: Persistent challenges

3. Recent Developments (2020-2024):
   - Global inflation surge
   - Post-COVID recovery patterns
   - Regional policy responses
