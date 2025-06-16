# This code corresponds to Part 1: Customer Segmentation Analysis.
# It generates a pie chart to visualize how total spending is distributed among
# the top 25%, middle 50%, and bottom 25% of customers based on amount spent.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'customer_segment': ['1 - Low-Value', '3 - High-Value', '2 - Mid-Value'],
    'total_ltv': [4298367.206793759, 135606968.77156094, 66367810.47621527]
}
df = pd.DataFrame(data)

# Plot
colors = sns.color_palette("Set2", len(df))
plt.figure(figsize=(14, 14))
plt.pie(df['total_ltv'], labels=df['customer_segment'], autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Customer Segment Distribution by Total LTV', y=1.1)
plt.axis('equal')
plt.show()


