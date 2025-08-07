# ETL Health Project: Diabetes Indicators Analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline and exploratory SQL analysis using a health indicators dataset. The analysis focuses on diabetes trends by **age group** and **gender** using SQLite and Python (`pandas`).

---

## Dataset

The dataset is stored locally as `diabetes_health.db`, which contains a single table, `health_indicators`, transformed from a cleaned CSV file.

---

## Tools & Technologies

- Python3
- pandas
- SQLite3
- VS Code

---

## Project Structure

1. diabetes_health.db: SQLite database with health data.
2. diabetes_012_health_csv: Original csv source.
3. etl_diabetes.py: Cleans and loads csv into SQLite.
4. analyze_diabetes_sql.py: SQL queries and analysis.
5. viz_diabetes.ipynd: Visualizations & insights.
6. README.md: Documentation.

---

## ETL Process Overview

1. **Extraction:** Raw health data loaded from CSV.
2. **Transform:** Cleaned column names, handled missing values, normalized data using `etl_diabetes.py`.
3. **Load:** Data inserted into a local SQLite database (`diabetes_health.db`).

---

## Key SQL Queries

- **Query 1:** Diabetes Rate by Age Group
- **Query 2:** Diabetes Rate by Gender

---

## Query Preview

<details>
<summary>Click to view Query 1 (Diabetes by Age Group)</summary>

```sql
SELECT age_group, COUNT(*) AS total,
       SUM(diabetes_012) AS diabetes_cases,
       ROUND(CAST(SUM(diabetes_012) AS FLOAT) / COUNT(*), 2) AS diabetes_rate
FROM health_indicators
GROUP BY age_group;

</details>
```

---

## Visual Insights

- Diabetes rates by age group (bar chart).
- Diabetes rates by gender (bar chart).
- Query validation included.

---

## Features

- Cleaned and transformed real-world health data.
- Built a local SQLite database for analysis.
- Executed SQL queries grouped by key demographics.
- Created reusable scripts for querying & visualization.

---

## Limitations and Next Steps

1. **More Demographics:** Current dataset lacks zip code, income level, and
   insurance information.
2. **Time Trends:** Add year-over-year data for trend analysis.
3. **Predictive Modeling:** Expand to logistic regression or decision trees.
4. **Interactive Dashboard:** Compare local results to CDC national data.

___

## How to Run

1. Clone the repo.
2. Run analysis.
3. Open visualization.

---

## Data Source

The dataset was sourced from Kaggle, including diabetes indicators, age, BMI, cholesterol, blood pressure, and physical activity. Transformed and loaded into diabetes_health.db for this project. Some download links may require a Kaggle login. 

## Author
H. Brooks 
