import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = [
    {'cohort_year': 2015, 'customer_revenue': 2810.29},
    {'cohort_year': 2016, 'customer_revenue': 3034.87},
    {'cohort_year': 2017, 'customer_revenue': 3025.58},
    {'cohort_year': 2018, 'customer_revenue': 2771.85},
    {'cohort_year': 2019, 'customer_revenue': 2870.55},
    {'cohort_year': 2020, 'customer_revenue': 2290.48},
    {'cohort_year': 2021, 'customer_revenue': 2626.29},
    {'cohort_year': 2022, 'customer_revenue': 2282.55},
    {'cohort_year': 2023, 'customer_revenue': 2043.49},
    {'cohort_year': 2024, 'customer_revenue': 1878.38},
]

# Create DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='cohort_year', y='customer_revenue', palette='Blues_d')

# Labels and formatting
plt.title('Average Customer Revenue by First Purchase Year')
plt.xlabel('First Purchase Year')
plt.ylabel('Avg. Customer Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()