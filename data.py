import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


### Task 1: Load and Explore the Dataset


# Creating a simple dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [200, 220, 250, 210, 230, 240],
    "Region": ["North", "South", "East", "West", "North", "South"]
}

# Convert dictionary to pandas DataFrame
df = pd.DataFrame(data)

# Display first few rows
print("First few rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\nData types and missing values:")
print(df.info())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())


### Task 2: Basic Data Analysis


# Basic statistics
print("\nBasic statistics:")
print(df.describe())

# Group by Region and calculate mean Sales
grouped = df.groupby("Region")["Sales"].mean()
print("\nAverage Sales per Region:")
print(grouped)


### Task 3: Data Visualization


# Use seaborn style
sns.set(style="whitegrid")

# 1. Line chart - Sales trend over months
plt.figure(figsize=(6,4))
plt.plot(df["Month"], df["Sales"], marker='o', color='blue')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# 2. Bar chart - Average sales by region
plt.figure(figsize=(6,4))
grouped.plot(kind='bar', color='green')
plt.title("Average Sales by Region")
plt.xlabel("Region")
plt.ylabel("Average Sales")
plt.show()

# 3. Histogram - Distribution of Sales
plt.figure(figsize=(6,4))
plt.hist(df["Sales"], bins=5, color='orange', edgecolor='black')
plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot - Month vs Sales (just as an example)
plt.figure(figsize=(6,4))
plt.scatter(df["Month"], df["Sales"], color='red')
plt.title("Sales Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


# Observations

print("\nObservations:")
print("1. Sales gradually increase over the first 3 months, dip slightly in April, then rise again.")
print("2. The North and South regions have similar average sales.")
print("3. The sales distribution is fairly uniform across the months.")
