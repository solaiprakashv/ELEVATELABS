import pandas as pd

# Replace this with the actual local path of your CSV file
file_path = r"C:\Users\solai prakash\Videos\TASK 1\dataset\netflix_titles.csv"

# Load dataset
df = pd.read_csv(file_path)

# 1. Identify missing values
print("Missing Values Before Cleaning:")
print(df.isnull().sum())

# 2. Remove duplicate rows
df_cleaned = df.drop_duplicates()

# 3. Standardize text values (convert country names to lowercase)
df_cleaned['country'] = df_cleaned['country'].str.lower()

# 4. Convert date formats to consistent type
df_cleaned['date_added'] = pd.to_datetime(df_cleaned['date_added'], errors='coerce', format='%B %d, %Y')

# 5. Rename column headers (lowercase, replace spaces with underscores)
df_cleaned.columns = df_cleaned.columns.str.strip().str.lower().str.replace(' ', '_')

# 6. Fix data types (release_year as int)
df_cleaned['release_year'] = df_cleaned['release_year'].astype('Int64')

# Optional: Fill missing values
df_cleaned['country'] = df_cleaned['country'].fillna('unknown')
df_cleaned['director'] = df_cleaned['director'].fillna('unknown')
df_cleaned['cast'] = df_cleaned['cast'].fillna('unknown')
df_cleaned['rating'] = df_cleaned['rating'].fillna('Not Rated')
df_cleaned['duration'] = df_cleaned['duration'].fillna('unknown')

# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df_cleaned.isnull().sum())

# Display cleaned dataset info
print("\nCleaned Dataset Info:")
print(df_cleaned.info())

# Save cleaned dataset (optional)
output_path = r"C:\Users\solai prakash\Videos\TASK 1\netflix_titles_cleaned.csv"
df_cleaned.to_csv(output_path, index=False)
print(f"\n✅ Cleaned dataset saved as: {output_path}")
