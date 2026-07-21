# Pandas Projects

A collection of data analysis projects built while learning Pandas — progressing from a small structured dataset to a large, messy real-world-style dataset requiring full data cleaning and business analysis.

## 📂 Projects

### 1. Student Performance Analyzer
`students_performance/`

A CSV-based analysis of student marks across multiple subjects.
- Handling missing values in exam scores
- Calculating per-student averages and pass/fail status
- Identifying top-performing students
- Filtering students by attendance
- Exporting cleaned results to a new CSV

### 2. Company Sales Analyzer
`company_sales_analyzer/`

A retail sales dataset analysis covering a week of multi-product sales.
- Handling missing sales records
- Calculating revenue per product (units × price)
- Identifying best/worst performing days and products
- Comparing weekday vs. weekend sales performance
- Simulating discount pricing
- Flagging slow-moving inventory

### 3. E-Commerce Sales Data Cleanup
`E_commerce_sales_data/`

A large-scale (6,000+ row) e-commerce order dataset with realistic data quality issues, requiring a full cleaning and analysis pipeline.
- Removing duplicate order records
- Standardizing inconsistent city and payment method text (case, whitespace)
- Fixing data-entry bugs (negative quantities)
- Handling multiple missing-value columns with justified strategies
- Parsing mixed date formats into proper datetime objects
- Engineering a discount-adjusted `Revenue` column
- Business analysis: revenue by city/category/product, monthly trends, cancellation rates, customer ratings by category, payment method preferences
- Pivot tables and top-customer identification
- Exporting a fully cleaned, analysis-ready dataset

## 🛠 Tools & Libraries

- **Python**
- **Pandas** — data loading, cleaning, transformation, aggregation, merging
- **NumPy** — supporting numerical operations

## 📝 Notes

These projects were built progressively — each one increasing in dataset size and real-world messiness — to practice the full Pandas workflow: loading data, cleaning it, engineering features, running business analysis, and exporting results.
