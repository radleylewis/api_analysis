import pandas as pd
import matplotlib.pyplot as plt

title = "Figure 1: Behavior Type Distribution"

# Load the dataset
df = pd.read_csv('remaining_behavior_ext.csv', sep=',\s*', engine='python')
df = df.loc[:, ~df.columns.str.startswith('Unnamed')]  # Drop unnamed columns

# Prepare data
counts = df['behavior_type'].value_counts().sort_index()

# Plot bar chart
plt.figure(figsize=(10, 6))
counts.plot(kind='bar', color='darkblue')

# Formatting
plt.xlabel('Behavior Type', fontsize=14, labelpad=15)
plt.ylabel('Frequency', fontsize=14, labelpad=15)
plt.title(title, fontsize=20, fontweight='bold', pad=20)
plt.xticks(rotation=0, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y')
plt.subplots_adjust(bottom=0.25)
plt.tight_layout()
plt.savefig('figure_1.png')
plt.show()

