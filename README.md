# ETL Health Project: Diabetes Indicators Analysis

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline & exploratory SQL analysis on a health indicators dataset. It focuses on identifying diabetes trends across age groups and gender using SQLite and Python (pandas). 


## Dataset

The dataset used is stored locally as 'diabetes_health.db' and contains a single table 'health_indicators', from a cleaned CSV source. 


## Tools & Technologies

- Python3
- pandas
- SQLite3
- VS Code


## Project Structure

health_etl_project/
-diabetes_health.db # SQLite database with health data.
-analyze_diabetes_sql.py # Main script for querying and analysis.
-etl_diabetes.py # Script for cleaning/loading the CSV into SQLite.
-README.md # Documentation. 


## ETL Process Overview

1. **Extraction:** Raw health data was originally loaded from a CSV file.
2. **Transform:** Columns were cleaned and formatted; nulls were handled and
   text fields were normalized using 'etl_diabetes.py'. 
4. **Load:** Data was inserted into a SQLite database for effiecient querying
   ('diabetes_health.db').


## Key SQL Queries
### Query 1: Diabetes by Age Group
### Query 2: Diabetes Rate by Gender


## Query Preview

<details>
  <summary>Click to view Query 1 (Diabetes by Age Group)</summary>

```sql
SELECT age_group, COUNT(*) AS total, 
       SUM(diabetes_012) AS diabets_cases, 
       ROUND(CAST(SUM(diabetes_012) AS FLOAT) / COUNT(*), 2) AS diabetes_rate
FROM health_indicators
GROUP BY age_group;
</details>
```

## Features

- Cleaned and transformed real-world health data.
- Built and queried a local SQLite database.
- SQL queuries grouped by key demographics.
- Prepares groundwork for visualizations or dashboarding. 


## How to Run

1. Clone the Repo: git clone https://github.com/HCBrooks-lab/etl-health-
   project.git
   cd etl-health-project

2. Open analyze_diabetes_sql.py in your IDE or run: python
   analyze_diabetes_sql.py

## Future Improvements

1. Add visualization such as bar plots for diabetes rate.
2. Improve age grouping logic based on numeric age.
3. Expand ETL script to allow reusable transformations.

## Data Source

The original dataset was sourced from [Kaggle], containing health-related indicators such as diabetes diagnosis, age, BMI, cholesterol, blood pressure, physical activity, etc. Since the original needed cleaning, it was transformed and loaded into a SQLite database ('diabetes_health.db') for this project. Please note some dataset download links may require a login or subscription. 

Author: 
H. Brooks
