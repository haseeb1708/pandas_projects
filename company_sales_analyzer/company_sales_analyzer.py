import pandas as pd
import numpy as np

# Tasks:

# Section A — Load & Clean

# 1. CSV load karo. Shape aur .info() print karo.
df = pd.read_csv('company-sales.csv')
print(df.shape)
print(df.info())

# 2. Kitni missing values hain har column mein?
print(df.isna().sum())

# 3. UnitsSold ke missing values ko us Product ke average UnitsSold se fill karo 
# (hint: groupby + transform, ya simple average bhi chalega abhi).
df['UnitsSold'] = df['UnitsSold'].fillna(df.groupby('Product')['UnitsSold'].transform('mean'))
print(df['UnitsSold'])

# 4. Discount ke missing values ko 0 se fill karo (matlab discount nahi mila).
df['Discount'] = df['Discount'].fillna(0)
print(df['Discount'])
#----------------------------------------------------------------------------------------------------------------------------------------#

# Section B — New Columns

# 5. Revenue column banao: UnitsSold × UnitPrice × (1 - Discount/100)
df['Revenue'] = df['UnitsSold'] * df['UnitPrice'] * (1 - df['Discount']/100)
print(df['Revenue'])

# 6. Date column ko pd.to_datetime() se proper date type mein convert karo.
df['Date'] = pd.to_datetime(df['Date'])
print(df['Date'])
#----------------------------------------------------------------------------------------------------------------------------------------#

# Section C — Analysis

# 7. Har Region ka total Revenue nikalo (groupby + sum).
print(df.groupby('Region')['Revenue'].sum())

# 8. Har SalesRep ka total Revenue nikalo — sabse zyada revenue kisne banaya? (sort_values use karo)
print(df.groupby('SalesRep')['Revenue'].sum().sort_values(ascending=False))

# 9. Har Category ka average UnitPrice aur total UnitsSold nikalo (agg use karke, dono ek saath).
print(df.groupby('Category').agg({
    'UnitPrice': 'mean',
    'UnitsSold': 'sum'
}))
#----------------------------------------------------------------------------------------------------------------------------------------#

# Section D — Advanced Filtering

# 10. Wo saari orders nikalo jaha Discount 10 se zyada tha AUR Category "Electronics" thi.
filtered_orders = (df['Discount'] > 10) & (df['Category'] == 'Electronics')
print(df[filtered_orders])

# 11. pivot_table banao — Region rows mein, Category columns mein, Revenue ka SUM values mein.
print(df.pivot_table(values='Revenue', aggfunc='sum', index='Region', columns='Category'))
#----------------------------------------------------------------------------------------------------------------------------------------#

# Section E — Save

# 12. Poora processed DataFrame ek nayi CSV mein save karo: sales_report.csv
df.to_csv('company-sales-report.csv', index=False)