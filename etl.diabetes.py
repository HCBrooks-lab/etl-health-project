# Importing libraries

import pandas as pd 
import sqlite3

# Loading file

file_path = 'diabetes_012_health_indicators_BRFSS2015.csv'
try:
    df = pd.read_csv(file_path, header = 1)
    print("Data loaded successfully.")
except FileNotFoundError:
    print("CSV file not found. Check the file path.")

# Previwing data

print("\n Dataset Shape:", df.shape)
print("\n First 5 Rows:")
print(df.head())

# Transforming the data

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print("\n Cleaned Column Names:")
print(df.columns.tolist())

print("\n Columns after cleaning:", df.columns.tolist())
print("\n Column data types:\n", df.dtypes)


print("\n Null Values Per Column:")
print(df.isnull().sum())

if 'age' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors = 'coerce')
    df['age_group'] = pd.cut(
        df['age'],
        bins=[18, 29, 39, 49, 59, 69, 120],
        labels=['18-29', '30-39', '40-49', '50-59', '60-69', '70+']
    )
    print("\n 'age_group' column added.")
else:
    print("\n No 'age' column found - age_group not created.")

# Database load

conn = sqlite3.connect('diabetes_health.db')
df.to_sql('health_indicators', conn, if_exists = 'replace', index = False)

result = conn.execute("SELECT * FROM health_indicators LIMIT 5").fetchall()
print("\n Sample rows loaded into SQLite:")
for row in result:
    print(row)

conn.close()
print("\n Data Successfully Saved to diabetes_health.db")