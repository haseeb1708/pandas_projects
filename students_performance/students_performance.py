import pandas as pd
import numpy as np

df = pd.read_csv("students-performance.csv")

# 1. Data Exploration
# CSV load karo. Shape, columns, aur pehli 5 rows (.head()) print karo.
print(df.shape)
print(df.columns)
print(df.head())

# 2. Missing Data
# Kitne total missing values hain (har column mein alag alag)?
print(np.sum(df.isna(), axis=0))

# 3. Fill Missing
# Math aur English ke missing values ko us column ke average se fill karo.
df['Math'] = df['Math'].fillna(df["Math"].mean())
print(df['Math'])

df['English'] = df['English'].fillna(df['English'].mean())
print(df['English'])

# 4. New Column
# "Average" naam ka column banao — Math, Science, English ka average (row-wise).
df['Average'] = df[['Math', 'English', 'Science']].mean(axis=1)
print(df)

# 5. Pass/Fail
# apply() ya np.where() use karke "Result" column banao:
# Average >= 60 → "Pass", warna "Fail"
df['Result'] = df['Average'].apply(lambda avrg: 'Pass' if avrg >= 60 else 'Fail')
print(df)

# 6. City-wise Analysis
# Har City ka average Marks (Average column ka) nikalo — groupby use karke.
print(df.groupby('City')['Average'].mean())

# 7. Top Performers
# Top 3 students (highest Average ke basis pe) ka Name aur Average print karo.
# (sort_values + head use kar sakta hai)
top_performers = df.sort_values(by='Average',ascending=False).head(3)
print(top_performers[['Name', 'Average']])

# 8. Attendance Insight
# Wo students nikalo jinki Attendance 70 se kam hai — filtering use karke.
high_attendance = df[df['Attendance'] < 70]
print(high_attendance)

# 9. Save Result
# Poora updated DataFrame ek nayi CSV file mein save karo:
# df.to_csv("student_results.csv", index=False)
df.to_csv('students-results.csv', index=False)
