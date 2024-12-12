# Project3

-------------------------------------------------------------------------------
Samadhi Lokuhewage part

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
Soheil part

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
