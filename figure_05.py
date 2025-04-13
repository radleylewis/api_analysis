import pandas as pd
import matplotlib.pyplot as plt

title = "Figure 5: API Access Uniqueness Distribution"

# Load the dataset
df = pd.read_csv('remaining_behavior_ext.csv', sep=',\s*', engine='python')
df = df.loc[:, ~df.columns.str.startswith('Unnamed')]  # Drop unnamed columns

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(df['api_access_uniqueness'], bins=20, color='lightgreen', edgecolor='black')

# Formatting
plt.xlabel('API Access Uniqueness', fontsize=14, labelpad=15)
plt.ylabel('Frequency', fontsize=14, labelpad=15)
plt.title(title, fontsize=22, fontweight='bold', pad=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y')
plt.subplots_adjust(bottom=0.25)
plt.tight_layout()
plt.savefig('figure_5.png')
plt.show()
