import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("adult.data.csv")

# 1. Age Distribution
plt.figure()
df['age'].hist()
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.savefig("age_distribution.png")

# 2. Race Count (Bar Chart)
plt.figure()
df['race'].value_counts().plot(kind='bar')
plt.title("Race Count")
plt.xlabel("Race")
plt.ylabel("Count")
plt.savefig("race_count.png")

# 3. Education vs Salary
plt.figure()
pd.crosstab(df['education'], df['salary']).plot(kind='bar', stacked=True)
plt.title("Education vs Salary")
plt.xticks(rotation=45)
plt.savefig("education_salary.png")

# 4. Hours per week vs Salary
plt.figure()
df.boxplot(column='hours-per-week', by='salary')
plt.title("Work Hours vs Salary")
plt.savefig("hours_salary.png")

print("Charts created successfully ✅")
