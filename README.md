# 🚀 ELEVATELABS - Data Analysis Learning Journey

This repository contains my daily tasks and projects as part of my data analysis and visualization learning path with ElevateLabs.

---

## 🎬 Movie Dataset Cleaning - Task 1

This project demonstrates **data cleaning techniques** using Python and Pandas on a movie dataset.
It is part of my learning journey to improve my **data analysis and machine learning skills**.

---

## 📌 Project Overview

In this task, I took a raw movie dataset and cleaned it step by step.
The main goals were to:

- Handle **missing values**
- Remove **duplicate records**
- Standardize column names and data formats
- Make the dataset **ready for analysis or visualization**

---

## 🛠️ Tools & Libraries Used

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



# 📊 Superstore Sales Analysis - Task 2

This task focuses on creating interactive data visualizations using Tableau to analyze sales performance and derive business insights from a superstore dataset.

---
