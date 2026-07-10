import pandas as pd 
import numpy as np


# Deliverables

# Phase 1 — Data Quality Audit

# Data load karo, .info() aur .shape se overview lo.
df = pd.read_csv('ecommerce_orders.csv')
print(df.info())
print(df.shape)

# Har column mein missing values count karo.
print(np.sum(df.isna(), axis=0))

# Duplicate rows kitni hain check karo aur unhe hata do.
print(df.duplicated().sum())
df = df.drop_duplicates()
print(df.shape)

# City column ki unique values dekho — kitni "versions" ek hi shehar ki hain?
print(df['City'].value_counts(dropna=False))
print(df['City'].nunique())
print(df['City'].str.strip().str.title().unique())

# PaymentMethod mein bhi yahi issue check karo.
print(df['PaymentMethod'].str.strip().str.title().unique())
#----------------------------------------------------------------------------------------------------------------------------------------#

# Phase 2 — Cleaning

# City ko standardize karo — sab ek consistent format mein ho (jaise proper case, no extra spaces). Sab 8 shehar sirf 8 unique values ki tarah dikhne chahiye, 20+ nahi.
df['City'] = df['City'].str.strip().str.title()
df['City'] = df['City'].replace({'Karachi City':'Karachi', 'Isb':'Islamabad', 'Rwp':'Rawalpindi'})
print(df['City'].nunique())

# PaymentMethod ko bhi standardize karo isi tarah.
df['PaymentMethod'] = df['PaymentMethod'].str.strip().str.title()
df['PaymentMethod'] = df['PaymentMethod'].replace({'Cc':'Credit Card', 'Cod':'Cash On Delivery', 'Jazzcash':'Jazz Cash'})
df['PaymentMethod'] = df['PaymentMethod'].fillna('Unknown')
print(df['PaymentMethod'].nunique())

# Quantity mein negative values ek data-entry bug hain — inko fix karo (absolute value le lo, ya soch ke decide karo kya sahi approach hai).
df['Quantity'] = abs(df['Quantity'])
print(df['Quantity'])

# Quantity ke missing values handle karo — apna justified approach socho.
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].mean())
print(df['Quantity'].unique())

# OrderDate ko proper datetime mein convert karo (dono formats ko handle karna hoga — pd.to_datetime() ka format='mixed' ya dayfirst explore karo).
df['OrderDate'] = pd.to_datetime(df['OrderDate'], format='mixed')
print(df['OrderDate'])
#----------------------------------------------------------------------------------------------------------------------------------------#

# Phase 3 — Feature Engineering

# Revenue column banao: UnitPrice × Quantity × (1 - DiscountPercent/100)
df['Revenue'] = df['UnitPrice'] * df['Quantity'] * (1 - df['DiscountPercent']/100)
print(df['Revenue'])

# OrderDate se ek naya Month ya Year column nikalo (datetime ka .dt.month / .dt.year explore karo).
print(df['OrderDate'].dt.month)
print(df['OrderDate'].dt.year)
#----------------------------------------------------------------------------------------------------------------------------------------#

#Phase 4 — Business Analysis

# Sabse zyada revenue dene wala City kaunsa hai?
print(f"The highest profit: {df.groupby('City')['Revenue'].sum().max():.2f}")
print(f"The city with the highest profit: {df.groupby('City')['Revenue'].sum().idxmax()}")

# Sabse zyada revenue dene wala Category aur Product kaunsa hai?
print(f"The category with the highest profit: {df.groupby('Category')['Revenue'].sum().idxmax()}")
print(f"The product with the highest profit: {df.groupby('Product')['Revenue'].sum().idxmax()}")

# Month-wise total revenue trend nikalo — kaunsa mahina sabse zyada bika?
print(f"The most sales is in {df.groupby(df['OrderDate'].dt.month)['Revenue'].sum().idxmax()} month")

# OrderStatus = "Cancelled" ya "Returned" waale orders ka percentage kitna hai total orders mein se?
print(f"{len(df[(df['OrderStatus'] == 'Returned') | (df['OrderStatus'] == 'Cancelled') ]) / len(df['OrderStatus']) * 100:.2f} % orders are 'Returned' and 'Cancelled'.")

# Average Rating har Category ka nikalo — sabse zyada satisfaction kis category mein hai?
print(df.groupby('Category')['Rating'].mean())
print(f"The most satisfied category is: {df.groupby('Category')['Rating'].mean().idxmax()}")

# Payment method preference — kaunsa method sabse zyada use hota hai (percentage ke saath)?
print(f"The most used payment method is: {df['PaymentMethod'].value_counts().idxmax()}\nwith the percentage rate of {(df['PaymentMethod'].value_counts(normalize=True) * 100).max():.2f} %")
#----------------------------------------------------------------------------------------------------------------------------------------#

# Phase 5 — Advanced

# pivot_table banao — City rows mein, Category columns mein, Revenue sum values mein.
print(df.pivot_table(values='Revenue', index='City', columns='Category'))

# Top 10 customers (CustomerID) by total spending nikalo.
print(df.groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False).head(10))

# Final cleaned dataset ko cleaned_ecommerce_data.csv mein save karo (index=False yaad rakhna 😉).
df.to_csv('cleaned_ecommerce_data.csv', index=False)
