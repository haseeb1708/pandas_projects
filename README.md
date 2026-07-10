# Pandas Projects
 
A collection of hands-on Pandas projects built while practicing data cleaning, feature engineering, and business analysis on real-world style datasets.
 
---
 
## 1. Company Sales Analyzer
 
**Folder:** `company_sales_analyzer/`
 
A sales dataset analysis project focused on cleaning raw sales records and extracting business insights.
 
**What was done:**
- Loaded the dataset and inspected its shape, structure, and missing values
- Filled missing `UnitsSold` values using the average units sold per product (`groupby` + `transform`)
- Filled missing `Discount` values with 0 (treated as "no discount applied")
- Created a `Revenue` column using the formula: `UnitsSold × UnitPrice × (1 - Discount/100)`
- Converted the `Date` column to proper datetime format
- Calculated total revenue by **Region** and by **SalesRep** (ranked to find the top performer)
- Calculated average unit price and total units sold per **Category** using `agg()`
- Filtered orders with discount above 10% in the Electronics category
- Built a **pivot table** showing revenue by Region (rows) and Category (columns)
- Exported the final cleaned and processed dataset to a new CSV
**Key skills used:** `groupby`, `transform`, `agg`, `pivot_table`, boolean filtering, datetime conversion
 
---
 
## 2. E-commerce Sales Data
 
**Folder:** `E_commerce_sales_data/`
 
A larger, messier real-world style e-commerce orders dataset (6,000+ rows) focused heavily on data quality auditing and cleaning before analysis.
 
**What was done:**
- Performed a full data quality audit — shape, info, missing values, and duplicate rows (duplicates removed)
- Identified inconsistent `City` and `PaymentMethod` entries (same city/method written in multiple different formats)
- Standardized `City` values (trimmed spacing, fixed casing, merged variants like "Karachi City", "Isb", "Rwp" into consistent single labels)
- Standardized `PaymentMethod` values similarly (e.g. "Cc" → "Credit Card", "Cod" → "Cash On Delivery", "Jazzcash" → "Jazz Cash")
- Fixed negative `Quantity` values caused by data-entry errors (converted to absolute values)
- Filled missing `Quantity` values using the column mean
- Converted `OrderDate` to proper datetime, handling **mixed date formats** in the same column
- Engineered a `Revenue` column: `UnitPrice × Quantity × (1 - DiscountPercent/100)`
- Extracted `Month` and `Year` from order dates for time-based analysis
- Ran full business analysis:
  - City with the highest total revenue
  - Best-performing Category and Product by revenue
  - Month with the highest total sales
  - Percentage of orders that were Cancelled or Returned
  - Average customer rating per Category
  - Most-used payment method (with percentage share)
- Built a **pivot table** of revenue by City and Category
- Found the top 10 customers by total spending
- Exported the final cleaned dataset to `cleaned_ecommerce_data.csv`
**Key skills used:** data quality auditing, string cleaning (`str.strip`, `str.title`, `replace`), duplicate handling, mixed-format datetime parsing, `groupby`, `idxmax`, `pivot_table`, `value_counts`
 
---
 
## 3. Students Performance
 
**Folder:** `students_performance/`
 
A student marks dataset used to practice core data exploration and analysis workflows end-to-end.
 
**What was done:**
- Loaded the dataset and explored its shape, columns, and first few rows
- Counted missing values across all columns
- Filled missing `Math` and `English` scores using each subject's column average
- Created an `Average` column (row-wise mean of Math, English, and Science)
- Created a `Result` column using conditional logic — "Pass" if Average ≥ 60, otherwise "Fail"
- Calculated average marks per **City** using `groupby`
- Identified the **top 3 performing students** by highest average
- Filtered out students with attendance below 70% for an attendance risk check
- Exported the final results to a new CSV
**Key skills used:** `fillna`, row-wise `mean(axis=1)`, `apply()` with conditional logic, `groupby`, `sort_values`, filtering
 
---
 
## Tech Stack
 
- Python
- Pandas
- NumPy
