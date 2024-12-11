# Project3
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











