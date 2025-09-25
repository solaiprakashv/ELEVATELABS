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
