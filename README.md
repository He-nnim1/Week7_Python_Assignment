### Overview
This Python script demonstrates basic data analysis and visualization using a simple sales dataset. It is designed for beginners to learn how to use pandas for data handling and matplotlib / seaborn for plotting.

# The dataset includes:
Month – the month of sales
Sales – sales figures for each month
Region – region of the sales

# The script covers:
Loading and exploring the dataset
Basic statistical analysis
Grouping and calculating mean sales by region
Visualization using line chart, bar chart, histogram, and scatter plot
Observations based on the data

### How to Run
Ensure you have Python 3.x installed.
Install required libraries if not already installed:
pip install pandas matplotlib seaborn
Save the script as sales_analysis.py (or any name you like).
Run the script from the terminal:
python sales_analysis.py
The script will print data tables and statistics in the console and display four plots.

### Features in the Script
# 1. Load and Explore Data
Creates a simple dataset as a pandas DataFrame
Displays the first few rows using .head()
Checks data types and missing values

# 2. Basic Analysis
Computes descriptive statistics with .describe()
Groups sales by Region and calculates the mean

# 3. Visualizations
Line Chart: Shows monthly sales trend
Bar Chart: Displays average sales per region
Histogram: Shows the distribution of sales
Scatter Plot: Shows relationship between month and sales

# 4. Observations
Highlights trends and patterns in the sales data, e.g.,
Gradual increase in sales in the first 3 months
North and South regions have similar average sales
Distribution is fairly uniform across months
