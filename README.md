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
3️⃣ Aggregation & Grouping

sql
Copy code
-- Total sales by region
SELECT o.Region, SUM(od.Sales) AS TotalSales
FROM orders o
JOIN order_details od ON o.OrderID = od.OrderID
GROUP BY o.Region
ORDER BY TotalSales DESC;
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
6️⃣ Optimization

sql
Copy code
-- Indexes for faster queries
CREATE INDEX idx_orders_orderid ON orders(OrderID);
CREATE INDEX idx_orderdetails_orderid ON order_details(OrderID);
CREATE INDEX idx_orders_region ON orders(Region);
🎯 Key Insights
Regions with highest and lowest sales

Products contributing most to revenue

Regions meeting or missing sales targets

Summary view (RegionalPerformance) provides quick decision-making insights

💡 Business Recommendations
Focus marketing and promotions on low-performing regions

Maintain inventory for high-demand products

Track performance against targets regularly for better planning

Use the SQL workflow as a repeatable analysis pipeline

🚀 How to Run Analysis
Open VS Code Terminal or Command Prompt

Navigate to the dataset folder:

bash
Copy code
cd "C:\Users\solai prakash\Videos\ELEVATELABS\TASK 4\dataset"
Start SQLite and create the database:

bash
Copy code
sqlite3 sales.db
Import CSVs and run the SQL script:

sql
Copy code
.mode csv
.import "List of Orders.csv" orders
.import "Order Details.csv" order_details
.import "Sales target.csv" sales_target

.read output.sql
Output will be saved in output.txt (all queries and results)

📂 Project Structure

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

