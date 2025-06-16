import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = [
    {'customer_status': 'Active', 'num_customers': 237, 'total_customers': 2825, 'status_percentage': 0.0839},
    {'customer_status': 'Churned', 'num_customers': 2588, 'total_customers': 2825, 'status_percentage': 0.9161},
    {'customer_status': 'Active', 'num_customers': 311, 'total_customers': 3397, 'status_percentage': 0.0916},
    {'customer_status': 'Churned', 'num_customers': 3086, 'total_customers': 3397, 'status_percentage': 0.9084},
    {'customer_status': 'Active', 'num_customers': 385, 'total_customers': 4068, 'status_percentage': 0.0946},
    {'customer_status': 'Churned', 'num_customers': 3683, 'total_customers': 4068, 'status_percentage': 0.9054},
    {'customer_status': 'Active', 'num_customers': 704, 'total_customers': 7446, 'status_percentage': 0.0945},
    {'customer_status': 'Churned', 'num_customers': 6742, 'total_customers': 7446, 'status_percentage': 0.9055},
    {'customer_status': 'Active', 'num_customers': 687, 'total_customers': 7755, 'status_percentage': 0.0886},
    {'customer_status': 'Churned', 'num_customers': 7068, 'total_customers': 7755, 'status_percentage': 0.9114},
    {'customer_status': 'Active', 'num_customers': 283, 'total_customers': 3031, 'status_percentage': 0.0934},
    {'customer_status': 'Churned', 'num_customers': 2748, 'total_customers': 3031, 'status_percentage': 0.9066},
    {'customer_status': 'Active', 'num_customers': 442, 'total_customers': 4663, 'status_percentage': 0.0948},
    {'customer_status': 'Churned', 'num_customers': 4221, 'total_customers': 4663, 'status_percentage': 0.9052},
    {'customer_status': 'Active', 'num_customers': 937, 'total_customers': 9010, 'status_percentage': 0.1040},
    {'customer_status': 'Churned', 'num_customers': 8073, 'total_customers': 9010, 'status_percentage': 0.8960},
    {'customer_status': 'Active', 'num_customers': 455, 'total_customers': 4718, 'status_percentage': 0.0964},
    {'customer_status': 'Churned', 'num_customers': 4263, 'total_customers': 4718, 'status_percentage': 0.9036},
]

# Load into DataFrame
df = pd.DataFrame(data)

# Add a cohort label to group bars by cohort size
df['cohort'] = df.groupby('total_customers').ngroup()

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='cohort', y='status_percentage', hue='customer_status')

# Formatting
plt.title('Churn vs. Active Status Percentage by Customer Cohort')
plt.xlabel('Customer Cohort (Grouped by Total Customers)')
plt.ylabel('Status Percentage')
plt.ylim(0, 1)
plt.legend(title='Customer Status')
plt.tight_layout()
plt.show()
