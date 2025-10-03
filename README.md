# 🚀 ELEVATELABS - Data Analysis Learning Journey

This repository contains my daily tasks and projects as part of my data analysis and visualization learning path with ElevateLabs.

---

## 🎬 Movie Dataset Cleaning - Task 1

This project demonstrates **data cleaning techniques** using Python and Pandas on a movie dataset.
It is part of my learning journey to improve my **data analysis and machine learning skills**.

---

### 📌 Project Overview

In this task, I took a raw movie dataset and cleaned it step by step.
The main goals were to:

- Handle **missing values**
- Remove **duplicate records**
- Standardize column names and data formats
- Make the dataset **ready for analysis or visualization**

---

### 🛠️ Tools & Libraries Used

- **Python 3**
- **Pandas** – for data manipulation
- **NumPy** – for numerical operations



Install dependencies:
```bash
pip install pandas numpy
```

🧾 Steps Performed
1️⃣ Importing Libraries and Dataset

```bash
import pandas as pd
import numpy as np

# Load the dataset (replace with your file path)
df = pd.read_csv('netflix_titles.csv')
print(df.head())
```

2️⃣ Checking for Missing Values

```bash
print("Missing Values Before Cleaning:")
print(df.isnull().sum())
```

3️⃣ Removing Duplicate Records

```bash
df_cleaned = df.drop_duplicates()
```

4️⃣ Standardizing Data

```bash
# Convert country names to lowercase
df_cleaned['country'] = df_cleaned['country'].str.lower()

# Convert date formats to consistent type
df_cleaned['date_added'] = pd.to_datetime(df_cleaned['date_added'], errors='coerce', format='%B %d, %Y')

# Rename column headers (lowercase, replace spaces with underscores)
df_cleaned.columns = df_cleaned.columns.str.strip().str.lower().str.replace(' ', '_')
```

5️⃣ Fixing Data Types

```bash
df_cleaned['release_year'] = df_cleaned['release_year'].astype('Int64')
```

6️⃣ Handling Missing Values

```bash
df_cleaned['country'] = df_cleaned['country'].fillna('unknown')
df_cleaned['director'] = df_cleaned['director'].fillna('unknown')
df_cleaned['cast'] = df_cleaned['cast'].fillna('unknown')
df_cleaned['rating'] = df_cleaned['rating'].fillna('Not Rated')
df_cleaned['duration'] = df_cleaned['duration'].fillna('unknown')
```

7️⃣ Final Dataset Check and Save

```bash
print("\nMissing Values After Cleaning:")
print(df_cleaned.isnull().sum())

print("\nCleaned Dataset Info:")
print(df_cleaned.info())

# Save cleaned dataset (optional)
output_path = "netflix_titles_cleaned.csv"
df_cleaned.to_csv(output_path, index=False)
print(f"\n✅ Cleaned dataset saved as: {output_path}")
```

📂 Project Structure

```bash
Netflix-Data-Cleaning/
├── netflix_titles.csv              # Original raw dataset
├── Task1.py                        # The Python data cleaning script
└── netflix_titles_cleaned.csv      # The final cleaned dataset
```

---
---

## 📊 Superstore Sales Analysis - Task 2

This task focuses on creating interactive data visualizations using Tableau to analyze sales performance and derive business insights from a superstore dataset.

---

### 📌 Project Overview
In this task, I created comprehensive dashboards and visualizations to:

Analyze sales trends across different regions
Identify top-performing product categories
Understand customer segments and their buying patterns
Provide actionable insights for business decisions

---

### 🛠️ Tools & Technologies Used

Tableau Desktop – for interactive data visualization
Microsoft Excel – for initial data exploration
PDF Documentation – for detailed analysis methodology

---

### 📁 Files Included

1)Book.pdf

Comprehensive documentation of the analysis process
Includes methodology, insights, and recommendations

2)Book.twbx

Interactive Tableau workbook with multiple dashboards
Contains various visualizations including:
Sales by Region
Product Category Performance
Time Series Analysis
Customer Segment Analysis

3)Sample - Superstore (1).xls

Raw dataset containing 4 years of sales data
Includes information on orders, products, customers, and regions

---

### 🎯 Key Insights Discovered
Regional Performance: Identified top-performing regions and underperforming areas
Product Analysis: Found which product categories drive the most profit
Seasonal Trends: Discovered patterns in sales throughout the year
Customer Segments: Analyzed which customer types contribute most to revenue

---

### 💡 Business Recommendations
Based on the analysis, I provided recommendations for:

Inventory management optimization
Regional marketing strategies
Product portfolio decisions
Customer retention strategies

---

### 🚀 How to View the Analysis

1)Excel Data: Open Sample - Superstore (1).xls to explore the raw data

2)Tableau Dashboards: Open Book.twbx in Tableau Desktop/Reader

3)Documentation: Read Book.pdf for detailed insights and methodology

---

### 📸 Dashboard Preview

The Tableau workbook includes:

Executive Summary Dashboard
Regional Performance Analysis
Product Category Deep Dive
Customer Segment Analysis
Time Series Trends

---

### 📂 Project Structure

```bash
TASK 2/
├── Book.pdf                        # Analysis documentation
├── Book.twbx                       # Tableau workbook with dashboards
├── Sample - Superstore (1).xls     # Raw superstore sales data
└── README.md                       # This file
```


---
---

## 📈 Financial Sales Analysis - Task 3

This task focuses on analyzing **financial sales data** using Tableau and presenting insights through interactive dashboards and reports.

---

### 📌 Project Overview

In this task, I worked on a coffee shop sales dataset and performed:

- Data preparation and cleaning
- Trend analysis on daily, weekly, and monthly sales
- Customer segmentation and product performance insights
- Creation of interactive dashboards for business decision-making

---

### 🛠️ Tools & Technologies Used

- **Tableau Desktop** – for building dashboards and interactive visualizations  
- **Microsoft Excel / CSV** – for data validation and preprocessing  
- **PDF Documentation** – summarizing the methodology and insights  

---

### 📁 Files Included

1. **Financial Sales Analysis.pdf**  
   - Detailed documentation of methodology, KPIs, and insights

2. **Financial Sales Analysis.twbx**  
   - Interactive Tableau workbook containing:
     - Sales Trends Dashboard  
     - Category & Product Performance Analysis  
     - Regional/Store-Level Breakdown  
     - Customer Insights  

3. **dataset/Coffe_sales.csv**  
   - The raw sales dataset used for analysis  

4. **~Financial Sales Analysis__2212.twbr**  
   - Tableau backup/temporary file (useful for recovery)

---

### 🎯 Key Insights Discovered

- **Sales Trends:** Identified peak hours, days, and months for maximum revenue  
- **Product Analysis:** Highlighted top-performing coffee products and low-performing items  
- **Customer Behavior:** Segmented customers by frequency and spend  
- **Revenue Optimization:** Suggested focus on high-profit categories and seasonal promotions  

---

### 💡 Business Recommendations

Based on the insights, I recommended:

- **Stock Optimization:** Increase inventory for high-demand periods  
- **Targeted Campaigns:** Run promotions during low-performing months  
- **Menu Adjustments:** Focus marketing on high-profit products  
- **Customer Loyalty Programs:** Reward frequent buyers to improve retention  

---

### 🚀 How to View the Analysis

1. **Dataset:** Open `dataset/Coffe_sales.csv` to explore raw data  
2. **Tableau Dashboard:** Open `Financial Sales Analysis.twbx` in Tableau  
3. **Documentation:** Review `Financial Sales Analysis.pdf` for detailed insights  

---

### 📂 Project Structure

```bash
TASK 3/
├── Financial Sales Analysis.pdf          # Detailed analysis documentation
├── Financial Sales Analysis.twbx         # Tableau workbook with dashboards
├── dataset/
│   └── Coffe_sales.csv                   # Raw coffee sales dataset
└── ~Financial Sales Analysis__2212.twbr  # Tableau backup file
```


---
---
## 📈 Financial Sales Analysis with SQLite - Task 4

This task demonstrates **data analysis using SQLite** on a financial sales dataset.  
It focuses on querying, joining tables, aggregating data, and creating views for **insightful business analysis**.

---

### 📌 Project Overview

In this task, I worked on sales data of multiple regions and products to:

- Import and clean CSV datasets into SQLite  
- Perform **SQL queries** including selection, filtering, aggregation, and joins  
- Compare **regional performance** versus sales targets  
- Create **views for analysis** and generate outputs for reporting  

This project strengthens **SQL querying skills**, understanding of **relational databases**, and **data-driven decision making**.

---

### 🛠️ Tools & Technologies Used

- **SQLite 3** – for database management and queries  
- **CSV Datasets** – raw sales data, order details, and sales targets  
- **VS Code / SQLite CLI** – to run queries and manage the database  
- **Output Files** – SQL query outputs and screenshots  

---

🧾 Steps Performed  

1️⃣ **Database Setup**

```sql
-- Create tables
CREATE TABLE orders (
    OrderID TEXT,
    OrderDate TEXT,
    CustomerName TEXT,
    Region TEXT,
    City TEXT
);

CREATE TABLE order_details (
    OrderID TEXT,
    ProductName TEXT,
    Quantity INTEGER,
    Sales REAL
);

CREATE TABLE sales_target (
    Region TEXT,
    Target REAL
);

-- Import CSV data
.mode csv
.import "List of Orders.csv" orders
.import "Order Details.csv" order_details
.import "Sales target.csv" sales_target
```
```sql
2️⃣ Basic Queries & Filtering

sql
Copy code
-- Select first 10 orders
SELECT * FROM orders LIMIT 10;

-- Orders with above-average sales
SELECT * FROM orders
WHERE OrderID IN (
    SELECT OrderID FROM order_details
    WHERE Sales > (SELECT AVG(Sales) FROM order_details)
);
```
```sql
3️⃣ Aggregation & Grouping

sql
Copy code
-- Total sales by region
SELECT o.Region, SUM(od.Sales) AS TotalSales
FROM orders o
JOIN order_details od ON o.OrderID = od.OrderID
GROUP BY o.Region
ORDER BY TotalSales DESC;
```
```sql
4️⃣ Joins

sql
Copy code
-- Join orders and order_details
SELECT o.OrderID, o.Region, od.ProductName, od.Quantity, od.Sales
FROM orders o
INNER JOIN order_details od ON o.OrderID = od.OrderID
LIMIT 10;

-- Left join with sales_target
SELECT o.Region, SUM(od.Sales) AS TotalSales, st.Target
FROM orders o
LEFT JOIN order_details od ON o.OrderID = od.OrderID
LEFT JOIN sales_target st ON o.Region = st.Region
GROUP BY o.Region;
```
```sql
5️⃣ Creating Views

sql
Copy code
-- View for regional performance
CREATE VIEW RegionalPerformance AS
SELECT o.Region, SUM(od.Sales) AS TotalSales, st.Target,
       (SUM(od.Sales) - st.Target) AS Difference
FROM orders o
JOIN order_details od ON o.OrderID = od.OrderID
LEFT JOIN sales_target st ON o.Region = st.Region
GROUP BY o.Region;

-- Query the view
SELECT * FROM RegionalPerformance
ORDER BY Difference DESC;
```
```sql
6️⃣ Optimization

-- Indexes for faster queries
CREATE INDEX idx_orders_orderid ON orders(OrderID);
CREATE INDEX idx_orderdetails_orderid ON order_details(OrderID);
CREATE INDEX idx_orders_region ON orders(Region);
```
---
🎯 Key Insights
Regions with highest and lowest sales

Products contributing most to revenue

Regions meeting or missing sales targets

Summary view (RegionalPerformance) provides quick decision-making insights

---
💡 Business Recommendations
Focus marketing and promotions on low-performing regions

Maintain inventory for high-demand products

Track performance against targets regularly for better planning

Use the SQL workflow as a repeatable analysis pipeline

---
🚀 How to Run Analysis
Open VS Code Terminal or Command Prompt

Navigate to the dataset folder:

Start SQLite and create the database:

```sql
sqlite3 sales.db
Import CSVs and run the SQL script:

.mode csv
.import "List of Orders.csv" orders
.import "Order Details.csv" order_details
.import "Sales target.csv" sales_target

.read output.sql

```
Output will be saved in output.txt (all queries and results)

📂 Project Structure
```bash
TASK 4/
├── dataset/
│   ├── List of Orders.csv
│   ├── Order Details.csv
│   ├── Sales target.csv
│   └── sales.db
├── Output/
│   ├── output.sql          # SQL queries
│   ├── output.txt          # Query results
│   └── Screenshots/        # Screenshots of terminal outputs
└── README.md               # Project documentation
```

---
---
## 📊 Exploratory Data Analysis (EDA) - Task 5

This task demonstrates **Exploratory Data Analysis (EDA)** using Python and Pandas on the **Titanic dataset**.  
It is part of my learning journey to strengthen **data analysis, visualization, and insight generation skills**.

---

### 📌 Project Overview

In this task, I performed a comprehensive analysis of the Titanic dataset to uncover patterns and relationships in passenger survival.  
The main goals were to:

- Understand **dataset structure and features**
- Identify **missing values** and data quality issues
- Explore **numerical and categorical distributions**
- Visualize patterns in **survival by gender, class, age, and fare**
- Summarize key **insights for decision-making**

---

### 🛠️ Tools & Libraries Used

- **Python 3**  
- **Pandas** – for data manipulation  
- **Matplotlib & Seaborn** – for data visualization  

Install dependencies:

```bash
pip install pandas matplotlib seaborn
```

🧾 Steps Performed
1️⃣ Importing Libraries and Dataset
```bash
from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Upload Titanic train dataset
uploaded = files.upload()

# Load dataset
df = pd.read_csv("train.csv")
df.head()
```

2️⃣ Basic Dataset Info
```bash
df.info()
```

3️⃣ Summary Statistics
```bash
df.describe()
```

4️⃣ Check Missing Values
```bash
df.isnull().sum()
```

5️⃣ Count Unique Values
```bash
df.nunique()
```

6️⃣ Age Distribution
```bash
sns.histplot(df['Age'].dropna(), kde=True)
plt.title("Age Distribution")
plt.show()
```
Observation: Most passengers are between 20–40 years old.

7️⃣ Survival Count
```bash
sns.countplot(x='Survived', data=df)
plt.title("Survival Count (0 = No, 1 = Yes)")
plt.show()
```
Observation: More passengers did not survive than survived.

8️⃣ Survival by Gender
```bash
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.show()
```
Observation: Females had a much higher survival rate than males.

9️⃣ Survival by Passenger Class
```bash
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Passenger Class")
plt.show()
```
Observation: 1st class passengers survived more than 3rd class.

🔟 Age vs Fare (Survival)
```bash
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df)
plt.title("Age vs Fare (colored by Survival)")
plt.show()
```
Observation: Wealthier passengers (higher Fare) had better survival chances.

1️⃣1️⃣ Boxplot: Age vs Survival
```bash
sns.boxplot(x='Survived', y='Age', data=df)
plt.title("Age vs Survival")
plt.show()
```
Observation: Younger passengers show slightly better survival trends.

1️⃣2️⃣ Correlation Heatmap
```bash
df_encoded = df.copy()
df_encoded['Sex'] = df_encoded['Sex'].map({'male': 0, 'female': 1})

plt.figure(figsize=(8,6))
sns.heatmap(df_encoded.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
```
Observation: Gender and class strongly correlate with survival.

1️⃣3️⃣ Pairplot (Optional)
```bash
sns.pairplot(df_encoded[['Survived','Age','Fare','Pclass','Sex']], hue='Survived')
plt.show()
```
1️⃣4️⃣ Final Summary

---
Markdown Observation:
* Survival strongly depended on gender and passenger class.

* Females had higher survival rates than males.

* 1st class passengers survived more than 3rd class.

* Younger passengers had slightly better chances.

* Higher fares correlated with survival.


🟢 Deliverables

---
* Notebook: .ipynb file with all code and observations

* PDF Report: Use File → Print → Save as PDF in Colab
---

📂 Project Structure
```bash
TASK 5 - Titanic EDA/
├── train.csv                 # Raw Titanic dataset
├── Titanic_EDA.ipynb         # Colab notebook with EDA steps
└── README.md                 # Project documentation
```

---
---

## 📊 Sales Trend Analysis - Task 6

This task demonstrates **sales trend analysis using Python and SQLite**, aimed at uncovering insights from an online sales dataset and performing data cleansing, aggregation, and visualization.  

---

### 📌 Project Overview

In this task, I analyzed online sales data to:

- Import and clean CSV datasets into SQLite  
- Perform **data validation and cleansing**  
- Analyze **sales trends by date, product category, and region**  
- Generate **summary statistics and visualizations** for business insights  

This task strengthens skills in **SQL querying, Python data analysis, and visualization**.  

---

### 🛠️ Tools & Libraries Used

- **Python 3** – for data manipulation and analysis  
- **Pandas & NumPy** – for cleaning and transforming data  
- **Matplotlib & Seaborn** – for visualizations  
- **SQLite 3** – for database operations  
- **VS Code / SQLite CLI** – to run scripts and queries  

Install Python dependencies:
```bash
pip install pandas numpy matplotlib seaborn
🧾 Steps Performed
1️⃣ Database Setup & CSV Import

```bash

-- Create sales table
CREATE TABLE online_sales (
    transaction_id INTEGER,
    order_date TEXT,
    product_category TEXT,
    product_name TEXT,
    amount REAL
);

-- Import CSV into SQLite
.mode csv
.import "online_sales.csv" online_sales
```

2️⃣ Data Cleaning
```bash
python

import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('sales.db')
df = pd.read_sql_query("SELECT * FROM online_sales", conn)

# Check missing values
print(df.isnull().sum())

# Fill missing values
df['amount'] = df['amount'].fillna(0)
df['product_category'] = df['product_category'].fillna('Unknown')
df['product_name'] = df['product_name'].fillna('Unknown')
```

3️⃣ Aggregations & Trend Analysis
```bash
python

# Total sales by category
category_sales = df.groupby('product_category')['amount'].sum().reset_index()

# Sales trend over time
df['order_date'] = pd.to_datetime(df['order_date'])
daily_sales = df.groupby('order_date')['amount'].sum().reset_index()

# Plot daily sales trend
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.plot(daily_sales['order_date'], daily_sales['amount'], marker='o')
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

```
---
🎯 Key Insights Discovered
Identified top-selling product categories

Found peak sales periods by date

Discovered regions with highest and lowest sales

Highlighted trends useful for inventory and marketing decisions

---

💡 Business Recommendations
Focus marketing campaigns on top-performing products

Adjust inventory according to peak sales periods

Target underperforming regions with promotions

Use this analysis workflow for future sales tracking


📂 Project Structure
```bash
TASK 6/
├── dataset/
│   └── online_sales.csv         # Raw sales dataset
├── Task6.py                     # Python script for analysis
├── sales.db                     # SQLite database (after import)
└── README.md                    # Project documentation
```

---
---
## 📊 Basic Sales Summary with SQLite - Task 7

This task demonstrates **basic sales analysis using Python and SQLite**.  
It focuses on calculating **total quantity sold** and **total revenue per product** from a small sales dataset, and visualizing it using a simple **bar chart**.

---

### 📌 Project Overview

In this task, I performed the following:

- Created a **SQLite database** (`sales_data.db`) with a `sales` table  
- Inserted **sample sales data** for multiple products  
- Used **Python** to connect to the database and run SQL queries  
- Calculated **total quantity** and **total revenue** per product  
- Visualized the revenue per product using **matplotlib bar chart**  

This task strengthens skills in **SQL queries inside Python**, **pandas DataFrame manipulation**, and **basic data visualization**.

---

### 🛠️ Tools & Libraries Used

- **Python 3** – for database connection, querying, and visualization  
- **SQLite 3** – for database storage  
- **Pandas** – for loading SQL query results into DataFrame  
- **Matplotlib** – for plotting a simple bar chart  

Install Python dependencies:

```bash
pip install pandas matplotlib
```

🧾 Steps Performed
1️⃣ Create Database and Insert Data
```bash
import sqlite3

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", [
    ("Laptop", 2, 50000),
    ("Phone", 5, 20000),
    ("Tablet", 3, 15000),
    ("Laptop", 1, 50000),
    ("Phone", 2, 20000)
])

conn.commit()
conn.close()
print("✅ Database created with sample data")
```

2️⃣ Run SQL Query and Load Results in Python
```bash
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("sales_data.db")

query = """
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

df = pd.read_sql_query(query, conn)
print("📊 Sales Summary:\n")
print(df)
```

3️⃣ Visualize Revenue by Product
```bash
df.plot(kind="bar", x="product", y="revenue", legend=False)
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.savefig("sales_chart.png")   # Save chart
plt.show()

conn.close()
```

---
**🎯 Key Insights Discovered**

Laptop: 3 units sold, total revenue ₹150,000

Phone: 7 units sold, total revenue ₹140,000

Tablet: 3 units sold, total revenue ₹45,000

Revenue visualization helps quickly identify the top-earning product.

---
**💡 Business Recommendations**

Focus marketing and sales efforts on top revenue-generating products

Track inventory for products with high sales volume

Use similar SQLite + Python workflow for other datasets

---
```bash
📂 Project StructureTASK 7/
├── create_db.py          # Script to create DB + insert sample data
├── task7.py              # Python analysis script (query + chart)
├── sales_data.db         # SQLite database (auto-created)
├── sales_chart.png       # Revenue bar chart (auto-generated)
└── README.md             # Project documentation
```


---
---

## 📊 Superstore Sales Dashboard - Task 8

This project demonstrates **data visualization and insights generation** using the Superstore dataset.  
The analysis highlights **sales, profit trends, regional performance, and category breakdowns**.

---

### 📌 Project Overview
- Dataset: **SuperStoreOrders.csv**
- Tools Used: **Tableau, Python (for preprocessing), Excel**
- Deliverables:  
  - `SuperStore Sales Dashboard.pdf` → Exported dashboard insights  
  - `SuperStoreOrders.twbx` → Tableau packaged workbook  
  - `Insights.txt` → Key findings from analysis  

---

### 🔑 Key Insights
- Regional sales trends with profit contribution.  
- Category-level performance (Furniture, Technology, Office Supplies).  
- Time-series view of **Order Date vs Sales & Profit**.  
- Identification of **high-performing vs low-performing regions**.  

---

### 📂 Folder Structure
```bash
TASK 8/
│── dataset/
│ └── SuperStoreOrders.csv
│── SuperStoreOrders.twbx
│── SuperStore Sales Dashboard.pdf
│── Insights.txt
│── ~SuperStoreOrders__10656.twbr
```
