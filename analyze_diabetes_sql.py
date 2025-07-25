import sqlite3
import pandas as pd

conn = sqlite3.connect('diabetes_health.db')

schema = pd.read_sql_query("PRAGMA table_info(health_indicators);", conn)
print("\n Table Schema:")
print(schema[['name','type']])

tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type = 'table';", conn)
print(" Tables in the Database:")
print(tables)

df = pd.read_sql_query("SELECT * FROM health_indicators LIMIT 5;", conn)
print("\n First 5 rows:")
print(df.head())

# Query 1: Diabetes Rate by Age Group

query1 = '''
SELECT
    age_group, 
    COUNT(*) AS total, 
    SUM(diabetes_012) AS diabetes_cases,
    ROUND(SUM(diabetes_012) * 1.0 / COUNT(*), 2) AS diabetes_rate
FROM health_indicators
GROUP BY age_group
ORDER BY age_group
'''

result1 = pd.read_sql_query(query1, conn)
print("\nDiabetes Rate by Age Group:")
print(result1)

# Function for Query 2: Diabetes Rate by Gender
query2 = '''
SELECT sex,
    COUNT(*) AS total,
    ROUND(SUM(diabetes_012) * 1.0 / COUNT(*), 2) AS diabetes_rate
FROM health_indicators
WHERE sex IS NOT NULL
GROUP BY sex
ORDER BY sex;
'''
result2 = pd.read_sql_query(query2, conn)
print("\nDiabetes Rate by Gender:")
print(result2)


conn.close()
print("\n Database Connection Closed.")