import pandas as pd
import matplotlib.pyplot as plt

title = "Figure 6: API Access Uniqueness (Binned)"

# Load the dataset
df = pd.read_csv('remaining_behavior_ext.csv', sep=',\s*', engine='python')
df = df.loc[:, ~df.columns.str.startswith('Unnamed')]  # Drop unnamed columns

# Create meaningful ranges for api_access_uniqueness
bins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
labels = ['Very Low (0–0.2)', 'Low (0.2–0.4)', 'Medium (0.4–0.6)', 
          'High (0.6–0.8)', 'Very High (0.8–1.0)']
df['uniqueness_category'] = pd.cut(df['api_access_uniqueness'], bins=bins, labels=labels)

# Prepare data
uniqueness_counts = df['uniqueness_category'].value_counts().sort_index()
sizes = uniqueness_counts.values
labels = uniqueness_counts.index.tolist()
explode = [0.05] * len(labels)

# Plot pie chart
plt.figure(figsize=(10, 6))
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    shadow=False,
    explode=explode,
    textprops={'fontsize': 12},
    labeldistance=1.15,
    pctdistance=0.85
)

# Formatting
plt.title(title, fontsize=14, fontweight='bold', pad=20)
plt.subplots_adjust(bottom=0.25)
plt.tight_layout()
plt.savefig('figure_6.png', dpi=300, bbox_inches='tight')
plt.show()
