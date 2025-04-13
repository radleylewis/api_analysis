import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

title = "Figure 7: Behavior Type Distribution"

# Load the dataset
df = pd.read_csv('remaining_behavior_ext.csv', sep=',\s*', engine='python')
df = df.loc[:, ~df.columns.str.startswith('Unnamed')]  # Drop unnamed columns

# Count behavior types
behavior_counts = df['behavior_type'].value_counts().sort_index()

# Plot
plt.figure(figsize=(10, 6))
ax = sns.barplot(x=behavior_counts.index, y=behavior_counts.values, palette='viridis')

# Formatting
plt.title(title, fontsize=20, fontweight='bold', pad=20)
plt.xlabel('Behavior Type', fontsize=14, labelpad=15)
plt.ylabel('Count', fontsize=14, labelpad=15)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig('figure_7.png', dpi=300, bbox_inches='tight')
plt.show()

